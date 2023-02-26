from DSAListNode import DSANode

class DSALinkedList():
    
    def __init__(self):
        self.head = None

    def display(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.key, end = "-->")
            curNode = curNode.pointer
        print()

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
        if self.isEmpty():
            self.head = DSANode(key)
        else:
            newNode = DSANode(key, self.head)
            self.head = newNode

    def insertLast(self, key):
        if self.isEmpty():
            self.head = DSANode(key)
        else:
            newNode = DSANode(key)
            curNode = self.head
            while curNode.pointer is not None:
                curNode = curNode.pointer
            curNode.pointer = newNode
     
    def insertMiddle(self,key):
        newNode = DSANode(key)
        if self.isEmpty():
            self.head = DSANode(key)
        else:
            curNode = self.head
            midNode = self.head
            while curNode.pointer is not None and curNode.pointer.pointer is not None:
                curNode = curNode.pointer.pointer
                midNode = midNode.pointer
            newNode.pointer = midNode.pointer
            midNode.pointer = newNode
            
            
    def peekFirst(self):
        return self.head.key

    def peekLast(self):
        peek = self.head
        while peek.pointer is not None:
            peek = peek.pointer
        return peek.key

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
            # Tracing back to the second last element then set its pointer as NULL
            curNode = self.head
            preNode = None
            while curNode is not None:
                preNode = curNode
                curNode = curNode.pointer
            delNode = curNode.key
            preNode.pointer = None
            return delNode

            #curNode = self.head
            #while curNode.pointer.pointer is not None:
            #    curNode = curNode.pointer
            #lastNode = curNode.pointer
            #curNode.pointer = None
            #lastNode.key = None

    def removeMiddle(self):
       pass        
