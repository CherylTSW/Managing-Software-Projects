import unittest

from lib import authentication as auth
from lib import database as db

test_config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "Test"
        }

# Create test tables in database
create_tables_queries = ["""
CREATE TABLE Permissions (
    permissionID INT(5) NOT NULL PRIMARY KEY,
    permissionName VARCHAR(30) NOT NULL,
    permissionDescription VARCHAR(200)
);
""", """
CREATE TABLE Roles (
    roleID INT(3) NOT NULL PRIMARY KEY,
    roleName VARCHAR(30) NOT NULL
);
""", """
CREATE TABLE RolePermissions (
    roleID INT(3) NOT NULL,
    permissionID INT(5) NOT NULL,
    PRIMARY KEY (roleID, permissionID),
    FOREIGN KEY (roleID) REFERENCES Roles(roleID),
    FOREIGN KEY (permissionID) REFERENCES Permissions(permissionID)
);
""", """
CREATE TABLE Users (
    userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    roleID INT(3) NOT NULL,
    FOREIGN KEY (roleID) REFERENCES Roles(roleID)
);
""", """
CREATE TABLE Passwords (
    passwordID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    password VARCHAR(30) NOT NULL,
    userID INT(5),
    FOREIGN KEY (userID) REFERENCES Users(userID)
);
""", """
CREATE TABLE EventTypes (
    eventTypeID INT(5) NOT NULL PRIMARY KEY,
    eventName VARCHAR(30) NOT NULL,
    eventDescription VARCHAR(200)
);
""", """
CREATE TABLE Logs (
    logID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    loggedDateTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    eventTypeID INT(5) NOT NULL,
    userID INT(5),
    FOREIGN KEY (eventTypeID) REFERENCES EventTypes(eventTypeID),
    FOREIGN KEY (userID) REFERENCES Users(userID)
);
"""]

# Populate table with default data
insert_queries = ["""
INSERT INTO Permissions (permissionID, permissionName, permissionDescription)
VALUES (1, "Edit Account", "Permission to edit details of an account");
""", """
INSERT INTO Permissions (permissionID, permissionName, permissionDescription)
VALUES (2, "Add Account", "Permission to add an account");
""", """
INSERT INTO Permissions (permissionID, permissionName, permissionDescription)
VALUES (3, "Delete Account", "Permission to add an account");
""", """
INSERT INTO EventTypes (eventTypeID, eventName, eventDescription)
VALUES (1, "Create Account", "The user has created an account");
""", """
INSERT INTO EventTypes (eventTypeID, eventName, eventDescription)
VALUES (2, "Password Change", "The user has changed its password");
""", """
INSERT INTO Roles (roleID, roleName) VALUES (1, "Owner");
""", """
INSERT INTO Roles (roleID, roleName) VALUES (2, "Manager");
""", """
INSERT INTO Roles (roleID, roleName) VALUES (3, "Cashier");
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (1, 1);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (1, 2);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (1, 3);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (2, 1);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (2, 2);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (2, 3);
""", """
INSERT INTO RolePermissions(roleID, permissionID) VALUES (3, 1);
"""]

class TestAuthentication(unittest.TestCase):
    def test_add_account(self):
        """
        Test that whether account is added successfully
        """
        test_config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "Test"
        }
        
        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        for query in create_tables_queries:
            db.execute_query(conn, query)

        for query in insert_queries:
            db.execute_query(conn, query)

        self.assertTrue(auth.add_account(conn, "test", "test", "test", "test", 1))

    def test_delete_account(self):
        """
        Test that whether account is deleted successfully
        """
        test_config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "Test"
        }
        
        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        for query in create_tables_queries:
            db.execute_query(conn, query)

        for query in insert_queries:
            db.execute_query(conn, query)

        auth.add_account(conn, "test", "test", "test", "test", 1)

        self.assertTrue(auth.delete_account(conn, auth.get_userID(conn, "test")))

    def test_change_password(self):
        """
        Test that whether account password is changed successfully
        """  

        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        for query in create_tables_queries:
            db.execute_query(conn, query)

        for query in insert_queries:
            db.execute_query(conn, query)

        auth.add_account(conn, "test", "test", "test", "test", 1)

        self.assertTrue(auth.password_change(conn, auth.get_userID(conn, "test"), "new pwd"))

if __name__ == '__main__':
    unittest.main()