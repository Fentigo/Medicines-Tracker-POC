import sqlite3
connect = sqlite3.connect('notification_data')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notification_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        User_ID TEXT NOT NULL,
        Notification_Type TEXT NOT NULL,
        Timestamp datetime NOT NULL,
        Message TEXT NOT NULL
    )
''')

def low_quantity_alert()
    quantity_threshold = 22
    cursor.execute("SELECT * FROM medicines WHERE quantity < ?", (quantity_threshold,))
    low_quantity_medicines = cursor.fetchall()
    
    if not low_quantity_medicines:
        connect.close()
    else:

def expiry_alert()
    
