#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    ... 

def insertionSort(A):
    ...

def selectionSort(A):
    n = len(A)

    for i in range(n):
        min_idx = i
        #finds smallest number in the array
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        #swap
        temp = A[min_idx]
        A[min_idx] = A[i]
        A[i] = temp
    #return sorted array
    return A

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


