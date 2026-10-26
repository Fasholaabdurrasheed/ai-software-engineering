from student import (
    calculate_average,
    calculate_grade,
    find_top_student,
    get_status,
    search_student,
    add_student,
    load_students,
    save_students,
    validate_score,
)


def main():
    students = load_students()
    
    print("========= Student Record Management System =========")
    print("1. Add a new student record")
    print("2. Process existing student records")
    option = input("Enter your choice (1 or 2): ").strip()

    while option not in {"1", "2"}:
        print("Invalid choice. Please enter 1 or 2.")
        option = input("Enter your choice (1 or 2): ").strip()

    if option == "1":
        # Loop until a valid, non-empty, non-duplicate name is provided
        while True:
            name = input("Enter student name: ").strip()
            if not name:
                print("Error: Student name cannot be empty. Please try again.")
                continue
            if search_student(students, name) is not None:
                print(f"Error: A student named '{name}' already exists. Please enter a unique name.")
                continue
            break

        # Loop until a valid integer score (0-100) is provided
        while True:
            try:
                score = int(input("Enter student score: "))
                validate_score(score)
                break
            except ValueError:
                print("Invalid score. Please enter an integer between 0 and 100.")
        
        # Add and persist student record
        add_student(students, name, score)
        save_students(students)
        print(f"\nStudent '{name}' added successfully!\n")

    # Process grades and status for any students missing them
    records_updated = False
    for student in students:
        if "grade" not in student:
            student["grade"] = calculate_grade(student["score"])
            records_updated = True
        if "status" not in student:
            student["status"] = get_status(student["score"])
            records_updated = True

    if records_updated:
        save_students(students)

    # Display student records
    print("===== Student Records =====")
    if not students:
        print("No student records available.")
    else:
        for student in students:
            print(
                f"Name: {student['name']} | Score: {student['score']} | "
                f"Grade: {student['grade']} | Status: {student['status']}"
            )

    # Calculate class average
    average = calculate_average(students)
    print(f"\nClass Average: {average:.1f}")

    # Safely handle find_top_student return value (Tuple or None)
    top = find_top_student(students)
    if top:
        top_student, highest_score = top
        print(f"Top Student: {top_student} ({highest_score})")
    else:
        print("Top Student: N/A (No records exist)")

    # Search for a student
    search_name = input("\nEnter student name to search: ").strip()
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