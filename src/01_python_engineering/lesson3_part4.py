# Challenge 1 - Basic for loop
students = ["Royhan", "Mubarak", "Mahmud", "Rafash"]
for student in students:
    print(f"Student: {student}")

# Challenge 2 - range()
for i in range(1, 11):
    print(i)

for i in range(0, 11, 2):
    print(i)

# Challenge 3 - Student records create 
students_record = [
    {"name": "Royhan", "score": 85},
    {"name": "Mubarak", "score": 52},
    {"name": "Mahmud", "score": 91},
    {"name": "Rafash", "score": 67}
]

for student in students_record:
    if student['score'] >= 50:
        student['status'] = "Pass"
    else:
        student['status'] = "Fail"

    print(f"{student['name']}: {student['score']} - {student['status']}")

# Challenge 4  - Use of continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# Challenge 5 - Use of break
for number in numbers:
    if number == 6:
        break
    print(number)