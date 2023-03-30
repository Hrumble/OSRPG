from Registries.Registry import ITEM_REGISTRY
from Items.WeaponItem import WeaponItem

# ITEM_REGISTRY.AddToRegistry(WeaponItem("example_weapon", "Example Weapon", value, damage, craftable))

ITEM_REGISTRY.AddToRegistry(WeaponItem("fractured_dagger", "Fractured Dagger", 1, 1))
ITEM_REGISTRY.AddToRegistry(WeaponItem("rusty_copper_Dagger", "Rusty Copper Dagger", 3, 2))
ITEM_REGISTRY.AddToRegistry(WeaponItem("sharp_dagger", "Sharp Dagger", 7, 3))
ITEM_REGISTRY.AddToRegistry(WeaponItem("vine_whip", "Vine Whip", 25, 7, True))
ITEM_REGISTRY.AddToRegistry(WeaponItem("moonlight_swordnata", "Moonlight Swordnata", 100, 30))
ITEM_REGISTRY.AddToRegistry(WeaponItem("wolf_sword", "Wolf Sword", 30, 8))
ITEM_REGISTRY.AddToRegistry(WeaponItem("sturdy_iron_sword", "Sturdy Iron Sword", 14,  5))
ITEM_REGISTRY.AddToRegistry(WeaponItem("slicer", "Slicer", 12, 4, True))
ITEM_REGISTRY.AddToRegistry(WeaponItem("hidden_slicer", "Hidden Slicer", 28, 7))
ITEM_REGISTRY.AddToRegistry(WeaponItem("fiery_sword", "Fiery Sword", 100, 10, True))