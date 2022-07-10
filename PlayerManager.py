from Player import *
from WorldRegistry import *
from WorldLoc import *

MAIN_PLAYER = Player("player", "Main Player", 10, 1)
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("sturdy_iron_sword"))
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("wolf_fang"), 3)
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("big_potion"), 2)
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("apple"), 4)
MAIN_PLAYER.inventory.AddToContainer(ITEM_REGISTRY.GetByID("leather_helmet"))


def PositionUpdate():
    for biome in BIOMES:
        if biome.CheckForPlayer(MAIN_PLAYER.position):
            MAIN_PLAYER.currentBiome = biome
    for entity in MAIN_PLAYER.currentBiome.map:
        if MAIN_PLAYER.position == entity.position and not MAIN_PLAYER.isInteracting:
            entity.Interact(MAIN_PLAYER)
    #print([entity.position for entity in MAIN_PLAYER.currentBiome.map])
    #print([entity.name for entity in MAIN_PLAYER.currentBiome.map])