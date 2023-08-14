import sqlite3
import datetime
connect = sqlite3.connect('inventory db')
cursor = connect.cursor()

import csv # download as CSV function

def generate_expiry_report():
    print("Generating report....")
    current_date = datetime.today().date()

    cursor.execute("SELECT * FROM medicines WHERE expiry_date < ?", (current_date,))
    expired_medicines = cursor.fetchall()
    if not expired_medicines:
        print("No expired medicines found.")
    else: 
        print("Expired Medicines Report:")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in expired_medicines:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")
        download_option = input("Do you want to download the report?(Y/N)")
        if download_option == 'N':
            connect.close()
        else: 
            with open("expired_medicines_report.csv", "w", newline = "")as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Medicine ID", "Name", "Batch Number", "Quantity", "Expiry Date"])
                for row in expired_medicines:
                    csv_writer.writerow(row)
                    print("Expired Medicines report saved as expired_medicines_report.csv")
        

    connect.close()

def generate_low_quantity_report():
    print("Generating report....")
    quantity_threshold = 22

    cursor.execute("SELECT * FROM medicines WHERE quantity < ?", (quantity_threshold,))
    low_quantity_medicines = cursor.fetchall()

    if not low_quantity_medicines:
        print("No low quantity medicines found.")
    else: 
        print("Medicine Quantity Report:")
        print("Medicine ID | Name | Batch Number | Quantity | Expiry Date")
        print("--------------------------------------------")
        for row in low_quantity_medicines:
            print(f"{row[0]:11}  | {row[1]:11}  | {row[2]:12}  | {row[3]:8}  | {row[4]}")
            download_option = input("Do you want to download the report?(Y/N)")
        if download_option == 'N':
            connect.close()
        else: 
            with open("low_quantity_report.csv", "w", newline = "")as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Medicine ID", "Name", "Batch Number", "Quantity", "Expiry Date"])
                for row in low_quantity_medicines:
                    csv_writer.writerow(row)
                    print("Expired Medicines report saved as low_quantity_report.csv")

    connect.close()


