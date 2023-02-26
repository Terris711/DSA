from DSAStack import DSAStack

def testStack():
    A = DSAStack(50)
    print("Pushing 50 elements in stack")
    for i in range(50):
        A.push(i)
    print()
    print("Poping 50 elements from stack")
    for i in range(51):
        print(A.pop())
