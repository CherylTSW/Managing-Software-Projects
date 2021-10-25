from lib import database

# Function to add account to database
def add_account(conn, username: str, pwd: str, firstName: str, lastName: str, role: int):
    # Add user into users table
    userQuery = f"""INSERT INTO Users (username, firstName, lastName, role, password) VALUES 
    ('{username}', '{firstName}', '{lastName}', {role}, '{pwd}');"""
    exec1 = database.execute_query(conn, userQuery)

    return exec1


# Function to delete account from database
def delete_account(conn, userID:int):
    # Delete the entry from users table
    deleteUserQuery = f"""DELETE FROM Users WHERE userID={userID};"""

    exec1 = database.execute_query(conn, deleteUserQuery)
    
    return exec1
    
# Function to get userID from username
def get_userID(conn, username:str):
    findQuery = f"""SELECT userID FROM Users WHERE username='{username}'"""
    result = database.read_query(conn, findQuery)
    userID = result[0][0]

    return userID

# Function to edit password of a user
def password_change(conn, userID:int, password:str):
    # Change password in users table
    pwdChangeQuery = f"""UPDATE Users SET password='{password}' WHERE userID={userID}"""
    
    exec1 = database.execute_query(conn, pwdChangeQuery)

    return exec1 