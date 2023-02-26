from maxHeap import DSAHeap

Heap = DSAHeap() 

print("Testing max heap")
print()

print("1. Add values")
print("2. Delete values")
print("3. Heap sort descending with RandomNames7000.csv")
print("4. Display")
print("5. Get Max Value")
print("6. Get Max child")
print("7. Exit")
print()
activity = int(input("Enter your option: "))
while activity != 7:
    if activity == 1:
       Heap.add(55)
       Heap.add(1)
       Heap.add(13)
       Heap.add(7)
       Heap.add(9)
       Heap.add(0)
       
    elif activity == 2:
       Heap.remove()
       
    elif activity == 3:
       idSort = DSAHeap()
       with open("RandomNames7000.csv","r") as fileobj:
            data = fileobj.readlines()
            for line in data:
                    splitline = line.strip().split(",")
                    idSort.add(int(splitline[0]))

       result = idSort.heapSort(idSort.heapArr, len(idSort.heapArr))

       for i in result:
               print(i)
                
    elif activity == 4:
       Heap.display()
    
    elif activity == 5:
       print(Heap.getMaxValue())
        
    elif activity == 6:
       print(Heap.getMaxChild(2))
        
        
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






