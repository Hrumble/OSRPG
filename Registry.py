import copy

class Registry:
    def __init__(self):
        self.list = []

    def AddToRegistry(self, item):
        self.list.append(item)

    def Get(self, item):
        for registeredItem in self.list:
            if registeredItem.ID == item.ID:
                return copy.deepcopy(registeredItem)
        return False
