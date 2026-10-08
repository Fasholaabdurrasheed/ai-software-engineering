# Challenge 1 - Student list
# Create a list containing 5 student names.
students = ["Royhan", "Mubarak", "Mahmud", "Ma'ruf", "Maryam"]

# Print the first student
print("First student:", students[0])

# Print the last student
print("Last student:", students[-1])

# Add another student 
students.append("Rafash")

# Remove one student
students.remove("Maryam")

# Print the final list.
print("Final student list:", students)

# Print the number of students 
print("Number of students:", len(students))

# Challenge 2 - Loop: using the same list
print("\nLooping through the student list:")
for student in students:
    print(f"Student: {student}")

#  Challenge 3 - Student dictionary
student = {
    "name": "Royhan",
    "age": 20,
    "department": "Computer Science",
    "score": 85
}

# Print the student's name
print("\nStudent's name:", student["name"])

# Print the student's score
print("Student's score:", student["score"])

# Change the student's score
student["score"] = 90

# Add a level key
student["level"] = "Undergraduate"

# Loop through the dictionary and print key-value pairs
print("\nStudent details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Challenge 4 - Combine them
# Create three student dictionaries and put them inside a list.

student_list = [
    {
        "name": "Fashola",
        "score": 88
    }, 
    {
        "name": "Mubarak",
        "score": 92
    },
    {
        "name": "AbdurRasheed",
        "score": 95
    }
]

# Loop through them and print each student's name and score
print("\nStudent list details:")
for student_record in student_list:
    print(f"{student_record['name']} -> {student_record['score']}")

print(f"{student_list[0]['name']}")