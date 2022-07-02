from Item import *

class WeaponItem(Item):
    def __init__(self, id, name, value, damage):
        super().__init__(id, name, value)
        self.damage = damage
