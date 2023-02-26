def search(arr,x):
    for i in range(len(arr)-1):
        if arr[i] == x:
            return i
    return -1


def binarySearch(arr,x):
    low = 0
    high = len(arr) -1
    mid = 0

    while low <= high:
        mid = (high + low) //2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1 

def binaryRecursion(arr, low, high, x):
    if high >= low:
        mid = (high + low) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binaryRecursion(arr, low, mid - 1, x)
        else:
            return binaryRecursion(arr, mid + 1, high, x)
    else:
        return -1

array = [1,2,3,4,5]
value = int(input("Enter a number: "))

print(search(array, value))

print(binarySearch(array, value))

print(binaryRecursion(array,0,len(array) - 1, value))  
