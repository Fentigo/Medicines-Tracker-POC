import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def view_medicines():
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()

    print("Medicine ID | Name    | Batch Number | Quantity | Expiry Date")
    print ("--------------------------------------------")
    for row in rows: 
        print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  |{row[3]:8}  | {row[4]}")
    connect.commit()
    connect.close

view_medicines()