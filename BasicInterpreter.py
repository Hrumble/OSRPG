from PlayerManager import *
from GeneralInterpreter import *
from cmd import Cmd

def DrawMiniMap():
    biome = MAIN_PLAYER.currentBiome
    playerPos = MAIN_PLAYER.position
    posArray = [[[playerPos[0] - 1, playerPos[1] + 1], [playerPos[0], playerPos[1] + 1], [playerPos[0] + 1, playerPos[1] + 1]],
                [[playerPos[0] - 1, playerPos[1]], playerPos, [playerPos[0] + 1, playerPos]],
                [[playerPos[0] - 1, playerPos[1] - 1], [playerPos[0], playerPos[1] - 1], [playerPos[0] + 1, playerPos[1] - 1]]]
    for position in posArray:
        left = position[0]
        middle = position[1]
        right = position[2]
        leftVal = "#"
        middleVal = "#"
        rightVal = "#"
        if biome.CheckAt(left):
            leftVal = "?"
        if biome.CheckAt(middle):
            middleVal = "?"
        if middle == playerPos:
            middleVal = "P"
        if biome.CheckAt(right):
            rightVal = "?"
        print(f"{leftVal} {middleVal} {rightVal}")

class BasicConsole(Cmd):
    
    prompt = DrawMiniMap(), "\n > "
    def do_go(self, args):
        direction = args[0]
        if direction == "north":
            MAIN_PLAYER.yPos += 1
        if direction == "south":
            MAIN_PLAYER.yPos -= 1
        if direction == "east":
            MAIN_PLAYER.xPos += 1
        if direction == "west":
            MAIN_PLAYER.xPos -= 1
    def do_tp(self, args):
        # TP the player to a specific spot on the map (Admin)

        xPos = int(args[0])
        yPos = int(args[1])

        MAIN_PLAYER.xPos = xPos
        MAIN_PLAYER.yPos = yPos

    def do_show(self, args):
        if args[0] == "inventory":
            MAIN_PLAYER.inventory.DisplayInventory()
        if args[0] == "equipped":
            MAIN_PLAYER.ShowEquipment()
        if args[0] == "stat":
            MAIN_PLAYER.ShowStats()
        if args[0] == "position":
            print(f"{MAIN_PLAYER.xPos} Latitude {MAIN_PLAYER.yPos} Longitude")
            print(f"Current Biome: {MAIN_PLAYER.currentBiome.name} Lvl: {MAIN_PLAYER.currentBiome.level}")
            print("--------------------------------------")

    def do_help(self, args):
        print("----- Command Help -----")
        print("use [show <trades/inventory/equipped/stats>] to display info")
        print("use [go <north/south/east/west>] to move in a particular direction")
        print("use [equip <index>] to equip an item in inventory")
        print("use [use <index>] to use a consumable")
        print("--------------------------------------")


