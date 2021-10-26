import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter.font import BOLD

# This is to create the database SPRINT1
def create_database():
    connection = mysql.connector.connect(
    host="localhost",
    database="SPRINT1",
    user="root",
    password="")
    connection.cursor().execute("CREATE DATABASE IF NOT EXISTS SPRINT1")
    connection.close()

# This is to connect to the database SPRINT1
def connect_contact_db():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        database="SPRINT1",
        user="root",
        password="")
        return connection

    except Error:
        return False

# This is to create a new table named CONTACTMODULE in the database
def create_contact_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='sprint1',
                                            user='root',
                                            password='')

        mySql_Create_Table_Query = """CREATE TABLE CONTACTMODULE ( 
                                    OrderID INT(10) NOT NULL,
                                    OrderDate VARCHAR(10),
                                    ManufacturerID INT(10),
                                    ProductID INT(10),
                                    Quantity INT(10),
                                    TotalPrice FLOAT(10,2),
                                    PRIMARY KEY (OrderID)) """
        
        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        
    except mysql.connector.Error:
        return False

# This is to insert a new row of information in the CONTACTMODULE with the user input        
def insert_contact(orderId: int, orderDate: str, manufacturerId: int, productId: int, quantity: int, totalPrice: float):
    try:
        connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

        mySql_insert_query = f"INSERT INTO CONTACTMODULE (orderId, orderDate, manufacturerId, productId, quantity, totalPrice) VALUES (%s, %s, %s, %s, %s, %s) "

        information = (orderId, orderDate, manufacturerId, productId, quantity, totalPrice)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, information)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Manufacturer table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Manufacturer table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# This is to delete the row of information based on the user input
def delete_contact(orderId: int):
    try:
        connection = connect_contact_db()
        myCursor = connection.cursor()

        # Delete a record
        deleting = f"Delete from CONTACTMODULE where orderId = " + str(orderId)
        myCursor.execute(deleting)
        connection.commit()

        # This is to count the number of row affected
        result = myCursor.rowcount
        connection.close()
        
        # If row affected > 0, the insertion is successful. Return True on success, else return false
        if(result > 0):
            return True
        else:
            return False

    except Error:
        print("Error while connecting to MySQL", Error)

