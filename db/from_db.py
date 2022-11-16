import os
import json

def loadItemsFromDB():
    
    with open(os.path.join('data', 'database.json'), 'r') as database:
        inventory = json.load(database)

    return inventory