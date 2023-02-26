class DSANode():
    def __init__(self, key = None, pointer = None, previous = None):
        self.key = key
        self.pointer = pointer # point to the next node
        self.previous = previous # point to the previous node

