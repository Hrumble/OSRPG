from Item import *

class ConsumableItem(Item):
    def __init__(self, id, name, value, healthModifier, craftable = False):
        super().__init__(id, name, value, craftable)
        self.modifier = healthModifier

    def Consume(self, player):
        print(f"[PLAYER] Consumed {self.name} - HP is now {player.currentHealth}")
        player.currentHealth += int(self.modifier * player.maxHealth)
        if player.currentHealth > player.maxHealth:
            player.currentHealth = player.maxHealth
        player.inventory.RemoveFromContainer(self)