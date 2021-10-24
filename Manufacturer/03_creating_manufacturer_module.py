import mysql.connector

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