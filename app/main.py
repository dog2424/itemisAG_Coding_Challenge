from db.from_db import loadShoppingBasketsFromDB
from models.invoice import Invoice
import sys

def main():
    
    shoppingCart = []

    shoppingCart = loadShoppingBasketsFromDB(sys.argv[1])

    currentInvoice = Invoice()

    for value in shoppingCart:
        currentInvoice.addNewItem(value[0], value[1])

    sys.exit(0)




