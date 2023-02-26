# Hash table using seperate chaining

from checkPrime import isPrime
from nextPrime import nextPrime
from DSADoubledlist import DSADoubledList
from DSAListNode import DSANode
import numpy as np

class HashEntry:


    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        
    def getValue(self):
        return self.value

    def getKey(self):
        return self.key


class HashTable(object):
    
    def __init__(self, size):

        if isPrime(size):
                self.size = size
        else:
                self.size = nextPrime(size)

        self.space = np.empty(self.size, dtype = object)

        for i in range(self.size):
                self.space[i] = DSADoubledList()

        self.count = 0

    def hash(self, key, size):
        return key % size


    def put(self, key, data):
        
        hashValue = self.hash(key, len(self.space))
        self.space[hashValue].insertLast(key, data)
        self.count += 1

    def rehash(self, oldValue, size):
        return (oldValue + 1) % size

    def get(self, key):
        hashValue = self.hash(key, len(self.space))
        getKey = self.space[hashValue].searchKey(key)
        return getKey

    def remove(self, key):
        hashValue = self.hash(key, len(self.space))
        self.space[hashValue].removeMiddle(key)
        self.count -= 1

    def hashdisplay(self):
        print("Key\tLinked List")
        for i in range(1,self.size):
                print(i, "\t", end = "")
                self.space[i].listdisplay()


    def __getitem__(self, key):
        return self.key

    def __setitem__(self, key, data):
        return self.put(self.key.data)
    
