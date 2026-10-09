from student import (
    calculate_average,
    calculate_grade,
    find_top_student,
    get_status,
    search_student,
    add_student,
    load_students,
    save_students,
)


def main():
    students = load_students()
    
    print("========= Student Record Management System =========")
    print("1. Add a new student record")
    print("2. Process existing student records")
    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        name = input("Enter student name: ")
        score = int(input("Enter student score: "))
        add_student(students, name, score)
        
        # save updated list back to the disk
        save_students(students)
        print(f"\nStudent {name} added successfully!\n")

    # Process grades and status for any students missing them
    for student in students:
        if "grade" not in student:
            student["grade"] = calculate_grade(student["score"])
        if "status" not in student:
            student["status"] = get_status(student["score"])

    # Display updated student records
    print("===== Student Records =====")
    for student in students:
        print(
            f"Name: {student['name']} | Score: {student['score']} | "
            f"Grade: {student['grade']} | Status: {student['status']}"
        )

    # Calculate class average
    average = calculate_average(students)
    print(f"\nClass Average: {average:.1f}")

    # Find top student
    top_student, highest_score = find_top_student(students)
    print(f"Top Student: {top_student} ({highest_score})")

    # Search for a student
    search_name = input("\nEnter student name to search: ")
    student = search_student(students, search_name)

    if student:
        print("\nStudent Found:")
        print(f"Name: {student['name']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {student['grade']}")
        print(f"Status: {student['status']}")
    else:
        print("\nStudent not found.")


if __name__ == "__main__":
    main()