# LLMethod.py
#   (Linked-List Method), used to help create linked list queue for question 3 of prac 5 
#   Code copied from Prac4, question 1

# Single Linked
class DSAListNode():
    """List node class, takes in a value and a next object of type DSAListNode"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value
    
    def setValue(self, inValue):
        self.value = inValue
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        ##MUST BE DSALISTNODE
        self.next = newNext

    def getPrev(self):
        return self.prev 
    
    def setPrev(self, newPrev):
        self.prev = newPrev
    
        
#Single Ended Single Linked rn
class DSALinkedList():
    """ DOCUSTRING """
    def __init__(self):
        """Head is data type DSAListNode"""
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None #and self.tail == None
    
    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = self.tail = newNd  #If empty, the new node will be head
        else:
            newNd.setNext(self.head) #the old head moves to 2nd
            self.head.setPrev(newNd) #set prev value
            self.head = newNd #new head
    
    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty(): #Head empty? last will be here
            self.head = self.tail = newNd
        else: #list has variables?        
            newNd.setPrev(self.tail) #the old tail moves to second last
            self.tail.setNext(newNd)
            self.tail = newNd #new tail

    def peekFirst(self):
        if self.isEmpty():
            return None
        return self.head.getValue()
        
    def peekLast(self):
        if self.isEmpty():
            return None
        return self.tail.getValue()
        
    def removeFirst(self):
        if self.isEmpty():
            return None
        nodeValue = self.head.getValue() #takes the value of current head
        if self.head == self.tail: #only one node
            self.head = self.tail = None
        else:
            self.head = self.head.getNext()
            self.head.setPrev(None)
        return nodeValue #''Pop'' the value
        
    def removeLast(self):
        if self.isEmpty():
            return None
        nodeValue = self.tail.getValue()
        if self.head == self.tail: #is there just 1 node
            self.head = self.tail = None
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        return nodeValue            