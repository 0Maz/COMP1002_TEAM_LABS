""" SelectionSort.py
 
Name: Mwansa Nawale
Student ID: 22225746
Date: 20/07/2025

Description: Implements a selection sort algorithm.

Appendices:
"""
import numpy as np

test_numbers = np.array([5, -2, 0, 1, 5, 6])

def selection_sort(array):
    n = len(array)

    for i in range(n):
        #who gets to be index 0, then 1, then 2 and so forth progressively
        min_idx = i
        #finds smallest number in the array
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        #swap
        temp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp
    #return sorted array
    return array

print("Sorted Array: ", selection_sort(test_numbers))