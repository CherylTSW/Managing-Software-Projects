from tkinter.font import BOLD
import mysql.connector
from tkinter import *
from mysql.connector import Error

# Method to create the SPRINT1 database
def create_sprint1_db():
    # Establishing the connection
    conn = mysql.connector.connect(user='root', password='', host='localhost')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping database SPRINT1 if already exists.
    cursor.execute("DROP database IF EXISTS SPRINT1")

    # Preparing query to create a database
    sql = "CREATE database SPRINT1"

    # Creating a database
    cursor.execute(sql)

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    # Closing the connection
    conn.close()

# Method to connect to the SPRINT1 database
def connect_sprint1_db():
    try:
        connection = mysql.connector.connect(host="localhost", database="SPRINT1", user="root", password="")

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server Version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)      

    except Error:
        print("Error while connecting to MySQL", Error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Method to create the Manufacturer table
def create_manufacturer_table():
    try:
        connection = mysql.connector.connect(host='localhost', database='sprint1', user='root', password='')

        mySql_Create_Table_Query = """CREATE TABLE MANUFACTURER ( 
                                    ManufacturerID INT(10) NOT NULL,
                                    ManufacturerFirstName nvarchar(25) NULL,
                                    ManufacturerLastName nvarchar(25) NULL,
                                    ManufacturerItem nvarchar(30) NULL,
                                    ManufacturerStreetAddress nvarchar(50) NULL,
                                    ManufacturerPhoneNumber INT(12) NULL,
                                    PRIMARY KEY (ManufacturerID)) """

        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("Manufacturer Table created successfully ")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Method to add the manufacturer details
def add_manufacturer(ManufacturerID: int, ManufacturerFirstName: str, ManufacturerLastName: str, ManufacturerItem: str, ManufacturerStreetAddress: str, ManufacturerPhoneNumber: str):
    try:
        connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

        mySql_insert_query = """INSERT INTO MANUFACTURER (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber) 
                            VALUES 
                            (%s, %s, %s, %s, %s, %s) """

        data = (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Manufacturer table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Manufacturer table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Method to remove the manufacturer details
def remove_manufacturer(ManufacturerID: int):
    try:
        connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

        cursor = connection.cursor()
        print("Manufacturer table before deleting a row")
        sql_select_query = """select * from MANUFACTURER where ManufacturerID = """ + str(ManufacturerID)
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)

        # Delete a record
        sql_Delete_query = """Delete from MANUFACTURER where ManufacturerID = """ + str(ManufacturerID)
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)

        # Verify using select query (optional)
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        if len(records) == 0:
            print("Record Deleted successfully ")

    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Method to display the items retrieved from database in a table form
#def display_manufacturer(window: Tk, startColumn: int, startRow: int, items):