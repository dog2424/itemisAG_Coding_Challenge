from app.main import loadFromDB

class Item():

    inventory = loadFromDB()

    def __init__(self):
        item = list(Item.inventory)

        self.name = item[0]['name']
        self.category = item[0]['category']
        self.price = item[0]['price ']
        self.tax = self.itemTaxCalculator()

    def itemTaxCalculator(self):
        tax = 0
        return tax