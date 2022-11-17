from models.item import Item
class Invoice():

    def __init__(self):
        self.invoice = []

    def addNewItem(self, id ,qty):

        itemToBeAdded = (id, qty)
        self.invoice.append(itemToBeAdded)

    def invoiceTotalTax(self):
        invoiceTotalTax = 0
        for value in self.invoice:
            item = Item(value[0])
            invoiceTotalTax += (item.tax * value[1])
        
        return invoiceTotalTax
    
    def grandTotal(self):
        invoiceTotalTax = self.invoiceTotalTax()
        total = 0
        for value in self.invoice:
            item = Item(value[0])
            total += item.price*value[1]
        grandTotal = invoiceTotalTax + total

        return invoiceTotalTax, grandTotal

    def invoiceDetails(self):

        values = []
        for value in self.invoice:
            item = Item(value[0])
            grandTotal = item.price + item.tax
            values.append(value[1], item.name, grandTotal)
        
        invoiceTotalTax, grandTotal = self.grandTotal()

        print(values)
        print(invoiceTotalTax)
        print(grandTotal)
            