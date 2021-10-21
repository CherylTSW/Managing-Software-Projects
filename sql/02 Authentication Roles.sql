INSERT INTO Roles (roleID, roleName)
VALUES (1, "Owner");

INSERT INTO Roles (roleID, roleName)
VALUES (2, "Manager");

INSERT INTO Roles (roleID, roleName)
VALUES (3, "Cashier");

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (1, 1);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (1, 2);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (1, 3);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (2, 1);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (2, 2);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (2, 3);

INSERT INTO RolePermissions(roleID, permissionID)
VALUES (3, 1);


