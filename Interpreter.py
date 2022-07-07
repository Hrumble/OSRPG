import TradingInterpreter
from PlayerManager import *
from Player import StateMachine
import BasicInterpreter
from WorldRegistry import *

def StartGame():
    ENTITY_REGISTRY.GetByID("wandering_trader").Interact(MAIN_PLAYER)
    MAIN_PLAYER.money = 1290
    MAIN_PLAYER
    while True:
        playerInput = input("> ").split()
        func = playerInput[0]
        command = func + "("
        if not len(playerInput) < 1:
            args = playerInput[1:]
            for i in range(len(args)):
                if i == 0:
                    command += args[i]
                else:
                    command += ", " + args[i]
        command += ")"

        if MAIN_PLAYER.state == StateMachine.Basic:
            BasicInterpreter.interpret(command)
        if MAIN_PLAYER.state == StateMachine.Trading:
            TradingInterpreter.interpret(command)
