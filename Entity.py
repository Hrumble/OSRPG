class Entity:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    @property
    def ID(self):
        return self._id

    def Die(self):
        print(f"{self.name} Died")
