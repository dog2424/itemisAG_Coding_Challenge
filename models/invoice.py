from models.item import Item
from math import ceil


class Invoice:
    def __init__(self):
        self.invoice = []

    def addNewItem(self, qty, id):

        itemToBeAdded = (id, qty)
        self.invoice.append(itemToBeAdded)

    def invoiceTotalTax(self):
        invoiceTotalTax = 0
        for value in self.invoice:
            item = Item(value[0])

            invoiceTotalTax += item.tax * value[1]
            roundedTax = ceil(round(invoiceTotalTax, 2) * 20) / 20

        return roundedTax

    def grandTotal(self):
        invoiceTotalTax = self.invoiceTotalTax()
        total = 0
        for value in self.invoice:
            item = Item(value[0])
            total += item.price * value[1]
        grandTotal = invoiceTotalTax + total

        return invoiceTotalTax, grandTotal

    def invoiceDetails(self):

        values = []
        for value in self.invoice:
            item = Item(value[0])
            grandTotal = item.price + item.tax
            values.append(
                "> " + "{} {} at {:.2f}".format(value[1], item.name, grandTotal)
            )

        invoiceTotalTax, grandTotal = self.grandTotal()

        print("\n".join(values))
        print("> Sales Taxes: " + str(invoiceTotalTax))
        print("> Total: " + str(round((grandTotal), 2)))
