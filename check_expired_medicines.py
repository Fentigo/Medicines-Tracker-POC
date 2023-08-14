import sqlite3
import datetime
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def check_expired_medicines():
    print ("Checking for expired medicines..")
    current_date = datetime.datetime.today().date()
    print(current_date)

    # calculate the date range for expiring medicines 
    end_date = current_date + datetime.timedelta(days = 7) # this is for the medicines that are going to expire within the next 7 days

    cursor.execute('SELECT * FROM medicines WHERE expiry_date BETWEEN ? AND ?', (current_date, end_date))
    expiring_medicines = cursor.fetchall()
    print("Current Date:", current_date)
    print("End Date: ", end_date) #Debugging 
    

    if not expiring_medicines:
        print("No Expired medicines found within the next 7 days.")
    else: 
        print("Here are the medicines that are expiring soon: ")
        print("Expiring Medicines:")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in expiring_medicines:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")

    cursor.execute('SELECT * FROM medicines WHERE expiry_date < ?', (current_date,))
    expired_medicines = cursor.fetchall()
    print("Here are the medicines that have expired: ")
    print("Expired Medicines:")
    print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
    print("--------------------------------------------")
    for row in expired_medicines:
        print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")
        
 
    connect.close()


check_expired_medicines()

