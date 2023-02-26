from DSAGraph import Graph
import numpy as np


Graph = Graph()

print("Start testing with graph ....")
print()

print("1. Add vertexes")
print("2. Add Edges")
print("3. Get vertex count")
print("4. Print vertex list")
print("5. Print Adjacent list")
print("6. Check adjacency")
print("7. Get Edge count")
print("8. List all adjacents")
print("9. Depth First Search")
print("10. Breadth First Search")
print("11. File IO")
print("12. Exit")
print()


activity = int(input("Enter your option: "))

while activity != 12:
    if activity == 1:
       
       label = (input("Enter label: "))
       value = int(input("Enter value: "))
       Graph.addVertices(label, value)

    elif activity == 2:
       
       label1 = input("Enter label1 want to connect: ")
       label2 = input("Enter label2 want to connect: ")
       Graph.addEdge(label1, label2)

    elif activity == 3:
        print(Graph.verticesCount())
                
    elif activity == 4:
        Graph.displayVertex()
               
    elif activity == 5:
        Graph.displayAdjacent()
               
    elif activity == 6:
       label1 = input("Enter label1 wanna check: ")
       label2 = input("Enter label2 wanna check: ")
       print(Graph.hasAdjacent(label1, label2))
                                    
    elif activity == 7:
         print(Graph.getEdgeCount())

    elif activity == 8:
        label = input("Enter label you wanna check: ")
        Graph.getAdjacent(label)
    
    elif activity == 9:
        label = input("Enter label you wanna start: ")
        Graph.Dfs(label)    
    
    elif activity == 10:
        label = input("Enter label you wanna start: ")
        Graph.Bfs(label)  
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






