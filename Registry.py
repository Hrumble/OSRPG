import copy

class Registry:
    def __init__(self):
        self.list = []

    def AddToRegistry(self, item):
        self.list.append(item)

    def GetByID(self, ID):
        for registeredItem in self.list:
            if registeredItem.ID == ID:
                return copy.deepcopy(registeredItem)
        return False
