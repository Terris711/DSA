from DSADoubledlist import DSADoubledList
from DSAStack import DSAStack
from testStack import testStack
from testQueue import testQueue
from fileIO import testFile

length = int(input("Enter number of element: "))
L = DSADoubledList()
for i in range(length):
    option = int(input("Enter a number you want to add: "))
    L.insertFirst(option)

print()
print("Your current list: ")
L.display()
print()

print("Now, we will try to modify the list!")
print()

print("1. Insert from the head")
print("2. Insert from the tail")
print("3. Delete from the head")
print("4. Delete from the tail")
print("5. Size of list")
print("6. Testing ITERATION")
print("7: Testing DSAStack implementation")
print("8: Testing DSAQueue implementation")
print("9: File IO")
print("10. Exit")
print()
activity = int(input("Enter your option: "))
while activity != 10:
    if activity == 1:
        newKey = int(input("Enter new value: "))
        L.insertFirst(newKey)
        L.display()
    elif activity == 2:
        newKey = int(input("Enter new value: "))
        L.insertLast(newKey)
        L.display()
    elif activity == 3:
        L.removeFirst()
        L.display()
    elif activity == 4:
        L.removeLast()
        L.display()
    elif activity == 5:
        L.getSize();
    elif activity == 6:
        iteration = iter(L)
        data = next(iteration)
        for data in L:
            print(data, end = "-->")
        print()
    elif activity == 7:
        testStack() 
    
    elif activity == 8:
        testQueue()
    
    elif activity == 9:
        testFile()
    #elif activity == 7:
    #elif activity == 7:

              
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






