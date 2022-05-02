import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

import time

def updateEmployee():
    # Enter the id that needs to be updated
    employee_id = int(input("\n\x1b[94mEnter the ID of the employee you would like to update: \x1b[0m"))

    print("\n\x1b[94mWhich field would you like to update? \x1b[0m\n" + 
    "Title\nFirstName\nLastName\nDepartment\nJobTitle\nAddress\nEmail\nDateOfBirth\nNiNumber")

    fieldName = str(input("\n\x1b[94mPlease enter one of the field names from the list above: \x1b[0m"))

    newFieldValue = input("\n\x1b[94mEnter the new value of the field: \x1b[0m")
     
    print('\n\x1b[92m' + 'You have updated the field' + '\x1b[0m ' + fieldName + ' \x1b[92mwith the new value' + "\x1b[0m " + newFieldValue + "\x1b[92m.\x1b[0m")
    newFieldValue = "'" + newFieldValue + "'"
    try:
        cursor.execute(f"UPDATE employees SET {fieldName} = {newFieldValue} WHERE EmployeeID = {employee_id} ")
        conn.commit()
        print(f"\x1b[92mEmployeeID:\x1b[0m {employee_id} \x1b[92mhas been updated.\n\x1b[0m")
        time.sleep(3)
        cursor.execute('SELECT * FROM employees')
        row = cursor.fetchall()
        for record in row:
            print('\n\x1b[107m','\x1b[30m',record, '\x1b[0m')
    except:
        print(f"\n\x1b[31mEmployee ID: {employee_id} was not updated.\n\x1b[0m")
    finally:
        conn.close()
