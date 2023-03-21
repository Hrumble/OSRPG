from Items.EquipableItem import EquipableItem


class ArmorItem(EquipableItem):

    headSlot = "head"
    chestSlot = "chest"
    legSlot = "legs"
    feetSlot = "feet"

    def __init__(self, id, name, value, protection, slot, craftable=True):
        super().__init__(id, name, value, craftable)
        self.protection = protection
        self.slot = slot
        self.type = "Armor"

    def ExtraInfo(self):
        print(f"Protection: {self.protection}")
