from managers.StudentManager import StudentManager
from models.Graduate import Graduate
from models.student import Student

manager = StudentManager()
student_id_counter = 1

while True:
    print("\nWelcome to Student Performance Tracker")
    print("1. Add Student (regular or graduate)\n2. Remove Student\n3. Search by Name\n4. Add Subject Scores\n5. List All Students\n6. Top Scorer in Subject\n7. Department Average\n8. Exit\n")

    choice = input("Enter choice: ")

    if choice == '1':
        student_type = input(
            "Enter student type (regular/graduate): ").strip().lower()
        name = input("Enter name: ")
        department = input("Enter department: ")
        if student_type == 'regular':
            student_id = f"S{student_id_counter:04d}".strip().lower()
            student_obj = Student(student_id, name, department)
            manager.add_student(student_obj)
            print("Student added successfully!")
        elif student_type == 'graduate':
            student_id = f"G{student_id_counter:04d}"
            thesis_title = input("Enter thesis title: ")
            graduate_student = Graduate(
                student_id, name, department, thesis_title)
            manager.add_student(graduate_student)
            print("Graduate student added successfully!")
        else:
            print("Invalid student type. Please enter 'regular' or 'graduate'.")
        student_id_counter += 1

    elif choice == '2':
        student_id = input("Enter student ID to remove: ")
        if manager.remove_student(student_id):
            print("Student removed successfully!")
        else:
            print("Student not found.")

    elif choice == '3':
        name = input("Enter name to search: ").strip().lower()
        found_student = manager.find_student_by_name(name)
        if found_student:
            print(found_student)
        else:
            print("Student not found.")

    elif choice == '4':
        student_id = input("Enter student ID to add scores: ")
        student_obj = next((s for s in manager.list_students()
                           if s.student_id == student_id), None)
        if student_obj:
            subject = input("Enter subject: ")
            try:
                marks = float(input("Enter marks: "))
                student_obj.add_score(subject, marks)
                print("Score added successfully!")
            except ValueError:
                print("Invalid marks. Please enter a number.")
        else:
            print("Student not found.")

    elif choice == '5':
        students = manager.list_students()
        if students:
            for s in students:
                print(s)
                print("-" * 40)
        else:
            print("No students found.")

    elif choice == '6':
        subject = input("Enter subject: ").strip().lower()
        top_student = manager.get_top_scorer(subject)
        if top_student:
            print("Top scorer in", subject, "is:")
            print(top_student)
        else:
            print("No scores found for this subject.")

    elif choice == '7':
        department = input("Enter department: ")
        avg = manager.get_department_average(department)
        print(f"Average score for {department}: {avg:.2f}")

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
