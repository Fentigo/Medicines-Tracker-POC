import sqlite3
connect = sqlite3.connect(
    'inventorydb'
)

cursor = connect.cursor()

def add_medicine():
    print(" Enter the following information")
    name = input('insert medicine name')
    batch_number = input ('insert batch number')
    quantity = int(input('Enter Quantity here'))
    expiry_date = input('Enter date here YYYY-MM-DD')
    cursor.execute ("INSERT INTO medicines (name, batch_number, quantity, expiry_date) VALUES (?, ?, ?, ?)", 
                    (name, batch_number, quantity, expiry_date))
    connect.commit()
    connect.close()
    print('Medicine has been added successfully!')