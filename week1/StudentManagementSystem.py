students=[]

def add_student():

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():

    if len(students) == 0:
        print("No students found.")
       

    for s in students:
        print("Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")



def check_results():

    name = input("Enter student name to check results: ")

    for s in students:
        if s["name"] == name:
            marks = int(input("Enter marks for {name}: "))
            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
            return

    print("Student not found.")


def del_student():

    name = input("Enter student name to delete: ")

    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def search_student():

    name = input("Enter student name to search: ")

    for s in students:
        if s["name"] == name:
            print("Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
            return

    print("Student not found.")


def show_highestmarks():

    if len(students) == 0:
        print("No students found.")
        return

    highest_marks = -1
    top_student = None

    for s in students:
        marks = int(input("Enter marks for {s['name']}: "))
        if marks > highest_marks:
            highest_marks = marks
            top_student = s

    print("Top student: {top_student['name']} with marks: {highest_marks}")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Results")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Show Highest Marks")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        check_results()
    elif choice == 4:
        del_student()
    elif choice == 5:
        search_student()  
    elif choice == 6:
        show_highestmarks() 
    elif choice == 7:   
        print("Exiting the program. Goodbye!")    
        break
    else:
        print("Invalid choice. Please try again.")