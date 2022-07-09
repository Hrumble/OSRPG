import time
from Player import StateMachine

class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def PlayerAttack(self):
        print(f"[WORLD] {self.player.name} dealt {self.player.damage} damage to {self.enemy.name}")
        self.enemy.currentHealth -= self.player.damage
        time.sleep(1)
        if self.enemy.currentHealth <= 0:
            self.enemy.Die(self.player)
            self.player.state = StateMachine.Basic
            self.player.isInteracting = False
            self.player.currentBiome.KillEntity(self.enemy)
            self.player.currentArmorHealth = self.player.maxArmorHealth
            return
        self.EnemyAttack()

    def EnemyAttack(self):
        print(f"[WORLD] {self.enemy.name} dealt {self.enemy.damage} damage to {self.player.name}")
        self.player.TakeDamage(self.enemy.damage)
        if self.player.currentHealth <= 0:
            self.player.Die()