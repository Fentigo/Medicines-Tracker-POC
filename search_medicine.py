import sqlite3
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()
def search():
    print("Search for a medicine:")
    print("1. Search by Name")
    print("2. Search by Batch Number")

    search_choice = input("Enter your choice (1/2): ")

    if search_choice == '1':
        try: 
            search_term = input("Enter medicine name: ")
            cursor.execute("SELECT *  FROM medicines WHERE name LIKE ?", (search_term,))#less hardcoding, instead of = i've added LIKE
        except ValueError:
            print("Invalid input. Please enter valid details")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    if search_choice == '2':
        try: 
            search_term = input("Enter batch number:")
            search_batch = "BATCH"+ search_term
            cursor.execute("SELECT *  FROM medicines WHERE name LIKE ?", (search_batch,))
        except ValueError:
            print("Invalid input. Please enter valid details")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid Choice.")
        return
    
    rows = cursor.fetchall()
    if not rows:
        print("No matching medicines found.")
    else:
        print("Search Results:")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in rows:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")