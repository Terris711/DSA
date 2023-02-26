import time


def facIterative(n):
   factorial = 1
   for i in range(n,1,-1):
       factorial = factorial * i
   return factorial 

def facRecursion(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        factorial = n * facRecursion(n-1)
        return factorial

start = time.time()
for i in range(1,1000):
    try:
        print("factorial(" +str(i) +")",facRecursion(i))
    except RecursionError:
        print("Factorial Recursion limit at i = ", i)
        break

print("Time: ", time.time() - start)



