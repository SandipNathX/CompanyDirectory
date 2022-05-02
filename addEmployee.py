import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

import time

# Create subroutines to add emplyee
def addEmployee():
    # Create an empty list
    employees = []
    # Employee ID field is auto increament 
  
    employeeID = cursor.lastrowid
    
    # Capture values from the user
    print("\n\x1b[94mAdd Employee - Enter employee information below:\x1b[0m\n")
    title = input("Title: ")
    firstName = input("First name: ")
    lastName = input("Last name: ")
    department = input("Department: ")
    jobTitle = input("Job Title: ")
    address = input("Address: ")
    email = input("Email: ")
    dateOfBirth = input("Date of Birth (dd-mm-yyyy): ")
    niNumber = input("NI Number: ")

    # Append the captured values from the user 
    employees.append(employeeID)
    employees.append(title)
    employees.append(firstName)
    employees.append(lastName)
    employees.append(department)
    employees.append(jobTitle)
    employees.append(address)
    employees.append(email)
    employees.append(dateOfBirth)
    employees.append(niNumber)

    try:
        # Cursor.execute('INSERT INTO employees, EmployeeID, Title, FirstName, LastName, Department, JobTitle, Address, Email, DateOfBirth, NiNumber VALUES(employeeID, title, firstName, lastName, department, jobTitle, address, email, dateOfBirth, niNumber)',employees)
        cursor.execute('INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', employees)
        conn.commit()
        print("\n\x1b[92mEmployee details have been successfully added.\n")
        time.sleep(3)
        cursor.execute('SELECT * FROM employees')
        row = cursor.fetchall()
        for record in row:
            print('\n\x1b[107m','\x1b[30m',record, '\x1b[0m')
    except:
        print(f"\n\x1b[31mEmployee details for {title} {firstName} {lastName} have not been added.\n\x1b[0m")
    finally:
        conn.close()