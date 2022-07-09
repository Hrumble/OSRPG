from WorldRegistry import *
from Biome import *

BIOMES = []
MAP = []

#Biomes# name, position, radius, entities, level
BIOMES.append(Biome("Starter Plains", [0, 0], 10, ["slime", "spider", "wolf", "wandering_trader"], 0, 2))
BIOMES.append(Biome("Shady Forest", [0, -20], 10, ["mushroom_warrior", "slime"], 2, 5))
BIOMES.append(Biome("Dry Dry Desert", [20, 0], 10, ["wolf"], 4, 6))




