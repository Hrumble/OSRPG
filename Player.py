from Entity import *
from Container import *
from ArmorItem import ArmorItem
from WeaponItem import *
import json

class Player(Entity):
    def __init__(self, id, name, health, damage):
        super().__init__(id, name)
        self.isAdmin = False
        self.adminError = "[SYSTEM] This command requires admin status (sudo)"
        self.isInteracting = False
        self.currentTrader = 0
        self.currentFight = 0
        self.currentBiome = 0
        self.state = StateMachine.Basic
        self._damage = damage
        self.xp = 0
        self.money = 0
        self._health = health
        self.inventory = Container("Player Inventory")
        self.equipment = {
            "head": 0,
            "chest": 0,
            "legs": 0,
            "feet": 0,
            "hand": 0
        }
        self.currentHealth = self.maxHealth
        self.currentArmorHealth = self.maxArmorHealth

    @property
    def level(self):
        return int(self.xp/100)

    @property
    def damage(self):
        if self.equipment["hand"] != 0:
            return self._damage + self.equipment["hand"].damage + self.level
        else:
            return self._damage + self.level

    @property
    def maxArmorHealth(self):
        health = 0
        for slot in self.equipment:
            armorItem = self.equipment[slot]
            if armorItem != 0 and slot != "hand":
                health += armorItem.protection
        return health

    @property
    def maxHealth(self):
        return self._health + self.level

    def TakeDamage(self, damage):
        difference = damage - self.currentArmorHealth
        if difference >= 0:
            self.currentArmorHealth = 0
            self.currentHealth -= difference
        elif difference < 0:
            self.currentArmorHealth -= damage

    def Die(self):
        print("----- Player Died -----")
        quit()

    def Craft(self, itemID):
        from WorldRegistry import ITEM_REGISTRY

        item = ITEM_REGISTRY.GetByID(itemID)
        if not item.craftable:
            print("[SYSTEM] Cannot craft this")
            return
        jsonF = 0
        with open(item.craftingDir, "r") as f:
            jsonF = json.load(f)
        for id in jsonF["materials"]:
            quantity = jsonF["materials"][id]
            if not self.inventory.HasItem(id, quantity)[1]:
                print(f"[Player] You are missing {ITEM_REGISTRY.GetByID(id).name} x{quantity - self.inventory.HasItem(id, quantity)[2]}")
                return
        for id in jsonF["materials"]:
            quantity = jsonF["materials"][id]
            print(f"[Player] used {ITEM_REGISTRY.GetByID(id).name} x{quantity}")
            self.inventory.RemoveFromContainer(ITEM_REGISTRY.GetByID(id), quantity)
        self.inventory.AddToContainer(item)
        print(f"[Player] Crafted {item.name}")
        print("-------------------------------------------")

    def Equip(self, equipmentPiece):
        if not (isinstance(equipmentPiece, ArmorItem) or isinstance(equipmentPiece, WeaponItem)):
            print("[System] Cannot equip this")
            return
        if self.equipment[equipmentPiece.slot] != 0:
            self.inventory.AddToContainer(self.equipment[equipmentPiece.slot])
        self.equipment[equipmentPiece.slot] = equipmentPiece
        self.inventory.RemoveFromContainer(equipmentPiece)
        print(f"[Player] Equipped {equipmentPiece.name} on {equipmentPiece.slot}")
        if not self.state == StateMachine.Fighting:
            self.currentArmorHealth = self.maxArmorHealth

    def Unequip(self, slot):
        equipmentPiece = self.equipment[slot]
        self.inventory.AddToContainer(equipmentPiece)
        self.equipment[slot] = 0
        print(f"[Player] Unequipped {equipmentPiece.name} off {equipmentPiece.slot}")

    def ShowEquipment(self):
        print("----- Equipped -----")
        print(f"Armor Health: {self.maxArmorHealth}")
        for slot in self.equipment:
            if self.equipment[slot] != 0:
                print(f"{slot} -> {self.equipment[slot].name}")
            else:
                print(f"{slot} : None")
        print("--------------------------------------")

    def ShowStats(self):
        print("----- Player\'s stats -----")
        print(f"You have {self.money} coins")
        print(f"Current HP is {self.currentHealth}")
        print(f"Current XP is {self.xp} and Current Level is {self.level}")
        print("--------------------------------------")

class StateMachine:
    Basic = "Basic"
    Trading = "Trading"
    Fighting = "Fighting"




