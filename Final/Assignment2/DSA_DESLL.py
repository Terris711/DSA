from DSAListNode import DSANode

class DSA_DESLL():
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def display(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.key, end = "-->")
            curNode = curNode.pointer
        print()

    def __iter__(self):
        curNode = self.head
        while curNode is not None:
            yield curNode.key
            curNode = curNode.pointer
        
    def isEmpty(self):
        return self.head == None

    def getSize(self):
        count = 0
        curNode = self.head
        while curNode is not None:
            count += 1
            curNode = curNode.pointer
        return count

    def insertFirst(self, key):
        newNode = DSANode(key)
        if self.isEmpty():
            self.tail = DSANode(key)
        else:
            newNode.pointer = self.head
        self.head = newNode
                                    
            

    def insertLast(self, key):
        newNode = DSANode(key)

        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.pointer = newNode
        self.tail= newNode         
            
    
    
    def peekFirst(self):
        return self.head.key

    def peekLast(self):
        curNode = self.head
        while curNode.pointer is not None:
            curNode = curNode.pointer
        return curNode.key

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            delNode = self.head.key
            self.head = self.head.pointer
        return delNode


#L = DSA_DESLL()

#L.insertLast(11)
#L.insertFirst(9)

#print(L.peekLast())

#L.display()
