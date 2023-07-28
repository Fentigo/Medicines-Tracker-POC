#Database Connection
import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()

#database operations 
#inserting data into medicines table
cursor.execute ("INSERT INTO medicines (name, batch_number, quantity, expiry_date) VALUES (?, ?, ?, ?)", ('Limitless', 'BATCH790', 100, '2023-12-31'))
connect.commit()
connect.close()
