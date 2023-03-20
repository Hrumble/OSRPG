import WorldRegistry
from Entity import *
from Container import *
from Player import StateMachine

class Chest(Entity):
    def __init__(self, id, name, lootTable, requiresKey=False, keyID="no_id"):
        super().__init__(id, name)
        self.inventory = Container(name)
        self.requiresKey = requiresKey
        self.keyID = keyID  # Item ID
        self.lootTable = lootTable  # class LootTable

    def Interact(self, player):
        player.isInteracting = True
        player.state = StateMachine.OpeningChest
        player.currentChest = self
        print(f"----- you have spotted a {self.name} -----")
        self.inventory.DisplayInventory()

    def OnSpawn(self):
        self.PopulateChest()

    def PopulateChest(self):
        pass

    def GetContents(self, player):
        print(f"- {player.name} has opened the chest -")
        from WorldRegistry import ITEM_REGISTRY
        for inventoryItem in self.inventory.inventory:
            player.inventory.AddToContainer(ITEM_REGISTRY.GetByID(inventoryItem.item.ID), inventoryItem.quantity)
            print(f"- You got {inventoryItem.name} x{inventoryItem.quantity} from {self.name}")
        print("-----------------------------------")

    def Open(self, player):
        if self.requiresKey:
            from WorldRegistry import ITEM_REGISTRY
            key = WorldRegistry.ITEM_REGISTRY.GetByID(self.keyID)
            if self.inventory.HasItem(self.keyID):
                self.inventory.RemoveFromContainer(key)
            else:
                print(f"- This Chest requires a {key.name} to be opened")
                return
        self.GetContents(player)


