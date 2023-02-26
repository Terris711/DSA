import time

def fibIterative(n):
    fibVal = 0 
    currVal = 1
    lastVal = 0 
    
    if (n == 0 ):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for i in range (n):
            fibVal = currVal + lastVal
            lastVal = currVal 
            currVal = fibVal 

    return fibVal

def fibRecursion(n):
    fibVal = 0

    if (n == 0):
        fibVal = 0
    elif ( n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursion(n - 1) + fibRecursion(n - 2)
    return fibVal


start = time.time()
for i in range(1,1000):
    try:
        print("fibonacci(" + str(i) + ")",fibRecursion(i))
    except RecursionError:
        print("Fibonacci Recursion limit at i = ", i)
        break 

print("Time: ", time.time() - start)



