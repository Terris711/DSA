from SQueue import DSAShufflingQueue

def testShufflingQueue():
    A = DSAShufflingQueue(50)
    print('Enqueue 50 elements in queue')
    for i in range(50):
        A.enqueue(i)
    print()
    print('Dequeue 50 elements from queue')
    for i in range(51):
        print(A.dequeue())
       
