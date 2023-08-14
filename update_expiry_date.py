#Update expiry date 
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def update_expiry_date():
    medicine_id = input(' Type Medicine ID here: ')
    cursor.execute("SELECT * FROM medicines WHERE id is ?", (medicine_id,))
    rows = cursor.fetchall()
    if not rows:
        print ("Please enter valid Medicine ID. ")
    else: 
        medicine_name = rows[0][1]
        batch_id = rows[0][2]
        expiry_date = rows[0][4]
        print(f"Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Batch ID: {batch_id}, Current Expiry Date is : {expiry_date} ") 
        cont = input("Do you want to change the expiry date? (Y/N)")
        if cont == "Y":
            new_date = input("Enter new expiry date here (YYYY/MM/DD):")
            cursor.execute("UPDATE medicines SET expiry_date = ? WHERE id =?", (new_date, medicine_id))
            print("Update successful")
            cursor.execute("SELECT * FROM medicines WHERE id = ?", (medicine_id,))
            connect.commit()
            updated_rows = cursor.fetchall()
            updated_expiry_date = updated_rows[0][4]
            print(f"Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Batch ID: {batch_id}, Current Expiry Date is : {updated_expiry_date} ") 
    connect.close()

update_expiry_date()