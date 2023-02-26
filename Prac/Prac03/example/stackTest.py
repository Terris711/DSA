from DSAStack import DSAStack

def testStack():
    A = [None]*50
    print("Pushing 50 elements in stack")
    for i  in range(50):
        A.push(i)
    print('Poping 50 elements from stack')
    for i in range(51):
        print(A.pop())


#def testStack():
#    S1 = Stack(50)
#    print("Pushing 50 elements in stack")
#    for i  in range(50):
#        S1.push(i)
#    print('Poping 50 elements from stack')
#    for i in range(51):
#        print(S1.pop())

#def reverseArray(A):
#    for i in range(len(A)):
#        A.push(i)
#    print('Pushing Array element in stack')
#    for i in range(len(A)):
#        print(A.pop())

#A = ['A', 'B','C']
#reverseArray(A)

#def readInt():
#    S1 = Stack()
#    char = input("Enter a character from 0- 9:  ")
#    while '0' <= char <= '9':
#        d = ord(char) -  ord('0')
#        S1.push(d)
#        char = input("Enter a character from 0 - 9: ")

#    value = 0
#    power_of_ten = 1
#    while not S1.isEmpty():
#        digit = S1.pop()
#        value += digit *power_of_ten
#        power_of_ten *= 10
 #   print("Value = ", value)

#readInt() 

testStack()
