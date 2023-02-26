import time
import random 


def selectionSort(A):
    for i in range(len(A) - 1):
        minPos = i
        for j in range(i+1,len(A)):
            if A[j] < A[minPos]:
                minPos = j
         
        temp = A[i]
        A[i] = A[minPos]
        A[minPos] = temp
    return A

A = [3,2,4,5,1,7,9,6,8,10]

start = time.time()*1000
Result = selectionSort(A)
print(A)
print("Time: ", time.time()*1000 - start)
