DROP DATABASE IF EXISTS Authentication;
CREATE DATABASE Authentication;
USE Authentication;

CREATE TABLE Permissions (
	permissionID INT(5) NOT NULL PRIMARY KEY,
    permissionName VARCHAR(30) NOT NULL,
    permissionDescription VARCHAR(200)
);

CREATE TABLE Roles (
	roleID INT(3) NOT NULL PRIMARY KEY,
    roleName VARCHAR(30) NOT NULL
);

CREATE TABLE RolePermissions (
	roleID INT(3) NOT NULL,
    permissionID INT(5) NOT NULL,
	PRIMARY KEY (roleID, permissionID),
    FOREIGN KEY (roleID) REFERENCES Roles(roleID),
    FOREIGN KEY (permissionID) REFERENCES Permissions(permissionID)
);

CREATE TABLE Users (
	userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    roleID INT(3) NOT NULL,
    FOREIGN KEY (roleID) REFERENCES Roles(roleID)
);

CREATE TABLE Passwords (
	passwordID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    password VARCHAR(30) NOT NULL,
    userID INT(5),
    FOREIGN KEY (userID) REFERENCES Users(userID)
);

CREATE TABLE EventTypes (
	eventTypeID INT(5) NOT NULL PRIMARY KEY,
    eventName VARCHAR(30) NOT NULL,
    eventDescription VARCHAR(200)
);

CREATE TABLE Logs (
	logID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    loggedDateTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    eventTypeID INT(5) NOT NULL,
    userID INT(5),
    FOREIGN KEY (eventTypeID) REFERENCES EventTypes(eventTypeID),
    FOREIGN KEY (userID) REFERENCES Users(userID)
);
