from Item import Item

class EquipableItem(Item):

    def __init__(self, id, name, value=True, craftable=False):
        super().__init__(id, name, value, craftable)

    def OnEquip(self):
        """
            Function is called when Item is equipped
        """
        pass

    def OnUnequip(self):
        """
            Function is called when Item is Unequipped
        """
        pass