from Items.Item import *


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

    def HasItem(self, itemID, quantity = 1):
        hasItem = False
        hasQuantity = False
        itemQuantity = 0
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemID:
                hasItem = True
                itemQuantity = inventoryItem.quantity
                if itemQuantity >= quantity:
                    hasQuantity = True

        return [hasItem, hasQuantity, itemQuantity]


    def AddToContainer(self, itemID, quantityToAdd=1):
        from Registries.Registry import ITEM_REGISTRY
        from PlayerManager import MAIN_PLAYER
        item = ITEM_REGISTRY.GetByID(itemID)
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemID:
                inventoryItem.quantity += quantityToAdd
                return
        self.inventory.append(InventoryItem(item, quantityToAdd))
        if MAIN_PLAYER.debug:
            print(f"[DEBUG] {quantityToAdd}x {itemID} has been added to inventory")

    def RemoveFromContainer(self, itemID, quantityToRemove=1):
        from PlayerManager import MAIN_PLAYER
        from Registries.Registry import ITEM_REGISTRY
        for inventoryItem in self.inventory:
            if inventoryItem.item.ID == itemID:
                if inventoryItem.quantity < quantityToRemove:
                    print(f"[System] You don't have enough of {ITEM_REGISTRY.GetName(itemID)} in inventory")
                    return False
                inventoryItem.quantity -= quantityToRemove
                if MAIN_PLAYER.debug:
                    print(f"[DEBUG] {quantityToRemove}x {itemID} has been removed from {self.name}")

                if inventoryItem.quantity <= 0:
                    self.inventory.remove(inventoryItem)
                return True
