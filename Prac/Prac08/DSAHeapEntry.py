# To be honest, I dont know what does DSAHeapEntry use for, so that I just write this file for demonstrating
# and not using it for any part of my program

class DSAHeapEntry:
    
    def __init__(self, priority = None, vAlue = object):
        self.priority = priority
        self.vAlue = vAlue

# getter and setter for adding validation logic around setting and getting values
    
    def __getter__(self, vAlue): 
        return self.vAlue

    def __setter__(self, x):
        self.vAlue = x 
