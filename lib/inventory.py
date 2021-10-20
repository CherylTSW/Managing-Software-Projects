import mysql.connector
from mysql.connector import Error

def create_inventory_db():
    # Create the database InventoryDB if it does not exist
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
    )
    mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS InventoryDB")
    mydb.close()

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
        

def get_inventory():
    query = "SELECT itemID, itemName, itemPrice, itemQuantity FROM Items"
    mydb = connect_inventory_db()
    result = mydb.cursor().execute(query).fetchall()
    return result