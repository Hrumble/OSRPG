from Registries.Registry import ENTITY_REGISTRY
from Entities.Enemy import Enemy

# ENTITY_REGISTRY.AddToRegistry(Enemy("example_enemy", "Example Enemy", base_health, base_damage))

ENTITY_REGISTRY.AddToRegistry(Enemy("slime", "Slime", 10, 2))
ENTITY_REGISTRY.AddToRegistry(Enemy("spider", "Spider", 8, 3))
ENTITY_REGISTRY.AddToRegistry(Enemy("wolf", "Wolf", 5, 5))
ENTITY_REGISTRY.AddToRegistry(Enemy("fierce_eagle", "Fierce Eagle", 10, 6))
ENTITY_REGISTRY.AddToRegistry(Enemy("mushroom_warrior", "Mushroom Warrior", 6, 3))
ENTITY_REGISTRY.AddToRegistry(Enemy("desert_spider", "Desert Spider", 10, 4))
ENTITY_REGISTRY.AddToRegistry(Enemy("angry_log", "Angry Log", 17, 6))
ENTITY_REGISTRY.AddToRegistry(Enemy("angry_cacti", "Angry Cacti", 12, 7))