import copy

# A List of entities/items
class Registry:
    def __init__(self, name):
        self.list = []
        self.name = name

    def AddToRegistry(self, item):
        self.list.append(item)

    # Returns a copy of an item class based on it's ID
    def GetByID(self, ID):
        for registeredItem in self.list:
            if registeredItem.ID == ID:
                return copy.deepcopy(registeredItem)
        print(f"{ID} does not exist in the {self.name}")
        return False

    def GetName(self, ID):
        for registeredItem in self.list:
            if registeredItem.ID == ID:
                return registeredItem.name
        print(f"{ID} does not exist in the {self.name}")
        return False

    def ListItems(self):
        for item in self.list:
            print(f"{item.name} | {item.ID} : type({item.type})")
