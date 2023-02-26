from DSAQueue import DSAQueue

def testQueue():
    A = DSAQueue(50)
    print('Enqueue 50 elements in queue')
    for i in range(50):
        A.enqueue(i)
    print()
    print('Dequeue 50 elements from queue')
    for i in range(49):
        print(A.dequeue())
        #print(i)
    #A.enqueue(100)
