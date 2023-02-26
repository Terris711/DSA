import random
import time 

def bubbleSortBasic(A):
    check = False
    i = 0
    while i < len(A) -1:
        for j in range(len(A) - 1 - i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j+1] = temp
                check = True
        i += 1       
        if not check:
            break
    return A



A = [3,2,4,5,1,7,9,6,8,10]


start = time.time()*1000
Result = bubbleSortBasic(A)
print(A)
print("Time: ", time.time()*1000 - start)
