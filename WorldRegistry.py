import ArmorItem
from Registry import *
from Item import *
from Enemy import *
from WeaponItem import *
from ArmorItem import *
from LootTable import *
from Trader import *

ITEM_REGISTRY = Registry()
ENTITY_REGISTRY = Registry()

def Items():
    return ITEM_REGISTRY
def Entities():
    return ENTITY_REGISTRY


#Items#
ITEM_REGISTRY.AddToRegistry(Item("apple", "Apple"))
ITEM_REGISTRY.AddToRegistry(Item("stone", "Stone"))
ITEM_REGISTRY.AddToRegistry(Item("slimeball", "SlimeBall", 6))
ITEM_REGISTRY.AddToRegistry(Item("spider_eye", "Spider Eye", 7))
ITEM_REGISTRY.AddToRegistry(Item("fur", "Fur", 5))
ITEM_REGISTRY.AddToRegistry(Item("wolf_fang", "Wolf Fang", 10))
ITEM_REGISTRY.AddToRegistry(Item("claw", "Claw", 14))

#Weapons#
ITEM_REGISTRY.AddToRegistry(WeaponItem("wooden_sword", "Wooden Sword", 1, 2))
ITEM_REGISTRY.AddToRegistry(WeaponItem("rusty_copper_sword", "Rusty Copper Sword", 1, 3))
ITEM_REGISTRY.AddToRegistry(WeaponItem("moonlight_swordnata", "Moonlight Swordnata", 50, 30))
ITEM_REGISTRY.AddToRegistry(WeaponItem("sturdy_iron_sword", "Sturdy Iron Sword", 5,  5))

#Armor#
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_helmet", "Leather Helmet", 1, 1, ArmorItem.headSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_chestplate", "Leather Chestplate", 1, 2, ArmorItem.chestSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_leggings", "Leather Leggings", 1, 1, ArmorItem.legSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_boots", "Leather Helmet", 1, 1, ArmorItem.feetSlot))

#Loot Tables#
slime_table = LootTable(["slimeball", "apple"], [2, 1], [100, 25])
spider_table = LootTable(["spider_eye"], [1], [50])
wolf_table = LootTable(["fur", "wolf_fang", "claw"], [1, 1, 1], [90, 20, 10])

# Entities#
ENTITY_REGISTRY.AddToRegistry(Enemy("slime", "Slime", 10, 2, 3, slime_table))
ENTITY_REGISTRY.AddToRegistry(Enemy("spider", "Spider", 8, 3, 2, spider_table))
ENTITY_REGISTRY.AddToRegistry(Trader("wandering_trader", "Wandering Trader", 1.5, ["slimeball", "wolf_fang"], [65, 5]))

