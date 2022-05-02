import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

import time

def deleteEmployee():
    employee_id = int(input("\n\x1b[94mEnter the Employee ID you would like to delete: \x1b[0m"))

    try:
        cursor.execute(f"DELETE FROM employees WHERE EmployeeID = {employee_id}")
        conn.commit()
        print(f"\n\x1b[31mEmployee ID\x1b[0m {employee_id} \x1b[31mhas been deleted.\n\x1b[0m")
        time.sleep(3)
        cursor.execute('SELECT * FROM employees')
        row = cursor.fetchall()
        for record in row:
            print('\n\x1b[107m','\x1b[30m',record, '\x1b[0m')
    except:
           print(f"Employee ID: {employee_id} was not updated.")
    
    finally:
           conn.close()