from db.from_db import loadItemsFromDB

class Item():

    inventory = loadItemsFromDB()

    def __init__(self, id):
        item = list(filter(lambda x: x.get('id') == id, Item.inventory))

        self.name = item[0]['name']
        self.category = item[0]['category']
        self.price = item[0]['price ']
        self.imported = item[0]['imported']
        self.tax = self.itemTaxCalculator()

    def itemTaxCalculator(self):
        tax = 0
        return tax