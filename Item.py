class Item:
    def __init__(self, id, name, value = 1):
        self._id = id
        self.name = name
        self.value = value
        self.type = "item"

    @property
    def ID(self):
        return self._id

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity