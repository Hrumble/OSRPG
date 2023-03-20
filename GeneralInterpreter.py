from PlayerManager import *
from cmd import Cmd

class GeneralCommands(Cmd):

    prompt = "> "

    # Constantly closes the Cmd line so the player position and info can update
    def postcmd(self, stop, line):
        self.do_EOF(line)
        from Interpreter import StartGame
        StartGame()
        return Cmd.postcmd(self, stop, line)

    def do_equip(self, args):
        if not args:
            print("Command requires an index")
            return
        inventoryIndex = int(args)
        MAIN_PLAYER.Equip(MAIN_PLAYER.inventory.inventory[inventoryIndex].item)

    def do_unequip(self, args):
        inventoryIndex = int(args)
        MAIN_PLAYER.Equip(MAIN_PLAYER.inventory.inventory[inventoryIndex].item)

    def do_craft(self, args):
        MAIN_PLAYER.Craft(args)

    def do_use(self, args):
        index = int(args)
        item = MAIN_PLAYER.inventory.inventory[index].item
        if isinstance(item, ConsumableItem):
            item.Consume(MAIN_PLAYER)
        else:
            print("[SYSTEM] You can\'t consume that")

    def do_info(self, args):
        from WorldRegistry import ITEM_REGISTRY
        ITEM_REGISTRY.GetByID(args).Info()

    def do_EOF(self, line):
        return True

    def do_sudo(self, args):
        if args == "q":
            MAIN_PLAYER.isAdmin = False
            print(f"[SYSTEM] Player Admin state switched to {MAIN_PLAYER.isAdmin}")
            return
        passw = input("Enter admin password> ")
        if passw == "root":
            MAIN_PLAYER.isAdmin = True
            print("[SYSTEM] Player is now Admin (use [sudo q] to quit)")
        else:
            print("[SYSTEM] Wrong password, find the password in RPG/GeneralInterpreter.py")

    def do_give(self, args):
        if not MAIN_PLAYER.isAdmin:
            print(MAIN_PLAYER.adminError)
            return
        if not args:
            print("[SYSTEM] You need to specify an item id")
            return

        args = args.split()

        if len(args) == 1:
            args[1] = 1

        item = ITEM_REGISTRY.GetByID(args[0])
        if not item:
            print("[SYSTEM] The ID specified does not exist")
            return
        MAIN_PLAYER.inventory.AddToContainer(item, int(args[1]))

