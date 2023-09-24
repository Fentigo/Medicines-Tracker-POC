from Modules.add_medicine import add_medicine
from Modules.view_medicine import view_medicines
from Modules.expiring_medicines import view_expiring_medicine
from Modules.update_expiry_date import update_expiry_date
from Modules.update_quantity import update_medicine_quantity
from Modules.delete import delete_medicine
from Modules.search_medicine import search
from Modules.check_expired_medicines import check_expired_medicines
import sqlite3

def display_menu():
    print("========== Pharmacy Inventory Management ==========")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. View Medicines Expiring Soon")
    print("4. Update Expiry Date")
    print("5. Update Quantity")
    print("6. Delete Medicine")
    print("7. Search Medicine")
    print("8. Check Alerts")
    print("9. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")
    return choice

def main():
    menu_functions = {
        '1': add_medicine,
        '2': view_medicines,
        '3': view_expiring_medicine,
        '4': update_expiry_date,
        '5': update_medicine_quantity,
        '6': delete_medicine,
        '7': search,
        '8': check_expired_medicines,
        '9': exit_program,
    }
    
    while True:
        choice = display_menu()
        if choice in menu_functions:
            try:
                menu_functions[choice]()
            except ValueError:
                print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please try again.")

def exit_program():
    print("Exiting the Pharmacy Inventory Management System.")

if __name__ == '__main__':
    main()
