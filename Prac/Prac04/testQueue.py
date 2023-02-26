from DSAQueue import DSAQueue
from DSADoubledlist import DSADoubledList

def testQueue():
    A = DSAQueue()
    print('Enqueue 5 elements in queue')
    for i in range(5):
        A.enqueue(i)

    print()
    print('Dequeue 3 elements from queue')
    for i in range(3):
        print(A.dequeue())
        

