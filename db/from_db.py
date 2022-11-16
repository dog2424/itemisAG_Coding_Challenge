import os
import json

def loadItemsFromDB():

    with open(os.path.join('data', 'itemDB.json'), 'r') as itemDB:
        inventory = json.load(itemDB)

    return inventory

def loadTaxFromDB():

    with open(os.path.join('data', 'taxDB.json'), 'r') as taxDB:
        taxes = json.load(taxDB)

    return taxes