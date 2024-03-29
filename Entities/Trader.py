from Entities.InventoryEntity import InventoryEntity
from Container import *


class Trader(InventoryEntity):
    def __init__(self, id, name, resellRate):
        super().__init__(id, name, "Traders")
        self.resellRate = resellRate
        self.type = "Trader"

    def BuyFromPlayer(self, index, quantity, player):
        if len(player.inventory.inventory) <= index:
            print("[SYSTEM] The index specified does not contain an item")
            return
        item = player.inventory.inventory[index].item
        if player.inventory.RemoveFromContainer(item.ID, quantity):
            player.money += item.value * quantity
            self.inventory.AddToContainer(item.ID, quantity)
            player.xp += 1
            print(f"- You sold {item.name} x{quantity} to {self.name}")
        else:
            print(f"[{self.name}] Don\'t try and sell me what you don\'t have!")

    def SellToPlayer(self, index, quantity, player):
        item = self.inventory.inventory[index].item
        price = int(item.value * self.resellRate * quantity)
        if player.money >= price:
            player.inventory.AddToContainer(item.ID, quantity)
            player.money -= price
            self.inventory.RemoveFromContainer(item.ID, quantity)
            player.xp += 1
            print(f"- You bought {item.name} x{quantity} from {self.name}")
        else:
            print(f"[{self.name}] You don\'t have enough money for that...")

    def Interact(self, player):
        from Entities.Player import StateMachine
        player.isInteracting = True
        player.state = StateMachine.Trading
        player.currentTrader = self
        print(f"----- you have spotted a {self.name} -----")
        self.ShowTrades()

    def ShowTrades(self):
        print("----- Trades -----")
        print(f"Resell Rate of: {self.resellRate}")
        i = 0
        while i < len(self.inventory.inventory):
            # Gets the inventoryItem
            inventoryItemI = self.inventory.inventory[i]
            price = int(inventoryItemI.item.value * self.resellRate)
            # if this is not the last item in the list print it on two separate lines
            # Otherwise print a single line
            if i != len(self.inventory.inventory) - 1:
                inventoryItemI1 = self.inventory.inventory[i + 1]
                price1 = int(inventoryItemI1.item.value * self.resellRate)
                print(f"{i}. [{inventoryItemI.item.type}] {inventoryItemI.item.name} x{inventoryItemI.quantity}  {price} coins      "
                      f"{i + 1}. [{inventoryItemI1.item.type}] {inventoryItemI1.item.name} x{inventoryItemI1.quantity}  {price1} coins")
            else:
                print(f"{i}. [{inventoryItemI.item.type}] {inventoryItemI.item.name} x{inventoryItemI.quantity}  {price} coins      ")
            i += 2
        print("--------------------------------------")
