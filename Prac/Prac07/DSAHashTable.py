# Hashtable using linear probing

from checkPrime import isPrime
from nextPrime import nextPrime
import numpy as np

class DSAHashTable(object):

    def __init__(self, size):
        
        if isPrime(size):
                self.size = size
        else:
                self.size = nextPrime(size)
        
# Dont use the same variable self.key and self.value because it will be overlap with linked list 
        self.space = np.array([None]*self.size) # Store key 
        self.data = np.array([None]*self.size) # Store value
        self.state = np.zeros(self.size)
        # Legend:
        # 0: free
        # 1: used
        #-1: previously-used

        self.count = 0

# Hash function to convert the key to an int
    def hash(self, key, size):
        return key % size

    def rehash(self, preHash, newSize):
        return (preHash + 1) % newSize

    def shouldResize(self):
        # if the table is being filled up >= 70%  ==> shoule be resized
        if (self.count / self.size) > 0.70:
                self._resize(self.size)

    def _resize(self, size):
        
        self.count = 0
        oldKeys = self.space
        oldValues = self.data

        self.size = self.size * 2

        if not isPrime(self.size):
                self.size = nextPrime(self.size)

        self.space = np.array([None] * self.size)
        self.data = np.array([None] *self.size)
        self.state = np.zeros(self.size)

        for i in range(len(oldValues)):
                if oldValues[i] is not None:
                        self.put(oldKeys[i], oldValues[i])


    def put(self, key, data):
        
        hashValue = self.hash(key, len(self.space))

        # If not used
        if self.space[hashValue] == None:
                self.space[hashValue] = key
                self.data[hashValue] = data
                self.state[hashValue] = 1

        else:
        # If used already
                if self.space[hashValue] == key:
                        self.data[hashValue] = data
                else:
                        nextSpace = self.rehash(hashValue, len(self.space))
                        while self.space[nextSpace] != None and self.space[nextSpace] != key:
                                nextSpace = self.rehash(nextSpace, len(self.space))
                        
                        if self.space[nextSpace] == None:
                                self.space[nextSpace] = key
                                self.data[nextSpace] = data
                                self.state[nextSpace] = 1
                        else:
                                self.data[nextSpace] = data
                                self.state[nextSpace] = 1
        self.count += 1
        self.shouldResize()

     
    def hasKey(self):
        pass

    def get(self, key):

        startSpace = self.hash(key, len(self.space))
        data = None
        stop = False
        found = False
        position = startSpace

        while self.space[position] != 0 and not found and not stop:
                if self.space[position] == key:
                        found = True
                        data = self.data[position]

                else:
                        position = self.rehash(position, len(self.space))
                        if position == startSpace:
                                stop = True
        return data


    def remove(self, key):
        
        value = self.hash(key, len(self.space))

        for i in range(self.size):
                if self.space[i] == key:
                        self.space[i] = None
                        self.data[i] = None
                        self.state[i] = -1
        self.count -= 1


    def display(self):
        
        print("Entry \t Key \t Value \t\t State \t")

        for i in range(1,self.size):
                print(i, "\t", self.space[i], "\t", self.data[i], "\t\t", self.state[i])
        print()

    def __getitem__(self, key):
        return self.key

    def __setitem__(self, key, data):
        return self.put(self.key.data)




