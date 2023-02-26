
def gcdIterative(a,b):
    while b != 0:
        if a == 1 or b == 1:
            return 1
        else:
            a,b = b, a%b
    return a

def wrapper(a,b):
     if ( a < -1000 or a > 1000) or ( b < -1000 or b > 1000):
         print("STOP entering too big number, my computer will be crashed!")
     else:
         result = _gcdRecursion(a,b)
         return result


def _gcdRecursion(a,b):
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    return _gcdRecursion(b, a%b)

a = int(input("Enter a: ")) 
b = int(input("Enter b: ")) 

print(wrapper(a,b))
