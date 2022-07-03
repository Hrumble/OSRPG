import random
from Item import *

class LootTable:
    def __init__(self, itemID, quantities, chances):
        self.table = {

        }
        for i in range(len(itemID)):
            self.table[f"{itemID[i]}"] = {"quantity": quantities[i], "chance": chances[i]}

    def GetInventoryItems(self):
        from WorldRegistry import Items
        items = []
        for id in self.table:
            chance = random.randint(0, 100)
            if chance <= self.table[id]["chance"]:
                items.append(InventoryItem(Items().GetByID(id), self.table[id]["quantity"]))

        return items
