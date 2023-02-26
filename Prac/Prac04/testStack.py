from DSAStack import DSAStack
from DSADoubledlist import DSADoubledList

def testStack():
    A = DSAStack()
    print("Pushing 5 elements in stack")
    for i in range(5):
        A.push(i)
    print()
    print("Poping 3 elements from stack")
    for i in range(3):
        print(A.pop())
