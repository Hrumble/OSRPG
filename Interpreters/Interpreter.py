import Interpreters.TradingInterpreter
from PlayerManager import *
from Entities.Player import StateMachine
import Interpreters.BasicInterpreter
import Interpreters.FightingInterpreter
import Interpreters.ChestInterpreter


def StartGame():
    while True:

        PositionUpdate()
        if MAIN_PLAYER.state == StateMachine.Basic:
            Interpreters.BasicInterpreter.BasicConsole().cmdloop()
        if MAIN_PLAYER.state == StateMachine.Trading:
            Interpreters.TradingInterpreter.TradingConsole().cmdloop()
        if MAIN_PLAYER.state == StateMachine.Fighting:
            Interpreters.FightingInterpreter.FightingConsole().cmdloop()
        if MAIN_PLAYER.state == StateMachine.OpeningChest:
            Interpreters.ChestInterpreter.ChestConsole().cmdloop()
