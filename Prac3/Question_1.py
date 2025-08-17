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

class DSAStack():

    def __init__(self, array):
        self.array = array 

    def push(self, element):
        """Add a new item to the top a stack."""
        self.array = np.append(self.array, element)
    
    def pop(self):
        """ Take the top most item from a stack."""
        if self.isEmpty():
            return None
        element = self.array[-1]        # grab the last element
        self.array = self.array[:-1]   # everything but the last element
        return element                  # returns the element we popped off 
    
    def top(self):
        """Look at the top-most item, but leave it on the stack."""
        if self.isEmpty():
            return None
        return self.array[-1]
    
    def isEmpty(self):
        """Check if an array is empty."""
        if len(self.array) == 0:
            return True
        else: 
            return False
    
    def count(self):
        """Returns the number of elements in the stack."""
        return len(self.array)

class DSAQueue():
    def __init__(self, array):
        self.array = array

def main():
    my_stack = np.array([])
    stack = DSAStack(my_stack)      # creating an instance of the class

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.array)
    print(stack.top())
    print(stack.count())
    print(stack.pop())
    print(stack.array)


if __name__ == "__main__":
    main()

