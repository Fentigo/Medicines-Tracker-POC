import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()

import sqlite3

def delete_medicine():
    try:
        connect = sqlite3.connect('inventory db')
        cursor = connect.cursor()

        medicine_id = input("Enter Medicine ID: ")
        cursor.execute("SELECT * FROM medicines WHERE id = ?", (medicine_id,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No medicine found with ID {medicine_id}")
            return

        medicine_name = rows[0][1]
        batch_number = rows[0][2]
        quantity = rows[0][3]
        expiry_date = rows[0][4]

        print(f"{medicine_id} | {medicine_name} | {batch_number} | {quantity} | {expiry_date}")
        cont = input("Is this the medicine you want to delete? (Y/N): ")

        if cont.upper() == 'N':
            print("Closing the connection now.")
        else:
            cursor.execute("DELETE FROM medicines WHERE id = ?", (medicine_id,))
            connect.commit()
            print(f"{medicine_name} with ID {medicine_id} has been deleted")
            print("Medicine has been deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter valid details")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connect.close()

    
    
