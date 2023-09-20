# there's a cleaner way to do this using modules
from datetime import datetime, timedelta
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
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
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    return choice


def main():
    # i want to implement a loop here to always checking for expiry alerts. 
    display_menu()
        
    while True:
        choice = display_menu()
        if choice == '1':
            try:
                from Modules.add_medicine import add_medicine
                add_medicine()
            except ValueError:
                print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '2':
            try: 
                from Modules.view_medicine import view_medicines
                view_medicines()
            except ValueError:
                print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '3':
            try:
                from Modules.expiring_medicines import view_expiring_medicine
                view_expiring_medicine()
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '4':
            try: 
                from Modules.update_expiry_date import update_expiry_date
                update_expiry_date()
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '5':
            try: 
                from Modules.update_quantity import update_medicine_quantity
                update_medicine_quantity()
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '6':
            try:
                from Modules.delete import delete_medicine
                delete_medicine()
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '7':
            try:
                from Modules.search_medicine import search
                search()
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '8':
            try:
                from Modules.check_expired_medicines import check_expired_medicines
                check_expired_medicines()
                print("Exiting the Pharmacy Inventory Management System.")
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        elif choice == '9':
            try:
                from Modules.check_expired_medicines import check_expired_medicines
                check_expired_medicines()
                print("Exiting the Pharmacy Inventory Management System.")
            except ValueError:
                 print("Invalid input. Please enter valid details")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            break
        else:
            print("Invalid choice. Please try again.")
        
main()