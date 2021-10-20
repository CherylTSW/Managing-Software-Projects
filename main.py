from lib import database as db

db_host = "localhost"
db_user = "root"
db_pwd = ""
auth_db = "Authentication"

auth_db_conn = db.create_db_connection(db_host , db_user, db_pwd, auth_db)
