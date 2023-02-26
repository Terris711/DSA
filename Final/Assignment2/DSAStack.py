import numpy as np

class DSAStack():
    def __init__(self, capacity):
        self._capacity = capacity
        self._arr = np.empty(self._capacity, dtype = object)
        self._count = 0

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._arr) - 1

    def push(self, item): #add item
        if self.isFull():
            raise Exception('Stack Overflow')
        else:
            self._arr[self._count] = item
            self._count += 1

    def pop(self): #remove item
        if self.isEmpty():
            raise Exception('Stack Underflow')
        else:
            item = self._arr[self._count-1]
            self._count -= 1
            return item

    def getCount(self):
        return self._count

    def top(self): #item location
        if self.isEmpty():
            raise Exception('Stack Underflow')
        return self._arr[self._count-1]


    def display(self):
        if self.isEmpty():
                print("Stack is empty!")
        else:
                i = self._count - 1
                while i >= 0:
                    print(self._arr[i])
                    i -= 1;
                        

    def __str__(self):
        return str(self._arr)

#S = DSAStack(10)

#S.push("A")
#S.push("B")
#S.push("C")
#S.push("D")


#S.display()

#print(S.getCount())

    
    
