from Registries.Registry import ITEM_REGISTRY
from Items.ArmorItem import ArmorItem

# ITEM_REGISTRY.AddToRegistry(ArmorItem("example_armor", "Example Armor", value, protection, slot))

ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_helmet", "Leather Helmet", 1, 1, ArmorItem.headSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_chestplate", "Leather Chestplate", 1, 2, ArmorItem.chestSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_leggings", "Leather Leggings", 1, 1, ArmorItem.legSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("leather_boots", "Leather Helmet", 1, 1, ArmorItem.feetSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("mushroom_cap", "Mushroom Cap", 3, 2, ArmorItem.headSlot))
ITEM_REGISTRY.AddToRegistry(ArmorItem("fire_chestplate", "Fire Chestplate", 100, 10, ArmorItem.chestSlot))
