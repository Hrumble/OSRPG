from Items.Item import *

class ConsumableItem(Item):
    def __init__(self, id, name, value, healthModifier, craftable=False):
        super().__init__(id, name, value, craftable)
        self.modifier = healthModifier
        self.type = "Consumable"

    def Consume(self, player):
        player.currentHealth += int(self.modifier * player.maxHealth)
        if player.currentHealth > player.maxHealth:
            player.currentHealth = player.maxHealth
        print(f"[PLAYER] Consumed {self.name} - HP is now {player.currentHealth}")
        player.inventory.RemoveFromContainer(self.ID)
        self.OnConsumed()

    def ExtraInfo(self):
        print(f"Restores {self.modifier * 100}% of HP")

    def OnConsumed(self):
        pass