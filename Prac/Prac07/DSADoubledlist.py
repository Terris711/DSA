# Update DSADoubledList to store both key and value of hash table


from DSAListNode import DSANode

class DSADoubledList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0 
    
    def getCount(self):
        return self.count

    
    def __iter__(self):
        curNode = self.head
        while curNode is not None:
            yield curNode.key
            curNode = curNode.pointer

    def listdisplay(self):
        curNode = self.head
        while curNode is not None:
                print(curNode.data1, curNode.data2, "--->", end = " ")
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
        print(count)

    def insertFirst(self, newValue1, newValue2):
        
        newNode = DSANode(newValue1, newValue2)
        newNode.pointer = self.head
                    
        if self.head is not None:
                self.head.previous = newNode
        self.head = newNode
        self.count += 1
                 

    def insertLast(self, newValue1, newValue2):
        newNode = DSANode(newValue1, newValue2)
        newNode.pointer = None
        if self.head is None:
                newNode.previous = None
                self.head = newNode
                return
        lastNode = self.head
        while lastNode.pointer is not None:
                lastNode = lastNode.pointer
        lastNode.pointer = newNode
        newNode.previous = lastNode
        self.count += 1
        return         
            
  
    def peekFirst(self, node):
        return node.head.data1, node.head.data2

    def peekLast(self, node):
        node = node.head
        while node.pointer is not None:
            node = node.pointer
        return node.data1, node.data2

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            self.head = self.head.pointer
            self.count -= 1

    def removeMiddle(self, data):
        temp = self.head
        if temp is not None:
                if temp.data1 == data:
                        self.head = temp.previous
                        temp = None
                        return

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
                self.count -= 1
            else:                       
                curNode.previous.pointer= None
                self.count -= 1
            
    def searchKey(self, data):
        temp = self.head
        while temp is not None:
                if temp.data1 == data:
                        return temp.data2
                temp = temp.previous

    def searchData(self, data):
        temp = self.head
        while temp is not None:
                if temp.data2 == data:
                        return temp.data1
                temp = temp.previous
     
