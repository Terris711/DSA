import numpy as np
from DSADoubledlist import DSADoubledList
from DSAGraphEdge import GraphEdge
from DSAGraphVertex import GraphVertex
from DSAQueue import DSAQueue
from DSAStack import DSAStack


class Graph:
    
    def __init__(self):
        self.vertices = DSADoubledList()
        self.adjlist = DSADoubledList()
        self.count = 0

    def addVertices(self, label, value):
        temp = GraphVertex(label, value)
        self.vertices.insertLast(temp)
        self.count += 1

    def verticesCount(self):
        return self.count

    def addEdge(self, label1, label2):
        vertex1, value1 = self.getVertex(label1)
        vertex2, value2 = self.getVertex(label2)

        print("Trying to connect ", vertex1.label, "and", vertex2.label)

        self.adjlist.insertLast(GraphEdge(vertex1, vertex2)) 

        vertex1.adjacent.insertLast(GraphVertex(vertex2, value2))
        vertex2.adjacent.insertLast(GraphVertex(vertex1, value1))

    def getEdgeCount(self):
        n = self.verticesCount()
        result = (n*(n - 1)) // 2
        return result


    def getVertex(self, label):
        for vertex in self.vertices:
                if vertex.label == label:
                        return vertex, vertex.label # return 2 values

    
    def hasVertex(self, label):
        for vertex in self.vertices:
                if vertex.label == label:
                        return True
        return False


    def hasAdjacent(self, label1, label2): # Check two labels are neighbor or not
        check = False
        vertex, value = self.getVertex(label1)
        neighbor = vertex.getAdjacent()

        for node in neighbor:
            if node.getLabel() == label2:
               check = True
        return check 

    def getAdjacent(self, label):
        print("All neighbor of ", label + " is :\n", end = " ")
        vertex, value = self.getVertex(label)
        neighbor = vertex.getAdjacent()
        for vertex in neighbor:
               print(vertex.getLabel(), end = " ")
        print()

    def displayVertex(self):
        for vertex in self.vertices:
                print(vertex.label, vertex.value)

    def displayAdjacent(self):
        for vertex in self.adjlist:
                print(vertex.froM.label, vertex.to.label)

    def Dfs(self, label):
        visited = []
        marked = []
        S = DSAStack(50)
        S.push(label)
        while not S.isEmpty():
                v = S.pop()
                if not v in marked:
                        visited.append(v)
                        marked.append(v)
                        neighbor = self.getAdjacent(v)
                        for w in neighbor:
                                if not w in marked:
                                        S.push(w)
        print(visited)
        

    def BFS(self, label):
        visited = []
        marked = []
        Q = DSAQueue(50)
        Q.enqueue(label)
        while not Q.isEmpty():
                v = Q.dequeue()
                if not v in marked:
                        visited.append(v)
                        marked.append(v)
                        neighbor = self.getAjacent(v) 
                        for w in neighbor:
                                if not w in marked:
                                        Q.enqueue(w)   
   # I did understand the algorithm of dfs and bfs but when I implement it, It shows me undesigned result. 
   # Sorry for this part does not work :<<
   # I need more time to fix it. If would be the best day in my life if you an have a conversation with me and help me understand my bug before the assgnment 1 release soon :<<<

        
