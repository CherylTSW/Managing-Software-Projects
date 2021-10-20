import mysql.connector

def ExecuteSQLFile(filename):
    # Connect to database
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "InventoryDB"
    )

    # Open file to read, then split the content with ';' as delimiter to form mSQL code that can be executed
    file = open(filename, 'r')
    sqlCode = file.read().split(';')
    file.close()

    # Execute the code
    myCursor = mydb.cursor()
    for code in sqlCode:
        myCursor.execute(code)

    # Declare 'result', iterate through the myCursor to store the tables present in database into 'result'
    result = ""
    myCursor.execute("SHOW TABLES")
    for x in myCursor:
        result += str(x)

    mydb.close()

    # (For testing purpose) to check if table is created successfully, result != ""
    return result

def CreateInventoryDB():
    # Create the database InventoryDB if it does not exist
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )
    mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS InventoryDB")

def AddInventory(itemName: str, itemPrice: float, itemQuantity: int):
    # Create the INSERT code to be executed
    sqlInsert = f"INSERT INTO Items (itemName, itemPrice, itemQuantity) VALUES (%s, %s, %s)"
    data = (itemName, itemPrice, itemQuantity)

    # Connect to database and execute the command
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "InventoryDB"
    )
    myCursor = mydb.cursor()
    myCursor.execute(sqlInsert, data)
    mydb.commit()

    # (For testing purpose) to check if INSERT is successful by ensuring row affected == 1
    return myCursor.rowcount

def GetInventory():
    query = "SELECT itemID, itemName, itemPrice, itemQuantity FROM Items"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "InventoryDB"
    )
    result = mydb.cursor().execute(query).fetchall()
    return result