def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "," + course + "\n")

    print("Student added successfully!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No students found.")
            else:
                for line in data:
                    name, age, course = line.strip().split(",")
                    print(f"Name: {name}, Age: {age}, Course: {course}")
    except FileNotFoundError:
        print("No file found.")

def search_student():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, age, course = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Found: {name}, {age}, {course}")
                    found = True
    except FileNotFoundError:
        print("No file found.")

    if not found:
        print("Student not found.")

def delete_student():
    delete_name = input("Enter name to delete: ")
    lines = []

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                name, age, course = line.strip().split(",")
                if name.lower() != delete_name.lower():
                    file.write(line)

        print("Student deleted (if existed).")
    except FileNotFoundError:
        print("No file found.")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")