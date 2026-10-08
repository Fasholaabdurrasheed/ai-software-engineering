students = [
    {"name":"Royhan", "score": 85, "attendance": 75},
    {"name":"Mubarak", "score": 82, "attendance": 80},
    {"name":"Mahmud", "score": 91, "attendance": 72},
    {"name":"Badmus", "score": 68, "attendance": 90},
    {"name": "Shuaib", "score": 59, "attendance": 75}
]

for student in students:
    if student["score"] >= 70:
        student["grade"] = "A"
    elif student["score"] >= 60:
        student["grade"] = "B"
    elif student["score"] >= 50:
        student["grade"] = "c"
    elif student["score"] >= 44:
        student["grade"] = "D"

    else:
        print("F")

    if student['attendance'] >= 75:
        student['eligibility'] = "Eligible"
    else:
        student['eligibility'] = "Not Eligible"

# print student infomation
    # print(f"student: {student['name']}")
    # print(f"Grade:  {student['grade']}")
    # print(f"Attendance: {student["attendance"]}%")
    # print(f"Status: {student['eligibility']}")


# Without a loop we have to write 
classes = ["JSS1", "JSS2", "JSS3", "SSS1", "SSS2", "SSS3"]
# print(classes[0])
# print(classes[1])
# print(classes[2])
# print(classes[3])
# print(classes[4])
# print(classes[5])

# for key in students:
    # print(f"{key['name']}: {key['score']}")


data = {
    "name": "Shapy",
    "age": 20,
    "department": "Agricultural Science",
    "score": 95
}
# for key, value in data.items():
    # print(f"{key}: {value}")

# range()
# for number in range(5):
    # print(number)
# for num in range(0, 11, 2):
    # print(num)

count = 1
# while count <= 5:
#     print(count)
#     count += 1
# for row in range(1, 6):
#     for col in range(1, 6):
#         print(f"Row: {row}, Column: {col}")

even_numbers = []

for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print(squares)