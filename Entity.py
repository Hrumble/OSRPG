class Entity:
    def __init__(self, id, name, health, damage):
        self._id = id
        self.name = name
        self.health = health
        self.damage = damage

    @property
    def ID(self):
        return self._id

    def Die(self):
        print(f"{self.name} Died")