""" 
BubbleSort.py
Name:         Luke Riedel
Student ID:   22224109
Date:         30/07/2025

Description:  Creating bubble sort algorithm to sort through arrays of 
              random, nearly sorted, and sorted numbers, sorting if
              necessary. 

Appendancies:
- 30/07/2025:   Created BubbleSort.py
"""
import numpy as np

def bubble_sort(array):
    n = len(array)
    print('The original array is:\t', array)
    
    if n <= 1:
        return array # If the array is 1, it is already sorted.
    else: 
        for i in range(n):
            k = n-i
            for  i in range(k-1):
                j = i+1
                if array[i] > array[j] and i < k:
                    array[i], array[j] = array[j], array[i]
                    print('elements swapped:', array[i], array[j])
                    print('\n', array)
                elif array[i] == array[j]:
                    print("Element ", array[i], "and ", array[j], "not swapped. ")
        print("\nThe sorted array is:\t", array, '\n')



  # make n-1 comparisons
  # for each element in an array:
  #   compare if E(N-1) < E(N)
  #   - if E1 is greater than E2 for example, swap.
  #   - pass
  # Each number of comparisons should be n-1-k, where k is the number of
  #   complete sweeps that have occured. This is to make thje program 
  #   efficient.
  # return the array after each sweep, and then the final array should be made.
  
def main():
    my_array = np.array([6,2,5,6,2,5,6,3,2])
    bubble_sort(my_array)

if __name__ == "__main__":
    main()
