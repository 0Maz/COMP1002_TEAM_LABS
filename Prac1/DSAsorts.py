#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Abbreviaton notice: Trouble-shooting = T.S

def bubbleSort(A):
    n = len(A)   
    if n <= 1:
        return A 
    else: 
        for i in range(n): # n = number of sweeps  
            k = n-i
            for  i in range(k-1):
                j = i+1 
                if A[i] > A[j] and i < k:
                    A[i], A[j] = A[j], A[i] 

                    # print('elements swapped:', A[i], A[j])    (T.S)
                    # print('\n', A)                            (T.S)

                # elif A[i] == A[j]:                            (T.S)    
                    # print("Element ", A[i], "and ", A[j], "not swapped. ")
        return A             

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        j = i   # use a key, 'j' for each loop, allowing us to move backwards safely. 
        while j > 0 and A[j-1] > A[j]: 
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1      # keep on searchin the elements to the left, until its correct. 
    return A

def selectionSort(A):
    n = len(A)

    for i in range(n):
        min_idx = i
        #finds smallest number in the array
        for j in range(i+1, n): # check all the numbers after the current spot to find if there is a smaller one
            if A[j] < A[min_idx]: 
                min_idx = j
        #swap
        A[min_idx], A[i] = A[i], A[min_idx]
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

