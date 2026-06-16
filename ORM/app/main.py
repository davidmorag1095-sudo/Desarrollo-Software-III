from ORM.app.controller.student_controller import StudentController
from ORM.app.config.database import init_db

def menu():
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. Get Student")
    print("3. List Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

if __name__ == "__main__":
    init_db()
    controller = StudentController()

    while True:
        menu()
        option = input("Choose an option: ")

        if option == "1":
            carnet = input("Carnet: ")
            name = input("Name: ")
            age = int(input("Age: "))
            controller.create(carnet, name, age)

        elif option == "2":
            carnet = input("Carnet: ")
            controller.get(carnet)

        elif option == "3":
            controller.list()

        elif option == "4":
            carnet = input("Carnet: ")
            name = input("New Name: ")
            age = int(input("New Age: "))
            controller.update(carnet, name, age)

        elif option == "5":
            carnet = input("Carnet: ")
            controller.delete(carnet)

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")
