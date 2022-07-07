from Player import *
from WorldRegistry import *

MAIN_PLAYER = Player("player", "Main Player", 10, 1)
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("sturdy_iron_sword"))
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("wolf_fang"), 76)
