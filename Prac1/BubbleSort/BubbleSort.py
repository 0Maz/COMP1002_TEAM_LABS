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
    if n <= 1:
        return array # If the array is 1, it is already sorted.
    for i in range(n-1):
        q = n-i-1
        j = n-1

        print("q is:", q)
        print("j is:", j)
        print()
        

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
