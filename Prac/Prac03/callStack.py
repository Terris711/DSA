def addNum(a,b):
    result = a + b
    return result

def averageNum(a,b):
    result = addNum(a,b) / 2
    return result

def printNum(a,b):
    print(averageNum(a,b))

a = int(input("Enter a: "))
b = int(input("Enter b: "))
printNum(a,b)
