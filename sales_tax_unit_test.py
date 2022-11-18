import unittest
from models.item import Item


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


unittest.main()
