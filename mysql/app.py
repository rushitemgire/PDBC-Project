from db_operations import create_table, create_user, get_users, update_user, delete_user

def menu():
    print("=== User Management System ===")
    print("1. Create User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

create_table()  # Ensure the table exists

while True:
    menu()
    choice = input("Enter your choice: ")
    
    match choice:

        case '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)

        case '2':
            print("User List:")
            get_users()

        case '3':
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            update_user(user_id, new_name, new_email)

        case '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        case '5':
            print("Project Terminated")
            break

        case _:
            print("Invalid choice. Please try again.")


