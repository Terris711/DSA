import numpy as np

class DSAQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._arr = np.empty(self._capacity, dtype = object)
        self._front = 0
        self._rear = -1
        self._count = 0
        

    def isEmpty(self):
        return len(self._arr) == 0

    def isFull(self):
        return len(self._arr) == self._count

    def  findCount(self):
        return self._count

    def enqueue(self, item):  #Adding more item to the list
        if self.isFull():
            raise Exception ('Queue is already full')
        else:
            self._rear += 1
            self._arr[self._rear] = item
            self._count += 1
            print('The value is added to the queue is: ', item)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is already empty')
        else:
            
            print('The item is removed is :', self._arr[self._front])
            self._front += 1 
            self._count -= 1
         
