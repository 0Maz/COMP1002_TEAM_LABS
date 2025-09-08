# LinkedList
#  Create a linked list implementation
# Author:   Mwansa Nawale (22225746)
# Date:     07/09/2025
#
# Dependecies. 
#
# References: DSA Lecture 4

#Single Linked
def DSAListNode(value, next, prev):
    """List node class, takes in a value and a next object of type DSAListNode"""
    def __init__(self, value, next, prev):
        self.value = value
        self.next = None
        self.prev = None

    def getValue():
        return self.value
    
    def setValue(inValue):
        self.value = inValue
    
    def getNext():
        return self.next
    
    def setNext(newNext):
        ##MUST BE DSALISTNODE
        self.next = newNext

    def getPrev():
        return self.prev 
    
    def setPrev(newPrev):
        self.prev = newPrev
    
        
#Single Ended Single Linked rn
def DSALinkedList(head, tail):
    """ DOCUSTRING """
    def __init__(self, head):
        """Head is data type DSAListNode"""
        self.head = None
        self.tail = None
    
    def insertFirst(newValue):
        newNd = DSAListNode(newValue)
        if isEmpty():
            self.head = newNd #If empty, the new node will be head
        else:
            newNd.setNext(self.head) #the old head moves to 2nd
            self.head = newNd #new head
    
    def insertLast(newValue):
        newNd = DSAListNode(newValue)
        if isEmpty(): #Head empty? last will be here
            self.head = newNd
        elif isTailEmpty: #Tail empty? last will be tail
            self.head.setNet(newNd)
            self.tail = newNd
        else: #list has variables?        
            newNd.setPrev(self.tail) #the old tail moves to second last
            self.tail = newNd #new head
    
    def isEmpty():
        return self.head == None #and self.tail == None
    
    def isTailEmpty():
        return self.tail == None

    def peekFirst():
        if isEmpty():
            return
        else:
            return self.head.getValue()
        
    def peekLast():
        if isEmpty():
            return
        else:
            return self.tail.getValue()
        
    def removeFirst():
        if isEmpty():
            return
        else:
            nodeValue = self.head.getValue() #takes the value of current head
            self.head = self.head.getNext()
            return nodeValue #''Pop'' the value
        
    def removeLast():
        if isEmpty():
            return
        elif self.head.getNext == None: #is there just 1 value
            nodeValue = self.head.getValue()
            self.head = None
            return nodeValue #'Pop the value
        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            return nodeValue            



def main():
    pass

if __name__ == "__main__":
    main()