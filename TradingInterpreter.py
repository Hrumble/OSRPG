from PlayerManager import *
from GeneralInterpreter import *
from cmd import Cmd

class TradingConsole(Cmd):
    prompt = "TRADE>> "

    def postcmd(self, stop, line):
        self.do_EOF(line)
        from Interpreter import StartGame
        StartGame()
        return Cmd.postcmd(self, stop, line)

    def do_buy(self, args):
        args = args.split()
        # if no quantity is specified, set it to 1
        if len(args == 1):
            args[1] = 1
        MAIN_PLAYER.currentTrader.SellToPlayer(args[0], args[1], MAIN_PLAYER)

    def do_sell(self, args):

        args = args.split()
        if len(args == 1):
            args[1] = 1
        MAIN_PLAYER.currentTrader.BuyFromPlayer(args[0], args[1], MAIN_PLAYER)

    def do_show(self, args):

        if args == "inventory":
            MAIN_PLAYER.inventory.DisplayInventory()
        if args == "equipped":
            MAIN_PLAYER.ShowEquipment()
        if args == "trade":
            MAIN_PLAYER.currentTrader.ShowTrades()
        if args == "stat":
            MAIN_PLAYER.ShowStats()

    def do_leave(self, args):
        if args:
            print("(No arguments need to be specified)")
        print("-----------------------------------")
        print("[WORLD] The trader wandered away...")
        print("-----------------------------------")
        MAIN_PLAYER.currentBiome.MoveEntity(MAIN_PLAYER.currentTrader, MAIN_PLAYER.currentBiome.GetRandomPosition())
        MAIN_PLAYER.state = StateMachine.Basic
        MAIN_PLAYER.isInteracting = False

    def do_help(self, args):
        print("----- Trading Help -----")
        print("use [show <trades/inventory/equipped/stats>] to display info")
        print("use [buy <index> <quantity>] to buy a certain quantity of items from the trader")
        print("use [sell <index> <quantity>] to sell a certain quantity of items from your inventory to the trader")
        print("use [use <index>] to use a consumable")
        print("use [leave] to leave")
        print("--------------------------------")

    def do_EOF(self, line):
        return True

