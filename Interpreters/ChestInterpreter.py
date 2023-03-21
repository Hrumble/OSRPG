from PlayerManager import *
from cmd import Cmd
from Interpreters.GeneralInterpreter import GeneralCommands

class ChestConsole(GeneralCommands):

    prompt = "CHEST>> "

    def do_open(self, args):
        MAIN_PLAYER.currentChest.Open(MAIN_PLAYER)
        self.do_leave("")
        MAIN_PLAYER.currentBiome.KillEntity(MAIN_PLAYER.currentChest)

    def do_leave(self, args):
        print("----------------------------------")
        print(f"[WORLD] {MAIN_PLAYER.name} stepped back from the chest")
        print("----------------------------------")
        MAIN_PLAYER.yPos -= 1
        MAIN_PLAYER.state = StateMachine.Basic
        MAIN_PLAYER.isInteracting = False

    def do_help(self, args):
        print("----- Chest Help -----")
        print("use [show <contents/inventory/equipped/stats>] to display info")
        print("use [open] to try opening the chest")
        print("use [leave] to leave")
        print("--------------------------------")