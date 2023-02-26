from DSAListNode import DSANode
from DSADoubledlist import DSADoubledList

class DSAStack(DSADoubledList):
    def __init__(self):
        super().__init__()
        
    def isEmpty(self):
        super().isEmpty()

    def push(self, item): #add item
        super().insertFirst(item) 

    def pop(self): #remove item
        return super().removeFirst()

    def top(self): #item location
       return super().peekFirst()

    def __iter__(self):
        return super().__iter__()
    
#S = DSAStack()
#S.push(3)
#S.push(4)
#S.push(5)
#print(S.pop()) 
