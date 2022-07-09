from Entity import *
from Container import *
from Player import StateMachine

class Trader(Entity):
    def __init__(self, id, name, resellRate, tradesID, quantities):
        super().__init__(id, name)
        self.resellRate = resellRate
        self.inventory = Container(f"{self.name}\'s inventory")
        from WorldRegistry import ITEM_REGISTRY
        for i in range(len(tradesID) - 1):
            item = ITEM_REGISTRY.GetByID(tradesID[i])
            self.inventory.AddToContainer(item, quantities[i])

    def BuyFromPlayer(self, index, quantity, player):
        item = player.inventory.inventory[index].item
        if player.inventory.RemoveFromContainer(item, quantity):
            player.money += item.value * quantity
            self.inventory.AddToContainer(item, quantity)
            print(f"- You sold {item.name} x{quantity} to {self.name}")
        else:
            print(f"[{self.name}] Don\'t try and sell me what you don\'t have!")

    def SellToPlayer(self, index, quantity, player):
        item = self.inventory.inventory[index].item
        price = int(item.value * self.resellRate * quantity)
        if player.money >= price:
            player.inventory.AddToContainer(item, quantity)
            player.money -= price
            self.inventory.RemoveFromContainer(item, quantity)
            print(f"- You bought {item.name} x{quantity} from {self.name}")
        else:
            print(f"[{self.name}] You don\'t have enough money for that...")

    def Interact(self, player):
        player.isInteracting = True
        player.state = StateMachine.Trading
        player.currentTrader = self
        print(f"----- you have spotted a {self.name} -----")
        self.ShowTrades()

    def ShowTrades(self):
        print(f"Resell Rate of: {self.resellRate}")
        i = 0
        for inventoryItem in self.inventory.inventory:
            price = int(inventoryItem.item.value * self.resellRate)
            print(f"{i}. {inventoryItem.item.name} x{inventoryItem.quantity} {price} coins")
            i += 1
