from DSAVertex import Vertex
import numpy as np


class Graph:
    def __init__(self, size = None):
        self.size = size 
        self.vList = np.empty(self.size, dtype = object)
        self.AMatrix = np.zeros([self.size, self.size], dtype = object)
        self.count = 0

    def addVertex(self, label, value):
        if self.count == self.size:
            print("Graph is full")
        else:
            tempV = Vertex(label, value, self.count)
            self.vList[self.count] = tempV
            self.count += 1

    def addEdge(self, label1, label2):
        for i in range(self.count):
            if self.vList[i].label == label1:
                tempIndex1 = self.vList[i].index
            if self.vList[i].label == label2:
                tempIndex2 = self.vList[i].index

        self.AMatrix[tempIndex1][tempIndex2] = 1
        self.AMaxtrix[tempIndex2][tempIndex1] = 1

    def getVcount(self):
        return self.count

    def getEdgecount(self):
        tempCount = 0
        for i in range(self.count):
            for j in range(self.count):
                if self.AMatrix[i][j] == 1:
                    tempCount += 1
        return tempCount

    def isAdjacency(self, label1, label2):
        check = False
        for i in range(self.count):
            if self.vList[i].label == label1:
                tempIndex1 = self.vList[i].index
            if self.vList[i].label == label2:
                tempIndex2 = self.vList[i].index
        if self.AMatrix[tempIndex1][tempIndex2] == 1 or self.AMaxtrix[tempIndex2][tempIndex1] == 1:
            check = True
        return check

    def displayvList(self):
        for i in range(self.count):
            print(self.vList[i])

    def displayAMatrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.AMatrix[i][j])



    
