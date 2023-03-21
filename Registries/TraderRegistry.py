from Registries.Registry import ENTITY_REGISTRY
from Entities.Trader import Trader

# ENTITY_REGISTRY.AddToRegistry(Trader("example_trader", "Example Trader", resell_rate))

ENTITY_REGISTRY.AddToRegistry(Trader("wandering_trader", "Wandering Trader", 1.5))
ENTITY_REGISTRY.AddToRegistry(Trader("forest_trader", "Forest Trader", 1.7))
