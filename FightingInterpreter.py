from PlayerManager import *
from GeneralInterpreter import *
import random


def interpret(command):
    eval(command)

def show(thing):
    if thing == "info":
        MAIN_PLAYER.currentFight.enemy.DisplayInfo()
    if thing == "inventory":
        MAIN_PLAYER.inventory.DisplayInventory()
    if thing == "equipped":
        MAIN_PLAYER.ShowEquipment()
    if thing == "stat":
        MAIN_PLAYER.ShowStats()

def help():
    print("----- Fighting Help -----")
    print("-use [show <info/inventory/equipped/stats>] to display info")
    print("-use [attack] to attack the enemy")
    print("-use [equip <index>] to equip an item in inventory")
    print("use [use <index>] to use a consumable")
    print("-use [run] to try running away")
    print("--------------------------------")

def attack():
    MAIN_PLAYER.currentFight.PlayerAttack()

def run():
    chance = random.randint(0, 100)
    print("----- Player Tries To run -----")
    if chance <= 65:
        print("Player successfully ran away")
        MAIN_PLAYER.state = StateMachine.Basic
        MAIN_PLAYER.isInteracting = False
        MAIN_PLAYER.currentBiome.MoveEntity(MAIN_PLAYER.currentFight.enemy, MAIN_PLAYER.currentBiome.GetRandomPosition())
    else:
        print("Player failed to Run")
        print("--------------------------------------")
        MAIN_PLAYER.currentFight.EnemyAttack()
