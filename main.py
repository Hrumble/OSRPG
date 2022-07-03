from WorldRegistry import *
from PlayerManager import *

def start():
    ENTITY_REGISTRY.GetByID("slime").DropLoot(MAIN_PLAYER)
    print(MAIN_PLAYER.inventory.DisplayInventory())

start()
