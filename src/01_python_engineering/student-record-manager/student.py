import json
import os 
from typing import Tuple, List, Optional

FILENAME = "students.json"

def load_students(filename: str = FILENAME) -> list:
    """Load students list from JSON file. if file does not 
    exist, return an empty list."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_students(students: list, filename: str = FILENAME) -> None:
    """Save students list back to JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
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

# challenge 2 get_status()
def get_status(score: int) -> str:
    if score >= 45:
        return "Pass"
    else:
        return "Fail"

# challenge 3 calculate_average()
def calculate_average(students: list) -> float:
    if not students:
        return 0.0
    total_score = 0
    for student in students:
        total_score += student['score']
    return total_score / len(students) if students else 0.0

# find top student()
def find_top_student(students: List[dict]) -> Optional[Tuple[str, int]]:
    """Returns (name, score) of the top student, or None if the record list is empty."""
    if not students:
        return None
    highest_score = students[0]['score']
    top_student = students[0]['name']
    for student in students:
        if student['score'] > highest_score:
            highest_score = student['score']
            top_student = student['name']
    return top_student, highest_score

# search_student()
def search_student(students: List[dict], name: str) -> Optional[dict]:
    clean_name = name.strip().lower()
    if not clean_name:
        return None
    for student in students:
        if student['name'].strip().lower() == clean_name:
            return student
    return None
def validate_score(score: int) -> None:
    if not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 100:
        raise ValueError("Score must be an integer between 0 and 100.")

# add student/create student record
def add_student(students: List[dict], name: str, score: int) -> None:
    clean_name = name.strip()
    
    # 1. Validate non-empty name
    if not clean_name:
        raise ValueError("Student name cannot be empty.")
        
    # 2. Check for duplicate names
    if search_student(students, clean_name) is not None:
        raise ValueError(f"A student with the name '{clean_name}' already exists.")

    # 3. Validate score range/type
    validate_score(score)

    student = {
        "name": clean_name,
        "score": score,
        "grade": calculate_grade(score),
        "status": get_status(score),
    }
    students.append(student)
