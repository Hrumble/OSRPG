from Entity import *
from Container import *
from ArmorItem import ArmorItem

class Player(Entity):
    def __init__(self, id, name, health, damage):
        super().__init__(id, name)
        self._damage = damage
        self._health = health
        self.inventory = Container("Player Inventory")
        self.equipment = {
            "head": 0,
            "chest": 0,
            "legs": 0,
            "feet": 0,
            "hand": 0
        }

    @property
    def damage(self):
        if self.equipment["hand"] != 0:
            return self._damage + self.equipment["hand"].damage
        else:
            return self._damage

    @property
    def armorHealth(self):
        health = 0
        for slot in self.equipment:
            armorItem = self.equipment[slot]
            if armorItem != 0 and slot != "hand":
                health += armorItem.protection
        return health

    def Equip(self, equipmentPiece):
        if not isinstance(equipmentPiece, ArmorItem):
            print("[System] Cannot equip this")
            return
        if self.equipment[equipmentPiece.slot] != 0:
            self.inventory.AddToContainer(self.equipment[equipmentPiece.slot])
        self.equipment[equipmentPiece.slot] = equipmentPiece
        print(f"-Equiped {equipmentPiece.name} on {equipmentPiece.slot}")











