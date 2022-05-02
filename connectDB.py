import sqlite3 # import sqlite3 library

conn = sqlite3.connect("employees.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database
