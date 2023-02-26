import time
import random

def insertionSort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
    
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1 

        A[j+1] = key
   
    return A



A = [3,2,4,5,1,7,9,6,8,10]

start = time.time()*1000
Result = insertionSort(A)
print(A)
print("Time: ", time.time()*1000 - start)






        
