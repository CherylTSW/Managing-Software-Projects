from lib import database

# Function to add account to database
def add_account(conn, username: str, pwd: str, firstName: str, lastName: str, roleID: int):
    # Add user into users table
    userQuery = f"""INSERT INTO Users (username, firstName, lastName, roleID) VALUES 
    ('{username}', '{firstName}', '{lastName}', {roleID});"""
    exec1 = database.execute_query(conn, userQuery)

    # Get latest user ID
    getUserIDQuery = "SELECT userID FROM Users ORDER BY userID DESC LIMIT 1"
    result = database.read_query(conn, getUserIDQuery)
    userID = result[0][0]

    # Add password for that userID into passwords table
    pwdQuery = f"""INSERT INTO Passwords (password, userID)
    VALUES ('{pwd}', {userID});"""
    exec2 = database.execute_query(conn, pwdQuery)

    logQuery = f"""INSERT INTO Logs (eventTypeID, userID)
    VALUES (1, {userID})"""
    exec3 = database.execute_query(conn, logQuery)

    return exec1 and exec2 and exec3


# Function to delete account from database
def delete_account(conn, userID:int):
    # Delete the entry from passwords, users and logs tables
    deletePwdQuery = f"""DELETE FROM Passwords WHERE userID={userID};"""
    deleteUserQuery = f"""DELETE FROM Users WHERE userID={userID};"""
    deleteLogQuery = f"""DELETE FROM Logs WHERE userID={userID};"""

    exec1 = database.execute_query(conn, deleteLogQuery)
    exec2 = database.execute_query(conn, deletePwdQuery)
    exec3 = database.execute_query(conn, deleteUserQuery)
    
    return exec1 and exec2 and exec3
    
# Function to get userID from username
def get_userID(conn, username:str):
    findQuery = f"""SELECT userID FROM Users WHERE username='{username}'"""
    result = database.read_query(conn, findQuery)
    userID = result[0][0]

    return userID

# Function to edit password of a user
def password_change(conn, userID:int, password:str):
    # Change password in passwords table
    pwdChangeQuery = f"""UPDATE Passwords SET password='{password}' WHERE userID={userID}"""
    # Insert password change log
    logQuery = f"""INSERT INTO Logs (eventTypeID, userID)
    VALUES (2, {userID})"""
    
    exec1 = database.execute_query(conn, pwdChangeQuery)
    exec2 = database.execute_query(conn, logQuery)

    return exec1 and exec2