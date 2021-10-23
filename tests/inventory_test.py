import unittest
from tkinter import *
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
        result = inventory.add_inventory("Paracetamol 10 Tablets", 12.90, 100)
        # result = False if error occurs while adding inventory
        self.assertTrue(result)

    # Test case to test if get_all_inventory() retrieve items from the database successfully
    def test_get_all_inventory(self):
        # Call the method and print the rows of the table if result != False
        result = inventory.get_all_inventory()
        if(result):
            for row in result:
                print(row)
        
        # result = False if error occurs while getting the inventory
        self.assertTrue(result)

    # Test case to test if get_inventory_by_id() retrieve correct items from the database successfully
    def test_get_inventory_by_id(self):
        # Call the method and print the record retrieved to see if expected item is retrieved
        result = inventory.get_inventory_by_id(1)
        if(result):
            for row in result:
                print(row)

        # result = False if error occurs while getting the inventory
        self.assertTrue(result)

    # Test case to test if get_inventory_by_name() retrieve correct items from the database successfully
    def test_get_inventory_by_name(self):
        # Call the method and print the record retrieved to see if expected item is retrieved
        result = inventory.get_inventory_by_name("Paracetamol 10 Tablets")
        if(result):
            for row in result:
                print(row)

        # result = False if error occurs while getting the inventory
        self.assertTrue(result)

    # Test case to test if edit_inventory() edit the item as expected
    def test_edit_inventory(self):
        # Call the method and assertTrue() function. 
        self.assertTrue(inventory.edit_inventory("Paracetamol 20 Tablets", 24.90, 30, 1))

        # Get the inventory item with itemID = 1 and print the result to see if item is edited as expected
        result = inventory.get_inventory_by_id(1)
        if(result):
            for row in result:
                print(row)

    # Test case to test if display_inventory displays the items as expected
    def test_display_inventory(self):
        window = Tk()
        window.title("PHP-SREPS")

        # Retrieve all records using get_all_inventory() and call display_inventory() to displays the records
        item = inventory.get_all_inventory()    
        inventory.display_inventory(window, 0, 0, item)

        window.attributes('-fullscreen', True)
        window.mainloop()

    
    
if __name__ == '__main__':
    unittest.main()