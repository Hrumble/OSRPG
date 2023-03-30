import json
import os

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

    def Info(self):
        print(f"----- {self.name} -----")
        print(f"Type: [{self.type}]")
        print(f"Value: {self.value}")
        self.ExtraInfo()
        self.ShowCrafting()
        print("------------------------")

    def ExtraInfo(self):
        pass

    def ShowCrafting(self):
        jsonF = 0
        if self.craftable and os.path.exists(self.craftingDir):
            with open(self.craftingDir, "r") as f:
                jsonF = json.load(f)
            print("--- Crafting ---")
            mats = jsonF["materials"]
            for id in mats:
                print(f"Requires {id} x{mats[id]}")
        else:
            print("-- No Crafting --")

    def OnCraft(self):
        pass

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

