from Entities.Player import *
from Registries.WorldLoc import *

# Set up player and default inventory
MAIN_PLAYER = Player("player", "Main Player", 10, 1)
MAIN_PLAYER.inventory.AddToContainer("sturdy_iron_sword")
MAIN_PLAYER.inventory.AddToContainer("wolf_fang", 3)
MAIN_PLAYER.inventory.AddToContainer("big_potion", 2)
MAIN_PLAYER.inventory.AddToContainer("apple", 4)
MAIN_PLAYER.inventory.AddToContainer("leather_helmet")
MAIN_PLAYER.inventory.AddToContainer("fire_chestplate")


# Updates player current biome and checks for entities on player's position
def PositionUpdate():
    MAIN_PLAYER.UpdateStats()
    for biome in BIOMES:
        if biome.CheckForPlayer(MAIN_PLAYER.position):
            if MAIN_PLAYER.currentBiome != biome:
                print(f"[WORLD] Player has entered the {biome.name} of Level {biome.level}")
                MAIN_PLAYER.currentBiome = biome
    for entity in MAIN_PLAYER.currentBiome.map:
        if MAIN_PLAYER.position == entity.position and not MAIN_PLAYER.isInteracting:
            # Each entity has its own interact function
            entity.Interact(MAIN_PLAYER)
    if MAIN_PLAYER.debug:
        print([f"{entity.name} : {entity.position}" for entity in MAIN_PLAYER.currentBiome.map])
