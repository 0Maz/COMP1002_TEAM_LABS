""" SelectionSort.py
 
Name: Mwansa Nawale
Student ID: 22225746
Date: 20/07/2025

Description: Implements a selection sort algorithm.

Appendices:
"""
import numpy as np

# Selection sort with a temporary array

test_numbers = np.array([5, 2, 9, 1, 5, 6])

smallest_num = test_numbers[0]
sorted_array = test_numbers

for i in range(1, len(test_numbers)):
    print(i-1)
#finds smallest number in the array
    for num in test_numbers:
        if num < smallest_num:
            smallest_num = num
    np.delete(test_numbers, i-1)
    sorted_array[i-1] = smallest_num
    print("Smallest number in the array is:", smallest_num, test_numbers[i-1])
    
    print("Sorted array so far:", sorted_array)
    
    #places value at the "start"
    
    
