from DSAListNode import DSANode

class DSADoubledList():
    
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
        print(count)

    def insertFirst(self, key):
        if self.isEmpty():
            self.head = DSANode(key)
        else:
            newNode = DSANode(key)
            newNode.pointer = self.head
            if self.head is not None:
                self.head.previous = newNode
            self.head = newNode
            
            

    def insertLast(self, key):
        newNode = DSANode(key)
        newNode.pointer = None

        if self.head is None:
            newNode.previous = None
            self.head = newNode 
        else: 
            lastNode = self.head
            while lastNode.pointer is not None:
                lastNode = lastNode.pointer
            lastNode.pointer = newNode
            newNode.previous = lastNode
         
            
    
    def insertMiddle(self,key):
        pass

    def peekFirst(self):
        return self.head.key

    def peekLast(self, node):
        node = node.head
        while node.pointer is not None:
            node = node.pointer
        return node.key

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            delNode = self.head.key
            self.head = self.head.pointer
        return delNode

    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            curNode = self.head
            # Find  the last node            
            while curNode.pointer is not None: 
                curNode = curNode.pointer
            
            if curNode == self.head:
            #when only one node left, remove head
                self.head = None
            else:                       
                curNode.previous.pointer= None
            

    def removeMiddle(self):
        pass        
