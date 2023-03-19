import FightingInterpreter
import TradingInterpreter
from PlayerManager import *
from Player import StateMachine
import BasicInterpreter
from Fight import *
from WorldRegistry import *
import FightingInterpreter


def StartGame():
    while True:

        PositionUpdate()
        if MAIN_PLAYER.state == StateMachine.Basic:
            BasicInterpreter.BasicConsole().cmdloop()
        if MAIN_PLAYER.state == StateMachine.Trading:
            TradingInterpreter.TradingConsole.cmdloop()
        if MAIN_PLAYER.state == StateMachine.Fighting:
            FightingInterpreter.FightingConsole().cmdloop()
