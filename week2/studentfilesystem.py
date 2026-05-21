while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        with open("students.txt", "a") as file:
            file.write(name + "\n")

        print("Student Saved")

    elif choice == "2":
        with open("students.txt", "r") as file:
            content = file.read()
            print(content)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")