from db.from_db import loadItemsFromDB


class Item:

    inventory = loadItemsFromDB()

    def __init__(self, id):
        item = list(filter(lambda x: x.get("id") == id, Item.inventory))

        self.name = item[0]["name"]
        self.category = item[0]["category"]
        self.price = item[0]["price"]
        self.imported = item[0]["imported"]
        self.tax = self.itemTaxCalculator()

    def itemTaxCalculator(self):

        currentTax = 0
        noTaxItem = ["books", "food", "medical"]
        standardItemTax = 10
        importedItemTax = 5

        if self.imported is True:
            currentTax += importedItemTax
        if self.category not in noTaxItem:
            currentTax += standardItemTax

        return (currentTax / 100) * self.price
