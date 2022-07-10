from WorldRegistry import *
from Biome import *

BIOMES = []

#Biomes# name, position, radius, entities, level, effective
BIOMES.append(Biome("Starter Plains", [0, 0], 10, ["slime", "spider", "wolf", "wandering_trader"], 0, 15))
BIOMES.append(Biome("Shady Forest", [0, -20], 10, ["mushroom_warrior", "slime", "forest_trader", "angry_log"], 2, 18))
BIOMES.append(Biome("Dry Dry Desert", [20, 0], 10, ["wolf"], 4, 6))




