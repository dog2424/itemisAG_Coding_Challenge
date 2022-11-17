from db.from_db import loadShoppingBasketsFromDB
from models.invoice import Invoice
import sys


def main():

    shoppingCart = []

    shoppingCart = loadShoppingBasketsFromDB(sys.argv[1])

    currentInvoice = Invoice()

    for value in shoppingCart:
        print(value[0])
        print(value[1])
        currentInvoice.addNewItem(value[0], value[1])

    currentInvoice.invoiceDetails()
    sys.exit(0)


main()
