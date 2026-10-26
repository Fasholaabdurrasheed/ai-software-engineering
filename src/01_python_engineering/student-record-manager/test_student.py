import pytest
import json

from student import calculate_grade, validate_score, add_student, load_students, save_students
# parameterized test for calculate_grade function

# sample test cases for calculate_grade function
@pytest.mark.parametrize("score, expected_grade",
    [
        (85, "A"),
        (65, "B"),
        (55, "C"),
        (45, "D"),
        (40, "F"),
        (44, "F"),
        (70, "A"),
        (69, "B"),
        (0, "F"),
    ],
    )

def test_calculate_grade(score, expected_grade):
    assert calculate_grade(score) == expected_grade

# test for valid score inputs (validate_score returns None on success)
@pytest.mark.parametrize("score", [1, 100, 0])
def test_validate_score_valid(score):
    # Should complete without raising an exception
    validate_score(score)

# Test for invalid score inputs (validate_score raises ValueError)
@pytest.mark.parametrize("score", [-1, 101, 75.5, "string", True, None])
def test_validate_score_invalid(score):
    with pytest.raises(ValueError):
        validate_score(score)

# Fixture providing a clean base list for existing records
@pytest.fixture
def sample_students():
    return [
        {"name": "Royhan","score": 85,"grade": "A","status": "Pass"},
        {"name": "Mubarak","score": 45,"grade": "D","status": "Pass" },
        {"name": "Mahmud","score": 91,"grade": "A","status": "Pass"},
    ]

@pytest.mark.parametrize("name, score, expected_grade, expected_status",[
    ("john", 85, "A", "Pass"),
    ("jane", 40, "F", "Fail"),
    ("rafash", 67, "B", "Pass"),
])
def test_add_student_success(sample_students, name, score, expected_grade, expected_status):
    add_student(sample_students, name, score)
    # Find the newly added student
    record = next((s for s in sample_students if s['name'] == name), None)
    assert record is not None
    assert record['score'] == score
    assert record['grade'] == expected_grade
    assert record['status'] == expected_status

# 3 reject an invalid score without adding the student record 

@pytest.mark.parametrize(
    "invalid_score",
    [-1, 101, 85.5, "string", True, None],
)
def test_add_student_invalid_score(sample_students, invalid_score):
    initial_count = len(sample_students)

    with pytest.raises(ValueError):
        add_student(sample_students, "invalid_student", invalid_score)

    # These assertions run after ValueError is confirmed.
    assert len(sample_students) == initial_count
    assert all(
        student["name"] != "invalid_student"
        for student in sample_students
    )

# 4 leave existing records intact when adding another student 
def test_add_student_existing_records_records(sample_students):
    initial_first_student = sample_students[0].copy()
    initial_second_student = sample_students[1].copy()
    initial_third_student = sample_students[2].copy()

    add_student(sample_students, "NewStudent", 90)
    # Verify the original records remain unchanged 
    assert sample_students[0] == initial_first_student
    assert sample_students[1] == initial_second_student
    assert sample_students[2] == initial_third_student
    assert len(sample_students) == 4  # New student added, total should be 4 

def test_save_students(sample_students, tmp_path):
    file_path = tmp_path / "students.json"
    save_students(sample_students, file_path)

    # Load the file and verify its contents
    with open(file_path, "r", encoding="utf-8") as file:
        loaded_students = json.load(file)
    assert loaded_students == sample_students
# Test A - Load an existing file
def test_load_students_existing_file(sample_students, tmp_path):
    # 1. Create file_path using tmp_path
    file_path = tmp_path / "students.json"

    # 2. write sample_students to that file using json.dump()
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(sample_students, file)

    # 3. Call load_students(file_path) after the file has been flushed and closed
    loaded = load_students(file_path)

    # 4. Assert that the returned list equals sample_students
    assert loaded == sample_students

# Test B - Load a missing file
def test_load_students_missing_file(tmp_path):
    # 1. Create a path called missing.json inside tmp_path
    missing_path = tmp_path / "missing.json"

    # 2. Do NOT create the file

    # 3. Call load_students() with that path
    result = load_students(missing_path)

    # 4. Assert that the result is an empty list
    assert result == []
  

def test_load_students_invalid_json(tmp_path):
    invalid_path = tmp_path / "invalid.json"
    invalid_path.write_text(
        "{invalid_json: true,}",
        encoding="utf-8",
    )

    with pytest.raises(json.JSONDecodeError):
        load_students(invalid_path)


