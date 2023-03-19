import copy

# A List of entities/items
class Registry:
    def __init__(self):
        self.list = []

    def AddToRegistry(self, item):
        self.list.append(item)

    # Returns a copy of an item class based on it's ID
    def GetByID(self, ID):
        for registeredItem in self.list:
            if registeredItem.ID == ID:
                return copy.deepcopy(registeredItem)
        return False
