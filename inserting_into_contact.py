import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='SPRINT1',
                                         user='root',
                                         password='')

    mySql_insert_query = """INSERT INTO CONTACTMODULE (OrderID, OrderDate, ManufacturerID, ProductID, Quantity, TotalPrice) 
                           VALUES 
                           (20, '2021-10-14', 345, 300, 1000, 765.50) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    
    data = cursor.fetchall()
    print(data)
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Contact Module table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")