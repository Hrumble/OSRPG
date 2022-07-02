from Item import *

class Container:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    def DisplayInventory(self):
        print(f"----- {self.name} -----")
        for inventoryItem in self.inventory:
            print(f"{inventoryItem.item.name} x{inventoryItem.quantity}")

    def GetItemIndex(self, itemID, quantity = 1):
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemID and inventoryItem.quantity >= quantity:
                return self.inventory.index(inventoryItem)
        return False

    def AddToContainer(self, itemToAdd, quantityToAdd = 1):
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemToAdd.ID:
                inventoryItem.quantity += quantityToAdd
                return
        self.inventory.append(itemToAdd, quantityToAdd)

    def RemoveFromContainer(self, itemToRemove, quantityToRemove = 1):
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemToRemove.ID:
                inventoryItem.quantity -= quantityToRemove

                if inventoryItem.quantity <= 0:
                    self.inventory.remove(inventoryItem)
                return
