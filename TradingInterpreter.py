from PlayerManager import *
from GeneralInterpreter import *

def interpret(command):
    eval(command)

def buy(index, quantity = 1):
    MAIN_PLAYER.currentTrader.SellToPlayer(index, quantity, MAIN_PLAYER)

def sell(index, quantity = 1):
    MAIN_PLAYER.currentTrader.BuyFromPlayer(index, quantity, MAIN_PLAYER)

def show(thing):
    if thing == "inventory":
        MAIN_PLAYER.inventory.DisplayInventory()
    if thing == "equipped":
        MAIN_PLAYER.ShowEquipment()
    if thing == "trade":
        MAIN_PLAYER.currentTrader.ShowTrades()
    if thing == "stat":
        MAIN_PLAYER.ShowStats()

def leave():
    print("-----------------------------------")
    print("[WORLD] The trader wandered away...")
    print("-----------------------------------")
    MAIN_PLAYER.currentBiome.MoveEntity(MAIN_PLAYER.currentTrader, MAIN_PLAYER.currentBiome.GetRandomPosition())
    MAIN_PLAYER.state = StateMachine.Basic
    MAIN_PLAYER.isInteracting = False

def help():
    print("----- Trading Help -----")
    print("use [show <trades/inventory/equipped/stats>] to display info")
    print("use [buy <index> <quantity>] to buy a certain quantity of items from the trader")
    print("use [sell <index> <quantity>] to sell a certain quantity of items from your inventory to the trader")
    print("use [use <index>] to use a consumable")
    print("use [leave] to leave")
    print("--------------------------------")