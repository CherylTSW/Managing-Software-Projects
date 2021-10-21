from lib import authentication as auth
from lib import database as db

db_host = "localhost"
db_user = "root"
db_pwd = ""
auth_db = "Authentication"

auth_db_conn = db.create_db_connection(db_host , db_user, db_pwd, auth_db)

# Add an account 
auth.add_account(auth_db_conn, "placeholder", "123", "pol", "tato", 1)

# Delete an account with userID
auth.delete_account(auth_db_conn, auth.get_userID(auth_db_conn, "placeholder"))