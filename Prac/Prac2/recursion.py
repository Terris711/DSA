# Resursion.py

def factorial(n):
    if n<= 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorialRecursion(n):
     if n <= 1:
        return 1
     else:
        return n*(factorialRecursion(n-1))

import time

start = time.time()
for i in range(2,20):
    print(factorialRecursion(i))

print("Execuation time: ", time.time() - start)
    
    
