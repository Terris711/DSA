from node import Node

class List:
    def __init__(self): 
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode is not None:
            yield curNode.key
            curNode = curNode.next

    def isEmpty(self):
        return self.head == None

    def printAll(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.key, end ="-->")
            tmp = tmp.next
        print()

    def numberOfElement(self):
        count = 0
        tmp = self.head
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def addToHead(self, key):
        if self.isEmpty():
            self.head = Node(key)
        else:
            tmp = Node(key, self.head)
            self.head = tmp 

    def addToTail(self, key):
        if self.isEmpty():
            self.head = Node(key)
        else:
            tmp = self.head
            while tmp is not None:
                tmp = tmp.next
            tmp.next = Node(key)

    def deleteFromHead(self):
        if self.isEmpty:
            return None
        else:
            delKey = self.head.key
            self.head = self.head.next
        return delKey

    def deleteFromTail(self):
        if self.isEmpty:
            return None
        else:
            curNode = self.head
            preNode = None
            while curNode is not None:
                preNode = curNode
                curNode = curNode.Node.next
            delNode = curNode.next
            preNode.next = None
            return delNode

    def peek(self):
        return self.head.key

