from Item import *

headSlot = "head"
chestSlot = "chest"
legSlot = "legs"
feetSlot = "feet"


class ArmorItem(Item):
    def __init__(self, id, name, value, protection, slot):
        super().__init__(id, name, value)
        self.protection = protection
        self.slot = slot
