from DSADoubledlist import DSADoubledList


class GraphVertex:
    
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.adjacent = DSADoubledList()
        self.adjacent.head = None
        self.visited = False

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        return self.adjacent

    def __iter__(self): # List all neighbor of vertex
        return self.adjacent.__iter__() # Recursive, repeat to return each neighbor in the list 


    def __str__(self):
        return ("Label: " + str(self.label) + " Value: " + str(self.value) + "\n")
