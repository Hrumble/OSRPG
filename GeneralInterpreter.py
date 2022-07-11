from PlayerManager import *

def equip(inventoryIndex):
    inventoryIndex = int(inventoryIndex)
    MAIN_PLAYER.Equip(MAIN_PLAYER.inventory.inventory[inventoryIndex].item)

def unequip(slot):
    MAIN_PLAYER.Unequip(slot)

def craft(id):
    MAIN_PLAYER.Craft(id)

def use(index):
    index = int(index)
    item = MAIN_PLAYER.inventory.inventory[index].item
    if isinstance(item, ConsumableItem):
        item.Consume(MAIN_PLAYER)
    else:
        print("[SYSTEM] You can\'t consume that")

def info(id):
    from WorldRegistry import ITEM_REGISTRY
    ITEM_REGISTRY.GetByID(id).Info()
