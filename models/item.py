from db.from_db import loadItemsFromDB
from math import ceil


class Item:
    # Goods class
    inventory = loadItemsFromDB()

    def __init__(self, id):
        item = list(filter(lambda x: x.get("id") == id, Item.inventory))

        # items properties
        self.name = item[0]["name"]
        self.category = item[0]["category"]
        self.price = item[0]["price"]
        self.imported = item[0]["imported"]
        self.tax = self.itemTaxCalculator()

    # calculate tax for a given item
    def itemTaxCalculator(self):

        currentTax = 0
        noTaxItem = ["books", "food", "medical"]  # item with no tax
        # Basic sales tax is applicable at a rate of 10% on all goods
        standardItemTax = 10
        # on all imported goods at a rate of 5%, with no exemptions.
        importedItemTax = 5

        # add specific tax for items
        if self.imported is True:
            currentTax += importedItemTax
        if self.category not in noTaxItem:
            currentTax += standardItemTax

        # transform and calculate tax

        # The rounding rules for sales tax are that for a tax
        # rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of
        # sales tax.

        percentTax = (currentTax / 100) * self.price
        roundedTax = ceil(round(percentTax, 2) * 20) / 20

        return roundedTax
