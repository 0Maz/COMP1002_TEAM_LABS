# LLQMethod.py
#   Linked-List-Queue Method
#   Imports from LLMethod (Linked List Method) uses it to create a queue. 
#   Copied directly from Question_2 of Prac4

from LLMethod import DSALinkedList

class DSAStack(DSALinkedList):       # uses LIFO (Last in First Out)

    def __init__ (self):
        self.DSALinkedList = DSALinkedList()
    
    def push(self, element):
        self.DSALinkedList.insertFirst(element)


    def pop(self):
        return self.DSALinkedList.removeFirst()

        
    def top(self):
        return self.DSALinkedList.peekFirst()
    
     
    def isEmpty(self):
        return self.DSALinkedList.isEmpty()
        

class DSAQueue(DSAStack):       # Uses FIFO (First In First Out)
    
    def __init__(self):
        self.DSALinkedList = DSALinkedList()

    def enqueue(self, element): 
        """Adds Item to the back of the queue. """
        self.push(element)

    def dequeue(self):
        """Takes of the first element in the queue (delete, remove). """
        return self.DSALinkedList.removeLast()
    
    def peek(self):
        return self.DSALinkedList.peekLast()


        
    
