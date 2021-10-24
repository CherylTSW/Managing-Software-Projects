import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='', host='localhost')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping database SPRINT1 if already exists.
cursor.execute("DROP database IF EXISTS SPRINT1")

#Preparing query to create a database
sql = "CREATE database SPRINT1"

#Creating a database
cursor.execute(sql)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the connection
conn.close()