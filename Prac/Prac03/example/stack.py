class Stack:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.pointer = -1


    def count(self):
        return self.pointer + 1

    def isEmpty(self):
        return self.pointer == -1


    def isFull(self):
        return self.pointer ==  self.capacity - 1

    def push(self, item):
        if self.isFull():
            raise Exception('Stack Overflow')

        self.pointer += 1
        self.stack[self.pointer] = item

    def pop(self):
        if self.isEmpty():
             raise Exception('Stack Underflow')

        item = self.stack[self.pointer]
        self.pointer -= 1
        return item

    def top(self):
        if self.isEmpty():
            raise Exceptiuon('Stack Underflow')
        return self.stack[self.pointer]
