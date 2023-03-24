from Entities.InventoryEntity import InventoryEntity
from Container import *

class Chest(InventoryEntity):
    def __init__(self, id, name, requiresKey=False, keyID="no_id"):
        super().__init__(id, name, "Chests")
        self.inventory = Container(name)
        self.requiresKey = requiresKey
        self.keyID = keyID  # Item ID
        self.type = "Chest"

    def Interact(self, player):
        from Entities.Player import StateMachine
        player.isInteracting = True
        player.state = StateMachine.OpeningChest
        player.currentChest = self
        print(f"----- you have spotted a {self.name} -----")
        self.inventory.DisplayInventory()

    def GetContents(self, player):
        print(f"-- {player.name} has opened the chest --")
        for inventoryItem in self.inventory.inventory:
            player.inventory.AddToContainer(inventoryItem.item.ID, inventoryItem.quantity)
            print(f"- You got {inventoryItem.item.name} x{inventoryItem.quantity} from {self.name}")
        print("-----------------------------------")

    def Open(self, player):
        if self.requiresKey:
            from Registries.Registry import ITEM_REGISTRY
            # checks if item is in inventory no matter the quantity
            if self.inventory.HasItem(self.keyID)[0]:
                self.inventory.RemoveFromContainer(self.keyID)
            else:
                print(f"- This Chest requires a {ITEM_REGISTRY.GetName(self.keyID)} to be opened")
                return
        self.GetContents(player)


123
