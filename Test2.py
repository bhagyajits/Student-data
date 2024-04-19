class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = float(input("Enter student's grade: "))
    student = Student(name, age, grade)
    return student

def display_student(student):
    print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

def main():
    students = []

    while True:
        print("\nStudent Data Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student = add_student()
            students.append(student)
            print("Student added successfully!")
        elif choice == '2':
            if not students:
                print("No student records found.")
            else:
                print("\nStudent Records:")
                for student in students:
                    display_student(student)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
