from Entity import *
import random
from Player import StateMachine
from Fight import *

class Enemy(Entity):
    def __init__(self, id, name, baseHealth, baseDamage, lootTable):
        super().__init__(id, name)
        self._damage = baseDamage
        self._health = baseHealth
        self.lootTable = lootTable
        self.level = 0
        self.currentHealth = 0

    @property
    def damage(self):
        return self.level + self._damage

    @property
    def maxHealth(self):
        return self.level + self._health

    def DropLoot(self, player):
        drops = self.lootTable.GetInventoryItems()
        print(f"----- {self.name} dropped -----")
        for inventoryItem in drops:
            print(f"{inventoryItem.item.name} x{inventoryItem.quantity}")
            player.inventory.AddToContainer(inventoryItem.item, inventoryItem.quantity)

    def Die(self, player):
        print(f"{self.name} has died")
        self.DropLoot(player)

    def Interact(self, player):
        self.currentHealth = self.maxHealth
        player.isInteracting = True
        player.state = StateMachine.Fighting
        player.currentFight = Fight(player, self)
        print(f"----- You Stumbled Upon a {self.name}! -----")
        print(f"Lvl {self.level}  HP {self.currentHealth}")

    def DisplayInfo(self):
        print(f"----- {self.name} -----")
        print(f"Lvl {self.level}  HP {self.currentHealth}")