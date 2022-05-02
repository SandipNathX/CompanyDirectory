import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

import time

def searchEmployee():
    print("\n\x1b[94mWhich field would you like to search for?\x1b[0m\n" + "EmployeeID\nTitle\nFirstName\nLastName\nDepartment\nJobTitle\nAddress\nEmail\nDateOfBirth\nNiNumber")

    searchField = str(input("\n\x1b[94mPlease enter one of the field names from the list above: \x1b[0m")).title()

    # Enter the value of the field you are searching
    searchValue = str(input(f"\n\x1b[94mEnter the value for the\x1b[0m {searchField} \x1b[94mfield you want to search: "))
    print(f"\n\x1b[92mThe search value you have entered is\x1b[0m {searchValue} ")

    # Add single quotes around the new field value entered by the user
    searchValue = "'" + searchValue + "'"

    cursor.execute("SELECT COUNT(*) FROM employees WHERE " + searchField + "=" + searchValue)
    total = (cursor.fetchone())
    total = str(total)[1:-1]
    new_total = total.replace(',', '')
    # search database
    cursor.execute("SELECT * FROM employees WHERE " + searchField + "=" + searchValue)
    conn.commit()
    time.sleep(3)

    row = cursor.fetchall()
    # Convert/cast(row) to a string data type
    strRow = str(row)
    if searchValue in strRow:
        print(f"\n{new_total} \x1b[92msearch results found for\x1b[0m {searchValue}\x1b[92m:\x1b[0m")
        for record in row:
            print('\n\x1b[107m','\x1b[30m',record, '\x1b[0m')
    else:
        print(f"The field {searchField} does not contains a {searchValue} in the database!")






