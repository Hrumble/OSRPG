from Entities.Entity import Entity
import json
from random import randint


class InventoryEntity(Entity):

    def __init__(self, id, name, loot_table_dir):
        super().__init__(id, name)
        from Container import Container
        self.inventory = Container(f"{self.name}'s inventory")
        self.loot_table_dir = f"LootTables/{loot_table_dir}/{self.ID}.json"

    def ExtraInfo(self):
        print("Possible drops: ")
        with open(self.loot_table_dir, "r") as f:
            jsonF = json.load(f)
        items_needed = jsonF["items"]
        chance = jsonF["chance"]
        from Registries.Registry import ITEM_REGISTRY
        # Check the loot table for item's id and the chance to get that item, then adds it in the inventory
        i = 0
        for id in items_needed:
            print(f"{i}. {ITEM_REGISTRY.GetName(id)} x{items_needed[id]} : chance of dropping is {chance[i]}%")
            i+=1

    def PopulateInventory(self):
        with open(self.loot_table_dir, "r") as f:
            jsonF = json.load(f)
        items_needed = jsonF["items"]
        chance = jsonF["chance"]
        # Check the loot table for item's id and the chance to get that item, then adds it in the inventory
        i = 0
        for id in items_needed:
            luck = randint(0, 100)
            if luck <= chance[i]:
                self.inventory.AddToContainer(id, items_needed[id])
            i += 1

    def OnSpawn(self):
        self.PopulateInventory()