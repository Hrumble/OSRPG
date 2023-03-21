from Registries.WorldRegistry import *
import random


class Biome:
    def __init__(self, name, position, radius, entitiesID, level, entityEffective):
        self.name = name
        self.position = position
        self.radius = radius
        self.entitiesID = entitiesID
        self.level = level
        self.wasPlayerIn = False
        self.map = []
        self.entityEffective = entityEffective

    @property
    def square(self):
        top = [self.position[0] - self.radius, self.position[1] + self.radius]
        bottom = [self.position[0] + self.radius, self.position[1] - self.radius]
        return [top, bottom]

    def CheckForPlayer(self, playerPos):
        if (playerPos[0] > self.square[0][0] and playerPos[1] < self.square[0][1]) and (playerPos[0] < self.square[1][0] and playerPos[1] > self.square[1][1]):
            if not self.wasPlayerIn:
                self.Populate(self.entityEffective)
            self.wasPlayerIn = True
            return True
        else:
            self.wasPlayerIn = False
            return False

    def CheckAt(self, position):
        for entity in self.map:
            if entity.position == position:
                return entity
        return False

    def Populate(self, effective):
        self.BeforePopulate()
        mobID = []
        for i in range(effective):
            mobID.append(random.choice(self.entitiesID))
        for id in mobID:
            mob = ENTITY_REGISTRY.GetByID(id)
            mobPos = self.GetRandomPosition()
            mob.xPos = mobPos[0]
            mob.yPos = mobPos[1]
            if isinstance(mob, Enemy):
                randLevel = random.randint(self.level - 1, self.level + 1)
                if randLevel < 0: randLevel = 0
                mob.level = randLevel
            self.map.append(mob)
            mob.OnSpawn()
        for entity in self.map:
            entity1pos = entity.position
            for entity2 in self.map:
                if entity2.position == entity1pos:
                    self.MoveEntity(random.choice([entity, entity2]), self.GetRandomPosition())
        self.AfterPopulate()

    def BeforePopulate(self):
        """
                    Function is called right before the biome has been populated
        """
        pass

    def AfterPopulate(self):
        """
            Function is called right after the biome has been populated
        """
        pass

    def KillEntity(self, entity):
        self.map.remove(entity)

    def MoveEntity(self, entityToMove, position):
        moved = False
        while not moved:
            for entity in self.map:
                if entity.position == position:
                    position += [random.randint(-1, 1), random.randint(-1, 1)]
                    continue
            entityToMove.xPos = position[0]
            entityToMove.yPos = position[1]
            moved = True

    def GetRandomPosition(self):
        xRange = [self.position[0] - self.radius, self.position[0] + self.radius]
        yRange = [self.position[1] - self.radius, self.position[1] + self.radius]
        randX = random.randint(xRange[0], xRange[1])
        randY = random.randint(yRange[0], yRange[1])
        return [randX, randY]
