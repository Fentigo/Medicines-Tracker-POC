## 28/07/2023 = The below code should create a database schema and create a table to store medicine details
#database design
import sqlite3
print(sqlite3.sqlite_version)

#Creates the database
connect = sqlite3.connect('inventory db')

#Create a cursor to execute SQL commands
cursor = connect.cursor()

#Defining the medicine table. Create Table command

cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        batch_number TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        expiry_date DATE NOT NULL
    )
''')
connect.commit()# Commit the changes 
# sample data 

cursor.execute(
    ''' INSERT INTO medicines (name, batch_number, quantity, expiry_date)
    Values
    ('Paracetemol', 'BATCH123', 100, '2023-12-31'),
    ('Ibuprofen', 'BATCH456', 40, '2024-04-31'),
    ('Aspirin', 'BATCH789', 30, '2023-10-31')
    '''
)
connect.commit()
#close the database cannection

def display_medicines():
    # this code should execute the SQL Query
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()

    print("Medicine ID | Name    | Batch Number | Quantity | Expiry Date")
    print ("--------------------------------------------")
    for row in rows: 
        print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  |{row[3]:8}  | {row[4]}")

display_medicines()
connect.close()

