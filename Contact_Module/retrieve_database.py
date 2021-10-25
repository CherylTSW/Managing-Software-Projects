import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sprint1',
                                         user='root')

    sql_select_Query = "select * from contactmodule"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("OrderID = ", row[0], )
        print("OrderDate = ", row[1])
        print("ManufacturerID  = ", row[2])
        print("ProductID  = ", row[3])
        print("Quantity  = ", row[4])
        print("TotalPrice  = ", row[5], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")