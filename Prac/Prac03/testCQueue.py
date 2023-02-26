from CQueue import DSACircularQueue

def testCircularQueue():
    A = DSACircularQueue(50)
    print('Enqueue 50 elements in queue')
    for i in range(50):
        A.enqueue(i)
    print()
    print('Dequeue 50 elements from queue')
    for i in range(51):
        print(A.dequeue())

