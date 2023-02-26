import numpy as np

class DSAHeap:
   
   def __init__(self):
        self.heapArr = np.empty(0, dtype = int)
        self.count= 0

   def isEmpty(self):
        return self.count == 0

   def getCount(self):
        return self.count

   def trickleUp(self, heapArr,index):

        parentIdx = (index - 1) // 2
        if index > 0:
                if self.heapArr[index] > self.heapArr[parentIdx]:
                        temp = self.heapArr[index] 
                        self.heapArr[index] = self.heapArr[parentIdx]
                        self.heapArr[parentIdx] = temp
                        self.trickleUp(self.heapArr,parentIdx)

    
   def add(self, value):
         newHeap = np.empty(self.count + 1, dtype = int)
         for i in range(len(self.heapArr)):
             newHeap[i] = self.heapArr[i] # copy data from heap to new heap
         newHeap[self.count] = value
         self.heapArr = newHeap
         self.count += 1
         self.trickleUp(self.heapArr, self.count - 1)
   

   def trickleDown(self, heapArr, index, count):
        leftIdx = (index * 2) + 1
        rightIdx = leftIdx + 1
        if leftIdx < self.count:
                largeIdx = leftIdx
                if rightIdx < self.count:
                        if self.heapArr[leftIdx] < self.heapArr[rightIdx]:
                                largeIdx = rightIdx
                if self.heapArr[largeIdx] > self.heapArr[index]:
                        temp = self.heapArr[largeIdx]
                        self.heapArr[largeIdx] = self.heapArr[index]
                        self.heapArr[index] = temp
                        self.trickleDown(self.heapArr,largeIdx,self.count)

   def getMaxValue(self):
        return self.heapArr[0]

   def getMaxChild(self, index):
        if (index * 2) + 1 < self.count:
                return index * 2 + 1
        else:
                if self.heapArr[i * 2] > self.heapArr[(i * 2) + 1]:
                        return i * 2
                else:
                        return (i * 2) + 1

   def remove(self):
        if self.isEmpty():
                print("Heap is empty")
        else: 
            delNode = self.heapArr[0]
            temp = self.heapArr[0]
            self.heapArr[0] = self.heapArr[self.count - 1]
            *self.heapArr, _ = self.heapArr
            self.count -= 1
            self.trickleDown(self.heapArr,0,self.count)
            return delNode
            
   def heapify(self, heapArr, count):
# Start at last non-leaf node, go backwards
        for i in range((self.count // 2) - 1, 0, -1):
                self.trickleDown(self.heapArr, i, self.count)
        return self.heapArr

   def heapSort(self, heapArr, count):
        self.heapArr = self.heapify(self.heapArr, self.count)
        for i in range (self.count - 1, 0, -1):
                temp = self.heapArr[0]
                self.heapArr[0]  = self.heapArr[i]
                self.heapArr[i] = temp
                self.trickleDown(self.heapArr[0:i], 0, i)

        return self.heapArr

   def display(self):
        for i in self.heapArr:
                print(i)


  
