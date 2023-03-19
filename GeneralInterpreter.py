from PlayerManager import *
from cmd import Cmd

class GeneralCommands(Cmd):

    prompt = "> "

    def postcmd(self, stop, line):
        self.do_EOF(line)
        from Interpreter import StartGame
        StartGame()
        return Cmd.postcmd(self, stop, line)

    def do_equip(self, args):

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

    def do_Default(self, line):
        print("[SYSTEM]Command does not exist or is entered wrongly")
