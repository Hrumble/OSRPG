from Biome import *

BIOMES = []

#Biomes# name, position, radius, entities, level, effective

BIOMES.append(Biome("Starter Plains", [0, 0], 10,
                    ["slime", "spider", "wolf", "wandering_trader", "basic_chest"],
                    0, 60))
BIOMES.append(Biome("Shady Forest", [0, -20], 10,
                    ["mushroom_warrior", "slime", "forest_trader", "angry_log"],
                    2, 90))
BIOMES.append(Biome("Dry Dry Desert", [20, 0], 10,
                    ["desert_spider", "fierce_eagle", "angry_cacti"],
                    4, 100))




