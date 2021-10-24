import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

    mySql_insert_query = """INSERT INTO MANUFACTURER (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber) 
                           VALUES 
                           (1234566, 'Selena', 'Gomez', 'Toilet Paper', '326, Jalan Rock', 987654320) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Manufacturer table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Manufacturer table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")