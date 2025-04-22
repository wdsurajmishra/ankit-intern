from opertaion import Management

welcomemsg = """
Welcome to the Employee Management System (EMS) project! 
_____________________________________________________________
"""

print(welcomemsg)

while True:
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Exit")
    choice = input("Please select an option (1-3): ")

    if choice == '1':
        name = input("Enter employee name: ")
        role = input("Enter employee role: ")
        mgs = Management.add_employee(name, role)
        print(mgs)

    elif choice == '2':
        mgs = Management.list_employees()
        print(mgs)

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
