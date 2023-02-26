# Thi Van Anh Duong - 90023112
# Question 3 - Part B
#

from DSAListNode import DSANode
from DSA_DESLL import DSA_DESLL

class DSACircular():
    
    def __init__(self, DSA_DESLL, length = 10):
        self.capacity = length
        self.items = DSA_DESLL()
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self):
        return 1 if self.count == 0 else 0

    def enqueue(self, key):
        if self.count == 10:
                print("The queue is currently full")
        else:
                if self.front == -1:
                        self.front = 0
                        self.rear = 0
                        self.items.insertLast(key)
                        print("Item enqueued is: ", key)
                else:
                        self.rear = (self.rear + 1) % self.capacity
                        self.items.insertLast(key)
                        print("Item enqueued is: ", key)
                self.count += 1


    def dequeue(self):
        if self.front == -1:
                print("The queue is currently empty!")
        else:
                if self.front == self.rear:
                        self.items.removeFirst()
                        self.front = -1
                        self.rear = -1
                else:
                        self.items.removeFirst()
                        self.front = (self.front + 1) % self.capacity
                self.count -= 1


    
    def __iter__(self):
        return self.items.__iter__()

    def display(self):
        if self.isEmpty():
                print("The queue is currently empty!")
        else:
                for i in self.items:
                        print(i, end = " ")
                print()


def main():
    C = DSACircular(DSA_DESLL)

    C.enqueue("Banana") 
    C.enqueue("Passion Fruit") 
    C.enqueue("Kiwi") 
    C.enqueue("Apple") 
    C.enqueue("Pomegranate") 
    C.enqueue("Lime") 
    C.enqueue("Strawberry") 
    C.enqueue("Rasberry") 
    C.enqueue("Blueberry") 
    C.enqueue("Blackberry") 
    C.enqueue("Pear") 
    C.enqueue("Jackfruit") 
     
    
    C.display()


if __name__ == "__main__":
        main()

