from lib import database

# Function to add account to database
def add_account(conn, username: str, pwd: str, firstName: str, lastName: str, roleID: int):
    # Add user into users table
    userQuery = f"""INSERT INTO Users (username, firstName, lastName, roleID) VALUES 
    ('{username}', '{firstName}', '{lastName}', {roleID});"""
    database.execute_query(conn, userQuery)

    # Get latest user ID
    getUserIDQuery = "SELECT userID FROM Users ORDER BY userID DESC LIMIT 1"
    result = database.read_query(conn, getUserIDQuery)
    userID = result[0][0]

    # Add password for that userID into passwords table
    pwdQuery = f"""INSERT INTO Passwords (password, userID)
    VALUES ('{pwd}', {userID});"""
    database.execute_query(conn, pwdQuery)

