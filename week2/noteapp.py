while True:
    print("\n--- Notes App ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Write your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note Saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                content = file.read()

                print("\n--- Your Notes ---")
                print(content)

        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")