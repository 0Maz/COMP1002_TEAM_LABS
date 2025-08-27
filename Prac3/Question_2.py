# CIRCULAR QUEUE
#  Create a second implementation of the DSAQueue to use a CircularQueue
# Author:   Mwansa Nawale (22225746)
# Date:     20/08/2025
#
# Dependecies. Question_1.py DSAQueue
#
# References: https://en.wikipedia.org/wiki/Circular_queue

import numpy as np
from Question_1 import DSAQueue


class DSACircularQueue(DSAQueue):
    """Circular queue implementation using numpy array."""

    def __init__(self, capacity):
        """Initializes an empty queue of a given capacity."""
        self.capacity = capacity #maximum amount of elements in the queue
        self.queue = np.empty(capacity, dtype=object)  # Initialize an empty array of given capacity
        self.size = 0 #current number of elements in the queue
        self.front = 0 #index of the front element in the queue
        
    def enqueue(self, element):
        """ Add an element to the back of the queue """
        if (self.size == self.capacity):
            print("queue is full")
        else:
            rear = (self.front + self.size) % self.capacity  # calculates rear position
            self.queue[rear] = element  # adds an element at the next spot at the end of the queue
            self.size += 1

    def dequeue(self):
        """ Takes an element from the fromt of the queue """
        if(self.size == 0):
            print("queue is empty")          
        else:
            current_front = self.queue[self.front] #tmp value to return/pop
            self.front = (self.front + 1) % self.capacity #calculates next step for front to go
            self.size -= 1
            return current_front
        
    def peek(self):
        """ Returns the front element without removing it """
        if(self.size == 0):
            print("queue is empty")
        else:
            return self.queue[self.front]
        
    def isEmpty(self):
        """ Checks if the queue is empty """
        return self.size == 0
    
    def isFull(self): 
        """ Checks if the queue is full """
        return self.size == self.capacity
    
    def count(self):
        """ Returns the number of elements in the queue """
        return self.size


def main():
    print("hello world")
    queue = DSACircularQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Front element:", queue.peek())
    print("Queue size:", queue.count())
    queue.dequeue()
    print("Front element after dequeue:", queue.peek())
    print("Queue size after dequeue:", queue.count())


if __name__ == "__main__":
    main()