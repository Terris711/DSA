#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

import numpy as np


def bubbleSort(A):
    check = False
    i = 0
    while i < len(A) - 1:
        for j in range(0, len(A) - 1 - i):
# Each time we loop, we already known the last element is in correct order
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] =  A[j+1]
                A[j+1] = temp
                check = True
        i += 1
        if not check:
            break
    return A
        
        
    
def insertionSort(A):
    for i in range(len(A)):
        key = A[i] # is current value and start from position 2  (in unsorted list)
        j = i - 1   # the first value ( in sorted list)

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key
    
    return A

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


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


#Run program 

#A = np.array([2,6,8,3,1,9,5,0,7,4])
#bubbleSort(A)
#insertionSort(A)
#selectionSort(A)

#for i in range(len(A)):
#    print("A[", i,"] = ", A[i])






