# QUESTION 1: IMPLEMENTATION OF STACK AND QUEUE:
#
# Synonpsis:  
#   Implement our own versions of stacks and queues to understand how
#   they work.
#
# Author:   Luke Riedel (22224109)
# Date:     17/08/2025
#
# Notes: 
#   - Remember that the end of an array is considered the top of a stack.

import numpy as np

class DSAStack():       # uses LIFO (Last in First Out)

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = np.empty(capacity, dtype=object) # empty stack
    
    def push(self, element):
        """Add a new item to the top a stack. """
        if self.size == self.capacity: #if full
            print("stack is full")
            return None 
        self.array[self.size] = element
        self.size += 1

    def pop(self):
        """ Take the top most item from a stack. """
        if self.isEmpty():
            return None
        element = self.array[self.size - 1]
        self.array[self.size - 1] = None        # grab the last element
        self.size -= 1
        return element  
        

    def top(self):
        """Look at the top-most item, but leave it on the stack. """
        if self.isEmpty():
            return None
        return self.array[self.size - 1]
    
    
    def isEmpty(self):
        """Check if an array is empty. """
        if self.size == 0:
            return True
        else: 
            return False
        
    def count(self):
        """Returns the number of elements in the stack. """
        return self.size


class DSAQueue(DSAStack):       # Uses FIFO (First In First Out)
    def __init__(self, element):
        self.element = element

    def enqueue(self, element): 
        """Adds Item to the back of the queue. """
        self.push(element)

    def dequeue(self):
        """Takes of the first element in the queue (delete, remove). """
        if self.count() == 0:
            return None
        else:
            element = self.array[0]
            self.array = self.array[1:]     # returns eveything but the element we took off
            return element
    
    def peek(self):
        """Check the first item, but do not take it off. """
        if self.isEmpty():
            return None
        return self.array[0]
    
    def isEmpty(self):
        """Checks if a queue is empty or not"""
        return self.isEmpty()     
     # ^ IDK about this one, like is it a good idea to 
     #   define it in this subclass again?

  
def main():

    # mostly just me testing in this section: 
    
     my_stack = np.array([])
     stack = DSAStack(10)      # creating an instance of the class

     print(stack.count())
     stack.push(10)
     stack.push(20)
     stack.push(30)

     print(stack.array)
     print(stack.top())
     print(stack.count())
     print(stack.pop())
     print(stack.array)
    #return
    
if __name__ == "__main__":
    main()

