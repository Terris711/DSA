# Linear Search

import numpy as np

def linearSearch(arr, target):
    matchIndex = -1
    ii = 0
    while (ii < len(arr) and matchIndex == -1 ):
        if (arr[ii] == target):
            matchIndex = ii
            print("Correct!")
            break
        else:
            print("Wrong!")
    return matchIndex

#if __name__ == "__main__":
target = int(input("Please enter your number: "))
arr = np.array([1,2,3,6,4,7,8])
index = linearSearch(arr, target)
print("Your number position is in :", index)
