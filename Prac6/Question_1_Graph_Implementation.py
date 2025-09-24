# GRAPH IMPLEMEMTATION
# 
# Implement DSAGraph and DSAGraphNode class using linked lists within each node to store the adjacency list
#
# Author: Luke Riedel, Mwansa Nawale!!

import numpy as np
from Prac5.LLMethod import DSALinkedList
from Prac5.LLMethod import DSAListNode

class DSAGraph():
    """Holds Vertices in linked list
    Each Vertex has a label, a possible value and a linked list of neighbors"""
    def __init__(self):
        self.vertices = DSALinkedList()   
        self.count = 0
        pass
        
    def addVertex(self, label, value):
        self.vertices.insertFirst(DSAGraphNode(label, value))
        self.count += 1
    
    ##both directions
    def addEdge(self, label1, label2):
        """If label1 and label2 exists
            add connection in edge list"""
        try:
            if self.hasNode(label1) and self.hasNode(label2):
                node1 = self.getNode(label1)
                node2 = self.getNode(label2)

                node1.setEdge(label2)
                node2.setEdge(label1)  
        except ValueError:
            if self.hasNode(label2) and self.hasNode(label1) is not True:
                print("Label1 and 2 Does not exist")
            if self.hasNode(label1) is not True:
                print("Label1 Does not exist")
            if self.hasNode(label2) is not True:
                print("Label2 Does not exist")
    
    def hasNode(self, label): ###LOOK AT THIS
        self.vertices.findNode()
        return
    
    def getNodeCount(self):
        return self.count 
    
    def getEdgeCount(self):
        return count #!!!
    

    def getNode(self, label):
        return vertex
    
    def getAdjacent(self, label):
        return vertexList
    
    def isAdjacent(self, label1, label2):
        return bool 
    
    def displayAsList(self):
        pass
    def displayAsMatrix(self):
        pass
    pass

class DSAGraphNode():
    def __init__(self, inLabel, inValue):
        self.label = inLabel
        self.value = inValue
        self.adjacentNodes = DSALinkedList() #linked list of adjacent nodes

        self.edges = DSALinkedList() 

        """edges may be sole keepers of connections --> no "links" in vertex"""
        
        ###self.visited = DSALinkedList()   FOR TRAVERSAL

        self.weighting = 0 #STUFF LATER
        pass

    def getLabel(self):
        return self.label
    
    def getValue(self):
        return self.value
    
    def getAdjacent(self):
        return self.adjacentNodes
    
    ####
    def getAdjacentEdges(self): #####LOOK AT THIS
        "returns list of edges"
        return self.edges
    
    def setEdge(self, node):
        """Vertex is type DSAGraphNode"""
        self.links.insertFirst(node)
        pass

    ####
    def setVisited(): ######LATER
        pass

    def clearVisitied():
        pass

    def getVisited():
        pass

    def toString(self): ######## Print out All the adjacent edges
        

        return string 

    pass


def main():
    array = DSAGraph(4)
    array.addVertex(1,"One")
    array.addVertex(2, "Two")
    array.addEdge(1,2)
    array.addEdge(1,1)
    

if __name__ == "__main__":
    main()
