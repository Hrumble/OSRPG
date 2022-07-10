from Item import *

class Container:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def DisplayInventory(self):
        print(f"----- {self.name} -----")
        i = 0
        while i < len(self.inventory):
            if i != len(self.inventory) - 1:
                print(f"{i}. [{self.inventory[i].item.type}] {self.inventory[i].item.name} x{self.inventory[i].quantity}        "
                      f"{i+1}. [{self.inventory[i+1].item.type}] {self.inventory[i+1].item.name} x{self.inventory[i+1].quantity}  ")
            else:
                print(f"{i}. [{self.inventory[i].item.type}] {self.inventory[i].item.name} x{self.inventory[i].quantity}        ")
            i += 2
        print("--------------------------------------")


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
        self.inventory.append(InventoryItem(itemToAdd, quantityToAdd))

    def RemoveFromContainer(self, itemToRemove, quantityToRemove = 1):
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemToRemove.ID:
                if inventoryItem.quantity < quantityToRemove:
                    print(f"[System]You don't have enough of {itemToRemove} in inventory")
                    return False
                inventoryItem.quantity -= quantityToRemove

                if inventoryItem.quantity <= 0:
                    self.inventory.remove(inventoryItem)
                return True
