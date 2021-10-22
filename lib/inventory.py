import mysql.connector
from mysql.connector import Error

# Method to create the database InventoryDB
def create_inventory_db():
    # Create the database InventoryDB if it does not exist
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
    )
    mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS InventoryDB")
    mydb.close()

# Method to connect to database InventoryDB. 
# Return the connection object if successful, else return False
def connect_inventory_db():
    # Create connection to database
    try:
        # If connection created successfully, return the connection object
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "InventoryDB"
        )
        return mydb
    except Error:
        # If error occurs, return False
        return False

# Method to execute SQL code from file
def execute_sql_file(filename):
    mydb = connect_inventory_db()

    # Open file to read, then split the content with ';' as delimiter to form mSQL code that can be executed
    file = open(filename, 'r')
    sqlCode = file.read().split(';')
    file.close()

    # Execute the code
    myCursor = mydb.cursor()
    for code in sqlCode:
        myCursor.execute(code)

    mydb.close()

# Method to add an inventory item using the itemName, itemPrice, and itemQuantity received as parameters.
# Return True if successful, else return False
def add_inventory(itemName: str, itemPrice: float, itemQuantity: int):
    # Create the INSERT code to be executed
    sqlInsert = f"INSERT INTO Items (itemName, itemPrice, itemQuantity) VALUES (%s, %s, %s)"
    data = (itemName, itemPrice, itemQuantity)

    # Connect to database and execute the command
    mydb = connect_inventory_db()
    myCursor = mydb.cursor()
    myCursor.execute(sqlInsert, data)
    mydb.commit()

    # Obtain the count of row affected
    result = myCursor.rowcount
    mydb.close()
    
    # If row affected > 0, the insertion is successful. Return True on success, else return false
    if(result > 0):
        return True
    else:
        return False

# Method to get all inventory item from the database
# Return the records if successful, else return False
def get_all_inventory():
    try:
        # try selecting all records from table Items, and return the result(the records)
        mydb = connect_inventory_db()
        query = "SELECT * FROM Items"
        myCursor = mydb.cursor()
        myCursor.execute(query)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to get inventory item by ID of the item
# Return the records if successful, else return False
def get_inventory_by_id(id: int):
    try:
        # try selecting all records from table Items with itemID matching the parameter 'id', and return the result(the records)
        mydb = connect_inventory_db()
        query = f"SELECT * FROM Items WHERE itemID = %s"
        itemID = (id,)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to get inventory item by name of the item
# Return the records if successful, else return False
def get_inventory_by_name(name: str):
    try:
        # try selecting all records from table Items with itemName matching the parameter 'name', and return the result(the records)
        mydb = connect_inventory_db()
        query = f"SELECT * FROM Items WHERE itemName = %s"
        itemID = (name,)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to edit the information of an inventory item with itemID = id(parameter) by replacing its itemName, itemPrice and itemQuantity with the parameter newName, newPrice and newQuantity.
# Return True if item is edited successfully, else return False
def edit_inventory(newName: str, newPrice: float, newQuantity: int, id: int):
    try:
        # try updating the table Items by setting itemName = newName, itemPrice = newPrice, itemQuantity = newQuantity. Return True
        mydb = connect_inventory_db()
        query = f"Update Items SET itemName = %s, itemPrice = %s, itemQuantity = %s WHERE itemID = %s"
        itemID = (newName, newPrice, newQuantity, id)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        mydb.commit()
        mydb.close()
        return True
    except Error:
        # return False if error occurs
        return False

