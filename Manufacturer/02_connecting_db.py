import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", database="SPRINT1", user="root", password="")

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server Version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)      

except Error:
    print("Error while connecting to MySQL", Error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")