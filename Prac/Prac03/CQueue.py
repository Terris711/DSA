from DSAQueue import DSAQueue
import numpy as np

class DSACircularQueue(DSAQueue):
    
    def __init__(self, capacity):
        super().__init__(capacity)
        self._front = -1
        self._rear = -1 
        
    
    def enqueue(self, item): 
# In circular queue, the element is always added from rear
        if self._rear - self._front == self._capacity - 1 or self._front - self._rear == 1:
            raise Exception ('The circular queue is already full')
        elif (self._front == -1):
            self._front = 0
            self._rear = 0
            self._arr[self._rear] = item
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._arr[self._rear] = item
            print('The item is added is: ', item)

# In circular queue, the element is always deleted from front
    def dequeue(self):
        if self._front == -1:
            raise Exception ('The circular queue is empty')
        else:
            if  self._front == self._rear:
                q = self._arr[self._front]
                self._front = -1
                self._rear = -1
                print('The item is removed is: ', q)
            
            else:
                q = self._arr[self._front]
                self._front = (self._front + 1) % self._capacity
                print('The item is removed is: ', q)
            
            
            

