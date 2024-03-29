from Entities.InventoryEntity import InventoryEntity
import random
from Fight import *
from Container import *


class Enemy(InventoryEntity):
    def __init__(self, id, name, baseHealth, baseDamage, xpDrop=5):
        super().__init__(id, name, "Enemies")
        self._damage = baseDamage
        self._health = baseHealth
        self.xpDrop = xpDrop
        self.level = 0
        self.type = "Enemy"

    @property
    def damage(self):
        return self.level + self._damage

    @property
    def maxHealth(self):
        return self.level + self._health

    def DropLoot(self, player):
        print(f"----- {self.name} dropped -----")
        for inventoryItem in self.inventory.inventory:
            print(f"{inventoryItem.item.name} x{inventoryItem.quantity}")
            player.inventory.AddToContainer(inventoryItem.item.ID, inventoryItem.quantity)
        print("--------------------------------------")

    def Die(self, player):
        self.currentHealth = 0
        print(f"{self.name} has died")
        player.xp += int(self.xpDrop*self.level)
        player.currentArmorHealth = player.maxArmorHealth
        self.DropLoot(player)

    def Interact(self, player):
        self.currentHealth = self.maxHealth
        from Entities.Player import StateMachine
        player.isInteracting = True
        player.state = StateMachine.Fighting
        player.currentFight = Fight(player, self)
        print(f"-- You Stumbled Upon a {self.name}! --")
        print(f"Lvl {self.level}  HP {self.currentHealth}")
        print("--------------------------------------")

    def DisplayInfo(self):
        print(f"----------- {self.name} -------------")
        print(f"Lvl {self.level}  HP {self.currentHealth}")
        print("--------------------------------------")