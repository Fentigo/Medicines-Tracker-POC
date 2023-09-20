import sqlite3
from datetime import datetime, timedelta
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def check_expiring_medicines():
    print ("Checking for expired medicines..")
    current_date = datetime.today().date()

    # calculate the date range for expiring medicines 
    end_date = current_date + timedelta(days = 7)

    cursor.execute('SELECT * FROM medicines WHERE expiry_date < ?', (current_date,))
    expiring_medicines = cursor.fetchall()

    if not expiring_medicines:
        print("No expiring medicines found within the next 7 days.")
    else: 
        print("Expiring Medicines (within 7 days):")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in expiring_medicines:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")


            # Alert Feature
            print ("Alert some medicines are expring within next 7 days.")
            action = input("Take actions? (Y/N): ")
            if action == 'Y':
                print("========== Pharmacy Inventory Management ==========")
                print("1. Update Expiry Date")
                print("2. Delete Medicine")
                print("3. Exit")
                choice = input("Enter your choice (1/2/3: ")
                return choice
            if choice == '1':
                from update_expiry_date import update_expiry_date
                update_expiry_date()
            elif choice == '2':
                from delete import delete_medicine
                delete_medicine()
            elif choice == '3':
                print('Exiting the application')
            break
check_expiring_medicines()