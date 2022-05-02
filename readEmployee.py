import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

def readEmployee():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchall()
    for record in row:
        print('\n\x1b[107m','\x1b[30m',record, '\x1b[0m')