class Invoice():

    def __init__(self):
        self.invoice = []

    def addNewItem(self, id ,qty):

        itemToBeAdded = (id, qty)
        self.invoice.append(itemToBeAdded)

