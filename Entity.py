class Entity:
    def __init__(self, id, name):
        self._id = id
        self.name = name
        self.xPos = 0
        self.yPos = 0

    @property
    def position(self):
        return [self.xPos, self.yPos]

    @property
    def ID(self):
        return self._id

    def Die(self):
        print(f"{self.name} Died")

    def Interact(self):
        """
            Function is called when player is on the same tile as entity
        """
        pass

    def OnSpawn(self):
        """
            Function is called when entity spawns in the biome
        """
        pass
