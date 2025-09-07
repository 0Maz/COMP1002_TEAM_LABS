# LinkedList
#  Create a linked list implementation
# Author:   Mwansa Nawale (22225746)
# Date:     07/09/2025
#
# Dependecies. 
#
# References: 

#Single Linked
def DSAListNode(value, next):
    """List node class, takes in a value and a next object of type DSAListNode"""
    def __init__(self, value, next):
        self.value = value
        self.next = None

    def getValue():
        return self.value
    
    def setValue(inValue):
        self.value = inValue
    
    def getNext():
        return self.next
    
    def setNext(newNext):
        ##MUST BE DSALISTNODE
        self.next = newNext
    
        
#Single Ended Single Linked rn
def DSALinkedList(head):
    """ DOCUSTRING """
    def __init__(self, head):
        """Head is data type DSAListNode"""
        self.head = None
    
    def insertFirst(newValue):
        newNd = DSAListNode(newValue)
        if isEmpty():
            self.head = newNd #If empty, the new node will be head
        else:
            newNd.setNext(head) #the old head moves to 2nd
            self.head = newNd #new head
    
    def insertLast(newValue):
        newNd = DSAListNode(newValue)
        if isEmpty():
            self.head = newNd
        else:
            currNd = self.head
            while currNd.getNext() != None: #find the last node
                currNd = currNd.getNext()
            currNd.setNext(newNd) #change the next from None to the new node inserted
    
    def isEmpty():
        return self.head == None

    def peekFirst():
        if isEmpty():
            return
        else:
            return self.head.getValue()
        
    def peekLast():
        if isEmpty():
            return
        else:
            currNd = self.head
            while currNd.getNext() != None: #find the last node
                currNd = currNd.getNext()
            return currNd.getValue()
        
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
            prevNd = None
            currNd = self.head
            while currNd.getNext() != None:
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            return currNd.getValue() #"Pop the value"
            



def main():
    pass

if __name__ == "__main__":
    main()