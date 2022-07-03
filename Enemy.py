from Entity import *
import random

class Enemy(Entity):
    def __init__(self, id, name, baseHealth, baseDamage, level, lootTable):
        super().__init__(id, name)
        self._damage = baseDamage
        self._health = baseHealth
        self.lootTable = lootTable
        self.level = level

    @property
    def damage(self):
        return self.level + self._damage
    @property
    def health(self):
        return self.level + self._health

    def DropLoot(self, player):
        drops = self.lootTable.GetInventoryItems()
        print(f"----- {self.name} dropped -----")
        for inventoryItem in drops:
            print(f"{inventoryItem.item.name} x{inventoryItem.quantity}")
            player.inventory.AddToContainer(inventoryItem.item, inventoryItem.quantity)


