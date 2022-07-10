import json

class Item:
    def __init__(self, id, name, value = 1, craftable = False):
        self._id = id
        self.name = name
        self.value = value
        self.type = "item"
        self.craftable = craftable
        self.craftingDir = "CraftingRecipes/" + self.ID + ".json"

    @property
    def ID(self):
        return self._id

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

