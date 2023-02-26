import numpy as np 
from DSAQueue import DSAQueue

class DSAShufflingQueue(DSAQueue):
    def __init__(self, capacity):
        super().__init__(capacity)
        self._front = 0
        self._rear = -1

    def enqueue(self, item):
        super().enqueue(item)

    def dequeue(self):
        super().dequeue()

    def shuffling(self):
        q = self._arr[0]
        for i in range(self._rear):
            self._arr[i] = self._arr[i+1]
        return q 
        

