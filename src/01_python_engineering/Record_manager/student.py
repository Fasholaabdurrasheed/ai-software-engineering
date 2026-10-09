import json
import os 

FILENAME = "students.json"

def load_students(filename: str = FILENAME) -> list:
    """Load students list from JSON file. if file does not 
    exist, return an empty list."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

def save_students(students: list, filename: str = FILENAME) -> None:
    """Save students list back to JSON file."""
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)
# challenge 1 calculate_grade()
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

# grade = calculate_grade(85)
# print(grade)

# challenge 2 get_status()
def get_status(score: int) -> str:
    if score >= 45:
        return "Pass"
    else:
        return "Fail"

# challenge 3 calculate_average()
def calculate_average(students: list) -> float:
    # if not students:
        # return 0.0
    total_score = 0
    for student in students:
        total_score += student['score']
    return total_score / len(students) if students else 0.0

# find top student()
def find_top_student(students: list) -> tuple:
    if not students:
        return "", 0
    highest_score = students[0]['score']
    top_student = students[0]['name']
    for student in students:
        if student['score'] > highest_score:
            highest_score = student['score']
            top_student = student['name']
    return top_student, highest_score

# search_student()
def search_student(students: list, name: str) -> dict | None:
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None
# add student/create student record
def add_student(students: list, name: str, score: int) -> None:
    student = {
        "name": name,
        "score": score,
        "grade": calculate_grade(score),
        "status": get_status(score),
    }
    students.append(student)

