from Items.EquipableItem import EquipableItem


class WeaponItem(EquipableItem):

    def __init__(self, id, name, value, damage, craftable=True):
        super().__init__(id, name, value, craftable)
        self.damage = damage
        self.slot = "hand"
        self.type = "Weapon"

    def ExtraInfo(self):
        print(f"DMG: {self.damage}")
