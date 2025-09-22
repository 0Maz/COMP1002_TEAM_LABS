# GRAPH IMPLEMEMTATION
# 
# Implement DSAGraph and DSAGraphNode class using linked lists within each node to store the adjacency list
#
# Author: Luke Riedel, Mwansa Nawale

import numpy as np

class DSAGraph():
    
    def __init__(self, capacity):   # capacity == n 
        self.size = 0
        self.capacity = capacity
        self.matrix = np.zeros((capacity, capacity), dtype = object)
        self.labels = np.zeros((capacity, 2), dtype = object)
        
        
    def addVertex(self, label, value):
        if label not in self.labels:
            self.labels[self.size][0] = label   # inserts label in labels
            self.labels[self.size][1] = value   # inserts value in values
            self.size += 1
            return print(f"\n{self.labels} \nself.size = {self.size}\tself.capacity = {self.capacity}")
        
    def addEdge(self, label1, label2):
        if label1 in self.labels and label2 in self.labels:
            self.matrix[(label1-1, label2-1)] += 1
        else: 
            print("InputError: Edge does not Exist")
        return print(self.matrix)
    
    def hasVertex(self):
        return
    
    def getVertexCount(self):
        return 
    
    def getEdgeCount(self):
        return
    
    def isAdjacent(self):
        return
    
    def getAdjacent(self):
        return 
    
    def displayAsList(self):
        return
    
    def displayAsMatrix(self):
        return
            





class DSAGraphNode():

    def __init__(self):
        self.nuts = 69




def main():
    array = DSAGraph(4)
    array.addVertex(1,"One")
    array.addVertex(2, "Two")
    array.addEdge(1,2)
    array.addEdge(1,1)
    

if __name__ == "__main__":
    main()
    print()
