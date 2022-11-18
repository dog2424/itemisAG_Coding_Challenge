import unittest
from models.item import Item
from models.invoice import Invoice
from db.from_db import *


class TestItem(unittest.TestCase):
    # test standard item taxes
    def testStandardTax(self):
        order = Item("testSdTax01")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0.4)

    # test  item without taxes
    def testItemWithoutTax(self):
        order = Item("testSdTax02")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0)

    # test imported item taxes
    def testImportedTax(self):
        order = Item("testSdTax03")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0.6)

    # test imported item taxes in the exception
    def testImportedWithoutTax(self):
        order = Item("testSdTax04")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0.2)


class TestInvoice(unittest.TestCase):
    def AddingItems(self):
        items = [
            (1, "testSdTax01"),
            (1, "testSdTax02"),
            (1, "testSdTax03"),
            (1, "testSdTax04"),
        ]
        testInv = Invoice()
        for item in items:
            testInv.addNewItem(item[0], item[1])

        return testInv

    # test sum of taxes
    def testInvoiceTotalTax(self):
        testInv = self.AddingItems()
        self.assertEqual(testInv.invoiceTotalTax(), 1.2)

    # test total taxes and total with tax
    def testGrandTotal(self):
        testInv = self.AddingItems()

        invoiceTotalTax, grandTotal = testInv.grandTotal()
        self.assertEqual(invoiceTotalTax, 1.2)
        self.assertEqual(grandTotal, 17.2)


class TestItemDB(unittest.TestCase):
    # check intemDB.json correctness
    def testItemsDB(self):
        inventory = loadItemsFromDB()
        inventoryCheck = False
        property = ["id", "name", "category", "imported", "price"]
        for item in inventory:

            print(item)
            if not len([x for x in property if x in item]) == len(property):
                inventoryCheck = False
            else:
                inventoryCheck = True

        self.assertEqual(inventoryCheck, True)


unittest.main()
