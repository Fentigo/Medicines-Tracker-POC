import sqlite3
import datetime
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()

def add_medicine():
    print("Enter the following information")

    try:
        connect = sqlite3.connect('inventory db')
        cursor = connect.cursor()

        name = input('Insert medicine name: ')
        batch_number_input = input('Insert batch number: ')
        batch_number = "BATCH" + batch_number_input
        quantity = int(input('Enter Quantity here: '))
        expiry_date_str = input('Enter date here (YYYY-MM-DD): ')

        try:
            expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            return

        cursor.execute("INSERT INTO medicines (name, batch_number, quantity, expiry_date) VALUES (?, ?, ?, ?)",
                       (name, batch_number, quantity, expiry_date))
        connect.commit()
        print('Medicine has been added successfully!')

    except ValueError:
        print("Invalid input. Please enter valid details")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        connect.close()
