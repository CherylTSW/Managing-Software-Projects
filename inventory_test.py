import unittest
from lib import inventory

class TestInventory(unittest.TestCase):

    # Test case to ensure ExecuteSQLFIle() read and execute sql code from a file successfully
    def test_ExecuteSQLFile(self):
        result = inventory.ExecuteSQLFile("sql/InventoryDB.sql")
        self.assertNotEqual(result, "")
    
    # Test case to ensure AddInventory() INSERT an item into the table successfully
    def test_AddInventory(self):
        inventory.CreateInventoryDB()
        result = inventory.AddInventory("Panadol 20 Tablets", 12.90, 100)
        self.assertEqual(result, 1)
    
    
if __name__ == '__main__':
    unittest.main()