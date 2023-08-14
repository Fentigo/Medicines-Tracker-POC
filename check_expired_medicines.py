import sqlite3
import datetime
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def check_expired_medicines():
    print ("Checking for expired medicines..")
    current_date = datetime.today().date()

    # calculate the date range for expiring medicines 
    end_date = current_date + datetime.timedelta(days = 7)

    cursor.execute('SELECT * FROM medicines WHERE expiry_date < ?', (current_date,))
    expired_medcines = cursor.fetchall()

    if not expired_medcines:
        print("No Expired medicines found.")
    else: 
        print("Expired Medicines:")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in expired_medicines:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")

