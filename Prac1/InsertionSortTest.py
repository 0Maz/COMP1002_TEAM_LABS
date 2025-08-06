# InsertionSortTest.py
#
# used to develop and test insertion sort algorithm for a random array 
# of numbers from 1-n. 

import numpy as np
import random
import DSAsorts

REPEATS = 3
NEARLY_PERCENT = 0.10
RANDOM_TIMES = 100

n = 13

A = np.arange(1, n+1, 1)

for i in range(RANDOM_TIMES*n):
    x = int(random.random()*n)
    y = int(random.random()*n)
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

print(A) # Randomoly sorted array of 1-n terms for an n-sized array

def insertionSort(A): 
    n = len(A)
    for i in range(1, n):
        j = i   # use a key, 'j' for each loop, allowing us to move backwards safely. 
        while j > 0 and A[j-1] > A[j]: 
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1      # keep on searchin the elements to the left, until its correct. 
    return A

print('\nThe ordered array is:\t', insertionSort(A), '\n')