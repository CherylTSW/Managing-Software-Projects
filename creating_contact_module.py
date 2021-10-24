import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sprint1',
                                         user='root',
                                         password='')

    mySql_Create_Table_Query = """CREATE TABLE CONTACTMODULE ( 
                                OrderID INT(10) NOT NULL,
                                OrderDate DATE,
                                ManufacturerID INT(10),
                                ProductID INT(10),
                                Quantity INT(10),
                                TotalPrice FLOAT(10,2),
                                PRIMARY KEY (OrderID)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Contact Module Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")