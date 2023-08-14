import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()

def add_medicine():
    print(" Enter the following information")
    
    try: #error handling
        name = input('insert medicine name')
        batch_number_input = input ('insert batch number')
        batch_number = "BATCH" +  batch_number_input #ensures correct format
        quantity = int(input('Enter Quantity here'))
        expiry_date = input('Enter date here YYYY-MM-DD')
        cursor.execute ("INSERT INTO medicines (name, batch_number, quantity, expiry_date) VALUES (?, ?, ?, ?)", 
                    (name, batch_number, quantity, expiry_date))
        connect.commit()
        connect.close()
        print('Medicine has been added successfully!')
    except ValueError:
        print("Invalid input. Please enter valid details")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    

    
