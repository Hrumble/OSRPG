from Item import *


class ArmorItem(Item):
    headSlot = "head"
    chestSlot = "chest"
    legSlot = "legs"
    feetSlot = "feet"

    def __init__(self, id, name, value, protection, slot, craftable = True):
        super().__init__(id, name, value, craftable)
        self.protection = protection
        self.slot = slot
        self.type = "Armor"
