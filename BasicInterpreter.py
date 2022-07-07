from PlayerManager import *

inventory = "inventory"
equipped = "equipped"
equipment = "equipped"

def interpret(command):
    eval(command)

def show(thing):
    if thing == "inventory":
        MAIN_PLAYER.inventory.DisplayInventory()
    if thing == "equipped":
        MAIN_PLAYER.ShowEquipment()
    if thing == "trade":
        MAIN_PLAYER.currentTrader.ShowTrades()

def equip(inventoryIndex):
    MAIN_PLAYER.Equip(MAIN_PLAYER.inventory.inventory[inventoryIndex].item)

