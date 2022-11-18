import os
import json


def loadItemsFromDB():

    with open(os.path.join("data", "itemDB.json"), "r") as itemDB:
        inventory = json.load(itemDB)

    return inventory


def loadTaxFromDB():

    with open(os.path.join("data", "taxDB.json"), "r") as taxDB:
        taxes = json.load(taxDB)

    return taxes


def loadShoppingBasketsFromDB(shoppingBasketNumb):
    cart = []
    with open(
        os.path.join("data", "shoppingBasket" + shoppingBasketNumb + ".json"), "r"
    ) as shoppingCartDB:
        shoppingCart = json.load(shoppingCartDB)
    qty = 1

    for item in shoppingCart:
        id = item["id"]
        value = (qty, id)
        cart.append(value)

    return cart
