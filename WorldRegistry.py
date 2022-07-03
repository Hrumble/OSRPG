from Registry import *
from Item import *
from Enemy import *
from WeaponItem import *
from ArmorItem import *
from LootTable import *

ITEM_REGISTRY = Registry()
ENTITY_REGISTRY = Registry()
CONSUMABLE_REGISTRY = Registry()

def Items():
    return ITEM_REGISTRY
def Entities():
    return ENTITY_REGISTRY


#Items#
ITEM_REGISTRY.AddToRegistry(Item("apple", "Apple"))
ITEM_REGISTRY.AddToRegistry(Item("stone", "Stone"))
ITEM_REGISTRY.AddToRegistry(Item("slimeball", "SlimeBall"))
ITEM_REGISTRY.AddToRegistry(Item("spider_eye", "Spider Eye"))

#Loot Tables#
slime_table = LootTable(["slimeball", "apple"], [2, 1], [100, 25])

# Entities#
ENTITY_REGISTRY.AddToRegistry(Enemy("slime", "Slime", 10, 2, 3, slime_table))

