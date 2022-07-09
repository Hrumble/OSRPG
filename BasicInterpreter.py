from PlayerManager import *

north = "north"
south = "south"
east = "east"
west = "west"
inventory = "inventory"
equipped = "equipped"
equipment = "equipped"
stats = "stat"
stat = "stat"
pos = "position"
position = "position"

def interpret(command):
    eval(command)

def show(thing):
    if thing == "inventory":
        MAIN_PLAYER.inventory.DisplayInventory()
    if thing == "equipped":
        MAIN_PLAYER.ShowEquipment()
    if thing == "stat":
        MAIN_PLAYER.ShowStats()
    if thing == "position":
        print(f"{MAIN_PLAYER.xPos} Latitude {MAIN_PLAYER.yPos} Longitude")
        print(f"Current Biome: {MAIN_PLAYER.currentBiome.name} Lvl: {MAIN_PLAYER.currentBiome.level}")

def equip(inventoryIndex):
    MAIN_PLAYER.Equip(MAIN_PLAYER.inventory.inventory[inventoryIndex].item)

def go(direction):
    if direction == "north":
        MAIN_PLAYER.yPos += 1
    if direction == "south":
        MAIN_PLAYER.yPos -= 1
    if direction == "east":
        MAIN_PLAYER.xPos += 1
    if direction == "west":
        MAIN_PLAYER.xPos -= 1

def tp(xPos, yPos):
    MAIN_PLAYER.xPos = xPos
    MAIN_PLAYER.yPos = yPos

def use(index):
    item = MAIN_PLAYER.inventory.inventory[index].item
    if isinstance(item, ConsumableItem):
        item.Consume()
    else:
        print("[SYSTEM] You can\'t consume that")

def help():
    print("----- Command Help -----")
    print("-use [show <trades/inventory/equipped/stats>] to display info")
    print("-use [go <north/south/east/west>] to move in a particular direction")
    print("-use [equip <index>] to equip an item in inventory")