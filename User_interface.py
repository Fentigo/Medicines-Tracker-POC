import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def display_menu():
    print("========== Pharmacy Inventory Management ==========")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. View Medicines Expiring Soon")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice


def add_medicine():
    print(" Enter the following information")
    name = input('insert medicine name')
    batch_number = input ('inser batch number')
    quantity = int(input('Enter Quantity here'))
    expiry_date = input('Enter date here YYYY-MM-DD')
    cursor.execute ("INSERT INTO medicines (name, batch_number, quantity, expiry_date) VALUES (?, ?, ?, ?)", 
                    (name, batch_number, quantity, expiry_date))
    connect.commit()
    connect.close
    pass

def view_medicine():
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()

    print("Medicine ID | Name    | Batch Number | Quantity | Expiry Date")
    print ("--------------------------------------------")
    for row in rows: 
        print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  |{row[3]:8}  | {row[4]}")
    connect.commit()
    connect.close
    pass

def view_expiring_medicine():
    #placeholder 
    pass
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            view_expiring_medicines()
        elif choice == '4':
            print("Exiting the Pharmacy Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

display_menu()