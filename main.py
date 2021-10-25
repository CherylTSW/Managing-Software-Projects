from lib import authentication as auth
from lib import database as db

auth_config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "Authentication"
        }

auth_db_conn = db.create_db_connection(auth_config)

# Add an account 
auth.add_account(auth_db_conn, "placeholder", "123", "pol", "tato", 1)

# Login
print(auth.login(auth_db_conn, "placeholder", "123"))

# Change password
auth.password_change(auth_db_conn, auth.get_userID(auth_db_conn, "placeholder"), "456")

# Delete an account with userID
auth.delete_account(auth_db_conn, auth.get_userID(auth_db_conn, "placeholder"))