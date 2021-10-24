import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

    mySql_insert_query = """INSERT INTO MANUFACTURER (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber) 
                           VALUES 
                           (%s, %s, %s, %s, %s, %s) """

    records_to_insert = [(1234567, 'Michael', 'Jackson', 'Antibiotics', '327, Jalan Rock', 987654321),
                         (1234568, 'Justin', 'Bieber', 'Panadol', '328, Jalan Rock', 987654322),
                         (1234569, 'Harry', 'Styles', 'Surgical Mask', '329, Jalan Rock', 987654323)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Manufacturer table")

except mysql.connector.Error as error:
    print("Failed to insert record into Manufacturer table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")