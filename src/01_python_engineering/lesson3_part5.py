# Lesson 3 Part 5 Challenge

# Challenge 1 - Squares
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number  in numbers]
print(squares)

# Challenge 2 - Even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Challenge 3 - Student names
students = [
    {"name": "Royhan", "score": 85},
    {"name": "Mubarak", "score": 45},
    {"name": "Mahmud", "score": 91},
    {"name": "Rafash", "score": 67}
]
student_names = [student['name'] for student in students]
print(student_names)

# Challenge 4 - Passed student
passed_students = [student['name'] for student in students if student["score"] >= 50]
print(passed_students)

# Challenge 5 - A little more technical
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(square_even_numbers)