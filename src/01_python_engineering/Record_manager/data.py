# from student import calculate_grade, get_status, calculate_average, find_top_student
# # Add search functionality to find a student by name and display their details using a manual  search method.
# students = [
#     {"name": "Royhan", "score": 85},
#     {"name": "Mubarak", "score": 45},
#     {"name": "Mahmud", "score": 91},
#     {"name": "Rafash", "score": 67},
#     {"name": "John", "score": 39}
# ]
# search_name = input("Enter the student name: ")
# found = False
# passed_students = []
# total_score = 0
# highest_score = 0
# top_student = ""
# total_students = 0
# passed_count = 0
# failed_count = 0
# average_score = calculate_average(students)
# for student in students:
#     student["grade"] = calculate_grade(student['score'])
#     student["status"] = get_status(student["score"])
#     total_students += 1
    
    
#     # if student['score'] > highest_score:
#     #     highest_score = student['score']
#     #     top_student = student['name']

#     # if student["score"] >= 70:
#     #     student["grade"] = "A"
#     #     student["status"] = "Pass"
#     # elif student["score"] >= 60:
#     #     student["grade"] = "B"
#     #     student["status"] = "Pass"
#     # elif student["score"] >= 50:
#     #     student["grade"] = "C"
#     #     student["status"] = "Pass"
#     # elif student["score"] >= 45:
#     #     student["grade"] = "D"
#     #     student["status"] = "Pass"
#     # else:
#     #     student["grade"] = "F"
#     #     student["status"] = "Fail"

#     # if student['status'] == "Pass":
#         # passed_students.append(student['name'])

#     if student['score'] >= 45:
#         passed_count += 1
#     else:
#         failed_count += 1

# top_student, highest_score = find_top_student(students)
# print(f"{student['name']}: {student['score']} - {student['grade']} - {student['status']}")
# for student in students:
#     if student["name"].lower() == search_name.lower():
#         print("Student found:")
#         print(f"Name: {student['name']}")
#         print(f"Score: {student['score']}")
#         print(f"Grade: {student['grade']}")
#         print(f"Status: {student['status']}")
#         found = True
#         break

# if not found:
#     print("Student not found.")

# # average_score = total_score / total_students

# print("====== Student Summary ======")
# print(f"Total Students: {total_students}")
# print(f"Passed Students: {passed_count}")
# print(f"Failed Students: {failed_count}")
# print(f"Class Average: {average_score}")
# print(f"Top Student: {top_student}")
# print(f"Highest Score: {highest_score}")

def start():
    print("Welcome to the Student Record Management System!")
    