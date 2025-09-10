# QUESTION 2: 
#   Create DSAStack and DSAQueue using Linked-lists instead of arrays
#
# NOTES: (From Question 2)
#   - For DSAQueue, use enqueue(), perform insertLast() in DSALinkedList
#   - For DSAQueue, use dequeue(), perform peekFirst() and removeFirst()
#       o We can reverse these operations to still achieve FIFO behaviour
#   
#   - For DSAStack, have push() perform insertFirst()
#   - For DSAStack, for pop(), use a combinations of peekFirst() and removeFirst()
#       o We use this to access the first element and remove it. 
#       o We can reverse these operations to acheive LIFO behaviour
#
#   - Similar simplifications occur for isEmpty() and other methods. 
#   - The following methods can be removed... 
#       o isFull()
#       o count()
#       o MAX_CAPACITY
#       o Alternate Constructor etc...      (IDK lol, im too tired for this)

# DSAStack and DSAQueue based on code in Practical 3, COMP1002 (Curtin University). 

from Question_1_Linked_Lists import DSALinkedList

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
    

  
def main():

    print("TESTING LINKED LIST STACK AND QUEUE")
    print("\nDSALinkedList - Stack:\n")
    
    
def main():

    print("TESTING LINKED LIST STACK AND QUEUE")
    print("\nDSALinkedList - Stack:\n")

    # Test DSAStack

    stack = DSAStack()
    print("Pushing 1, 2, 3 onto stack...")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top of stack (should be 3):", stack.top())
    print("Popping from stack (should be 3):", stack.pop())
    print("Popping from stack (should be 2):", stack.pop())
    print("Is stack empty? (should be False):", stack.isEmpty())
    print("Popping from stack (should be 1):", stack.pop())
    print("Is stack empty? (should be True):", stack.isEmpty())

    print("\nDSALinkedList - Queue:\n")

    # Test DSAQueue

    queue = DSAQueue()
    print("Enqueuing 1, 2, 3 into queue...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Peeking the last element (Should be 1)", queue.peek())
    print("Dequeuing from queue (should be 1):", queue.dequeue())
    print("Dequeuing from queue (should be 2):", queue.dequeue())
    print("Is queue empty? (should be False):", queue.isEmpty())
    print("Dequeuing from queue (should be 3):", queue.dequeue())
    print("Is queue empty? (should be True):", queue.isEmpty())

if __name__ == "__main__":
    main()

