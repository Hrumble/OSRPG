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
        playerInput = input("> ").split()
        func = playerInput[0]
        command = func + "("
        if not len(playerInput) < 1:
            args = playerInput[1:]
            for i in range(len(args)):
                if i == 0:
                    command += "\"" + args[i] + "\""
                else:
                    command += ", " + "\"" + args[i] + "\""
        command += ")"
        if MAIN_PLAYER.state == StateMachine.Basic:
            BasicInterpreter.interpret(command)
        if MAIN_PLAYER.state == StateMachine.Trading:
            TradingInterpreter.interpret(command)
        if MAIN_PLAYER.state == StateMachine.Fighting:
            FightingInterpreter.interpret(command)
