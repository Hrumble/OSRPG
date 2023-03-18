from PlayerManager import *
from GeneralInterpreter import *
import random
from cmd import Cmd

class FightingConsole(Cmd):
    prompt = "FIGHT>> "
    def do_show(self, args):
        # Shows info on current player things

        if len(args) == 0:
            print("Usage: show <info/inventory/equipped/stat>")
        if args[0] == "info":
            MAIN_PLAYER.currentFight.enemy.DisplayInfo()
        if args[0] == "inventory":
            MAIN_PLAYER.inventory.DisplayInventory()
        if args[0] == "equipped":
            MAIN_PLAYER.ShowEquipment()
        if args[0] == "stat":
            MAIN_PLAYER.ShowStats()
    def do_help(self, args):
        print("----- Fighting Help -----")
        print("-use [show <info/inventory/equipped/stats>] to display info")
        print("-use [attack] to attack the enemy")
        print("-use [equip <index>] to equip an item in inventory")
        print("use [use <index>] to use a consumable")
        print("-use [run] to try running away")
        print("--------------------------------")
    def do_attack(self):
        MAIN_PLAYER.currentFight.PlayerAttack()

    def do_run(self):
        chance = random.randint(0, 100)
        print("----- Player Tries To run -----")
        if chance <= 65:
            print("Player successfully ran away")
            MAIN_PLAYER.state = StateMachine.Basic
            MAIN_PLAYER.isInteracting = False
            MAIN_PLAYER.currentBiome.MoveEntity(MAIN_PLAYER.currentFight.enemy,
                                                MAIN_PLAYER.currentBiome.GetRandomPosition())
        else:
            print("Player failed to Run")
            print("--------------------------------------")
            MAIN_PLAYER.currentFight.EnemyAttack()

