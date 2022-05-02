import sqlite3 # import sqlite3 library

conn = sqlite3.connect("companyDirectory.db") # Create and connect the database
cursor = conn.cursor() # Cursor method iterate the database

cursor.execute(""" 

CREATE TABLE "employees" (
	"EmployeeID" INTEGER NOT NULL UNIQUE,
	"Title"	TEXT NOT NULL,
	"FirstName" TEXT NOT NULL,
	"LastName" TEXT NOT NULL,
	"Department" TEXT NOT NULL,
	"JobTitle" TEXT NOT NULL,
	"Address" TEXT NOT NULL,
	"Email" VARCHAR NOT NULL UNIQUE,
	"DateOfBirth" DATE NOT NULL,
	"NiNumber" VARCHAR NOT NULL UNIQUE,
	PRIMARY KEY("EmployeeID" AUTOINCREMENT)
)"""
)