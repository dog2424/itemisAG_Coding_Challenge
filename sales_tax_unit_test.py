import unittest
from models.item import Item
from models.invoice import Invoice


class TestItem(unittest.TestCase):
    def testStandardTax(self):
        order = Item("testSdTax01")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0.4)

    def testItemWithoutTax(self):
        order = Item("testSdTax02")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0)

    def testImportedTax(self):
        order = Item("testSdTax03")
        print(order.itemTaxCalculator)

        self.assertEqual(order.tax, 0.6)

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

    def testInvoiceTotalTax(self):
        testInv = self.AddingItems()
        self.assertEqual(testInv.invoiceTotalTax(), 1.2)

    def testGrandTotal(self):
        testInv = self.AddingItems()

        invoiceTotalTax, grandTotal = testInv.grandTotal()
        self.assertEqual(invoiceTotalTax, 1.2)
        self.assertEqual(grandTotal, 17.2)


unittest.main()
