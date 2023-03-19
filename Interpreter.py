import FightingInterpreter
import TradingInterpreter
from PlayerManager import *
from Player import StateMachine
import BasicInterpreter
from Fight import *
from WorldRegistry import *
import FightingInterpreter

def DrawMiniMap():
    biome = MAIN_PLAYER.currentBiome
    if biome == 0:
        print("[Minimap ERROR]")
        return
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

def StartGame():
    while True:

        PositionUpdate()
        if MAIN_PLAYER.state == StateMachine.Basic:
            DrawMiniMap()
            BasicInterpreter.BasicConsole().cmdloop()
        if MAIN_PLAYER.state == StateMachine.Trading:
            TradingInterpreter.interpret()
        if MAIN_PLAYER.state == StateMachine.Fighting:
            FightingInterpreter.FightingConsole().cmdloop()
