from Entity import Entity
from Container import Container
import json
from random import randint


class InventoryEntity(Entity):

    def __init__(self, id, name):
        super().__init__(id, name)
        self.inventory = Container(f"{self.name}'s inventory")
        self.loot_table_dir = "LootTables/" + self.ID + ".json"

    def PopulateInventory(self):
        with open(self.loot_table_dir, "r") as f:
            jsonF = json.load(f)
        items_needed = jsonF["items"]
        chance = jsonF["chance"]
        from WorldRegistry import ITEM_REGISTRY
        # Check the loot table for item's id and the chance to get that item, then adds it in the inventory
        i = 0
        for id in items_needed:
            luck = randint(0, 100)
            if luck <= chance[i]:
                self.inventory.AddToContainer(ITEM_REGISTRY.GetByID(id), items_needed[id])

    def OnSpawn(self):
        self.PopulateInventory()