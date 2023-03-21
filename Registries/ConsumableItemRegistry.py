from Registries.Registry import ITEM_REGISTRY
from Items.ConsumableItem import ConsumableItem

# ITEM_REGISTRY.AddToRegistry(ConsumableItem("example_consumable", "Example Consumable", value, health_modifier, craftable))

ITEM_REGISTRY.AddToRegistry(ConsumableItem("apple", "Apple", 2, 0.1))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("pie", "Pie", 5, 0.15))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("small_potion", "Small Potion", 10, 0.2))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("medium_potion", "Medium Potion", 20, 0.4, True))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("big_potion", "Big Potion", 40, 0.6, True))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("large_potion", "Large Potion", 60, 0.8, True))
ITEM_REGISTRY.AddToRegistry(ConsumableItem("extreme_potion", "Extreme Potion", 100, 1, True))
