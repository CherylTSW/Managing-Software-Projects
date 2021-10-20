import unittest
from lib import inventory

class TestInventory(unittest.TestCase):

    # Test case to test if create_inventory_db() created the database successfully
    def test_create_inventory_db(self):
        inventory.create_inventory_db()
        mydb = inventory.connect_inventory_db()
        self.assertTrue(mydb)
    
    # Test case to to test if execute_sql_file() read and execute sql code from a file successfully
    def test_execute_sql_file(self):
        inventory.execute_sql_file("sql/InventoryDB.sql")
        mydb = inventory.connect_inventory_db()
    
        # Iterate through the cursor to obtain the tables present in database
        myCursor = mydb.cursor()
        myCursor.execute("SHOW TABLES")
        result = ""
        for table in myCursor:
            result += str(table)
        print(result)

        # If SQL code from file executed successfully, table should be created and result != ""
        self.assertNotEqual(result, "")
    
    # Test case to test if add_inventory() INSERT an item into the table successfully
    def test_add_inventory(self):
        result = inventory.add_inventory("Panadol 20 Tablets", 12.90, 100)
        self.assertTrue(result)
    
    
if __name__ == '__main__':
    unittest.main()