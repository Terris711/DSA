class Vertex():
    def __init__(self, label = None, value = None, index = None):
        self.label = label
        self.value = value
        self.index = index
        #self.visited = 0

    def __str__(self):
        return ("Vertex: ", self.label + " Value: " + self.value)
