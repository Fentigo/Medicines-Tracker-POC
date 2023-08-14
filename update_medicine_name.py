#Update Medicine Name
#Update medical quantity
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()


def update_medicine_name():
    medicine_id = input('Enter medicine ID here')
    cursor.execute("SELECT * FROM medicines WHERE ID IS ? ", (medicine_id,))
    rows = cursor.fetchall() 
    if not rows:
        print ("Medicine ID is not found")
    else:
        
        medicine_name = rows[0][1]
        expiry_date = rows[0] [4]
        print(f"Medicine ID {medicine_id} is {medicine_name}.")
        cont = input("Do you want to update the name? (Y/N)")
        if cont == "Y":
            new_name = input('Enter the updated product name:')
            cursor.execute("UPDATE medicines SET name = ? WHERE ID = ?", (new_name, medicine_id))
            connect.commit() 

            #retrieve and display new quantity
            cursor.execute("SELECT * FROM medicines WHERE ID IS ? ", (medicine_id,))
            updated_rows = cursor.fetchall()
            medicine_name = updated_rows [0][1]
            expiry_date = updated_rows [0][4]
            print("Update successful!")
            print(f"The new name of Medicine ID: {medicine_id} is {medicine_name}, its expiry date is {expiry_date} ")
        else: 
           print("closing connection now")
        connect.close()
update_medicine_name() 