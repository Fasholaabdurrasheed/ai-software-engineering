# Challenge 1 - Basic grading
score = int(input("Enter your score: "))

if score >= 70:
    print("Grade: A")
elif score  >= 60:
    print("Grade: B")
elif score >=  50:
    print("Grade: C")
elif score >= 45:
    print("Grade: D")
else:
    print("Grade: F")

# Challenge 2 - Student eligibility
attendance = 80
if attendance >= 75:
    print(f"Attendance: {attendance}%\nStatus: Eligible")
else:
    print(f"Attendance: {attendance}%\nStatus: Not Eligible")

# Challenge 3 - Combine both challenges
# create a dictionary to store student info and use the dictionary values to determine:
# Student's name, score, grade, examination eiligibility, and attendance status.
student = {
    "name": "Royhan",
    "score": 68,
    "attendance": 82
}

# Use the dictionary values to determine the student's grade
if student["score"] >= 70:
    student["grade"] = "A"
elif student["score"] >= 60:
    student["grade"] = "B"
elif student["score"] >= 50:
    student["grade"] = "C"
elif student["score"] >= 45:
    student["grade"] = "D"
else:
    student["grade"] = "F"

# Use the dictionary values to determine the student's examination eligibility
if student["attendance"] >= 75:
    student["eligibility"] = "Eligible"
else:
    student["eligibility"] = "Not Eligible"

# Print the student's information
print(f"Student: {student['name']}")
print(f"Score: {student['score']}")
print(f"Grade: {student['grade']}")
print(f"Attendance: {student['attendance']}%")
print(f"Status: {student['eligibility']}")