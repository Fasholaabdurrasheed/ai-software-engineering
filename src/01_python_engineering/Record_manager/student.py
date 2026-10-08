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
    highest_score = students[0]['score'] if students else 0
    top_student = ""
    for student in students:
        if student['score'] > highest_score:
            highest_score = student['score']
            top_student = student['name']
    return top_student, highest_score


cal_avg = calculate_average([])
print(cal_avg)
    