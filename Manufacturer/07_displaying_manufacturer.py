import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', database='SPRINT1', user='root', password='')

    sql_select_Query = "select * from MANUFACTURER"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Manufacturer ID = ", row[0], )
        print("Manufacturer First Name = ", row[1])
        print("Manufacturer Last Name = ", row[2])
        print("Manufacturer Selling Item  = ", row[3])
        print("Manufacturer Street Address  = ", row[4])
        print("Manufacturer Phone Number  = ", row[5], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")