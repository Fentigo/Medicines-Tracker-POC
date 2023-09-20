#Update medical quantity
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()


def update_medicine_quantity():
    try:
        medicine_id = input('Enter medicine ID here')
        cursor.execute("SELECT * FROM medicines WHERE ID IS ? ", (medicine_id,))
        rows = cursor.fetchall() 
        if not rows:
            print ("Medicine ID is not found")
        else:
            medicine_name = rows[0][1]
            current_quantity = rows[0] [3]
            expiry_date = rows[0] [4]
            print(f"The current Quantity of {medicine_name} is {current_quantity},its expiry date is {expiry_date}.")
            cont = input("Do you want to update this quantity? (Y/N)")
            if cont == "Y":
                new_quantity = int(input('Enter the updated product quantity:'))
                cursor.execute("UPDATE medicines SET quantity = ? WHERE ID = ?", (new_quantity, medicine_id))
                connect.commit()

            #retrieve and display new quantity
                cursor.execute("SELECT * FROM medicines WHERE ID IS ? ", (medicine_id,))
                updated_rows = cursor.fetchall()
                medicine_name = updated_rows [0][1]
                expiry_date = updated_rows [0][4]
                print("Update successful!")
                print(f"The new quantity of {medicine_name} is {new_quantity}, its expiry date is {expiry_date} ")
            else: 
                print("closing connection now")
            connect.close()
    except ValueError:
        print("Invalid input. Please enter valid details")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

update_medicine_quantity() 