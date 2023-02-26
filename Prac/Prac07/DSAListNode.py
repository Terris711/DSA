# Update DSADoubledList to store both key and value of hash table

class DSANode():

    def __init__(self, data1, data2, pointer = None, previous = None):
        self.data1 = data1          # Consider as key in hashtable
        self.data2 = data2          # Consider as value in hashtable
        self.pointer = pointer # point to the next node
        self.previous = previous # point to the previous node

    def getData1(self):
        return self.data1

    def getData2(self):
        return self.data2

