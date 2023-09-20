from datetime import datetime, timedelta
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def view_expiring_medicine():

    print("Viewing medicines expiring soon")
    current_date = datetime.today().date() #gets current date
    #placeholder, add a date range, and show the immediate expiring 
    end_date = current_date + timedelta(days=30)
    cursor.execute( "SELECT * FROM medicines WHERE expiry_date BETWEEN ? and ?", (current_date, end_date))
    #fetch all rows returned by the above query.
    rows = cursor.fetchall() 
    # displaying the fetched data 

    if not rows: 
        print ("No Medicines due to expire ")
    else:
         print("Medicine ID | Name    | Batch Number | Quantity | Expiry Date")
         print ("--------------------------------------------")
    for row in rows: 
        print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  |{row[3]:8}  | {row[4]}")

    connect.close() 
view_expiring_medicine()