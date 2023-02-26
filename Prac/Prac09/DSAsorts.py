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
    return _mergeSortRecurse(A, 0 , len(A) - 1)

def _mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            
            _mergeSortRecurse(A, leftIdx, midIdx)
            _mergeSortRecurse(A, midIdx + 1, rightIdx)

            _merge(A, leftIdx, midIdx, rightIdx)
    
    return A

def _merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.empty(rightIdx - leftIdx + 1, dtype = int)
    i = leftIdx
    j = midIdx + 1
    k = 0

    while ( i <= midIdx) and (j <= rightIdx):
            if A[i] <= A[j]:
                    tempArr[k] = A[i]
                    i += 1
            else:
                    tempArr[k] = A[j]
                    j += 1
            k += 1
    #print (tempArr)

    for i in range(i, midIdx + 1):
            tempArr[k] = A[i]
            k += 1
            #print (tempArr)

    for j in range(j, rightIdx + 1):
            tempArr[k] = A[j]
            k += 1
            #print (k)
    
    
    for k in range(leftIdx, rightIdx + 1):
            A[k] = tempArr[k - leftIdx]


    return A



def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    return _quickSortRecurse(A, 0, len(A) - 1)

def _quickSortRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
            pivotIdx = leftIdx
            newPivotIdx = _doPartitioning(A, leftIdx, rightIdx, pivotIdx)

            _quickSortRecurse(A, leftIdx, newPivotIdx - 1)
            _quickSortRecurse(A, newPivotIdx + 1, rightIdx)

    return A

def _doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    
# split the array, set new leftIdx and rightIdx
# this function takes last element as pivot
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal

    curIdx = leftIdx

# Sorting by compare and swap (ascending order)
    for i in range(leftIdx, rightIdx):
            if A[i] < pivotVal:
                    A[i], A[curIdx] = A[curIdx], A[i]
                    curIdx += 1
# update index stuff
    newPivotIdx = curIdx
    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivotVal

    return newPivotIdx


def quickSort3Median(A):
    return _quickSort3Recurse(A, 0, len(A) -1)

def _quickSort3Recurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        midIdx = (leftIdx + rightIdx) // 2
        pivotIdx = _median( leftIdx, midIdx, rightIdx)

        newPivotIdx = _doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        _quickSort3Recurse(A, leftIdx, newPivotIdx - 1)
        _quickSort3Recurse(A, newPivotIdx + 1, rightIdx)

    return A

def _median(a,b,c):
    if (a - b) * (c - a) > 0:
        return a
    elif (b - a) * (c - b) > 0:
        return b
    else:
        return c   

def quickSort3way(A):
    return _3wayRecurse(A, 0, len(A) - 1)

def _3wayRecurse(A, first, last):
    i = 0
    j = 0
    if first < last:
            i, j = _partition3(A, first, last, i, j )
            _3wayRecurse(A, first, i)
            _3wayRecurse(A, j, last)
    return A
            

def _partition3(A, left, right, i, j):
    if right - left <= 1:
            if A[right] < A[left]:
                    A[right], A[left] = A[left], a[right]

            i = left
            j = right

    mid = left
    pivot = A[right]
    while mid <= right:
            if A[mid] < pivot:
                    A[left], A[mid] = A[mid], A[left]
                    left += 1
                    mid += 1
            elif A[mid] == pivot:
                    mid += 1
            else:
                    A[mid], A[right] = A[right], A[mid]
                    right -= 1
    i = left - 1
    j = mid
     
    return i, j



def display(A):
    for i in range(len(A)):
        print("A[",i,"] = ", A[i])
       










