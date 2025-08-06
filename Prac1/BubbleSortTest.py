# BubbleSortTest.py
# small program to test if the bubble sort algorithm worked

import numpy as np
import random
import DSAsorts

REPEATS = 3
NEARLY_PERCENT = 0.10
RANDOM_TIMES = 100

n = 10

A = np.arange(1, n+1, 1)

for i in range(RANDOM_TIMES*n):
    x = int(random.random()*n)
    y = int(random.random()*n)
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

print(A)

DSAsorts.bubbleSort(A)
print(A)