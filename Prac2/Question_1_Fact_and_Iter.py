# FACTORIAL AND FIBONACCI: 
#   Given the code in the lecture slides, implement the iterative and recursive
#   functions for Factorial and Fibonacci;
#
# Author:   Luke Riedel (22224109)
# Date:     09/08/2025
# 
# Assumptions: 
#   - I have to make two function each? An iterative and recursive for both Fac.
#     and Fib.?

import numpy as np

def factorial_It(n):        # Factorial function (Iterative)         
    nFact = 1              # variable for solution we will return at the end
    for i in range(1, n+1):
        nFact *= i
    return nFact

def factorial_Re(n):
    if (n==0):
        return 1
    else: 
        return n * factorial_Re(n-1)
        
def fibonacci_It(n):
    nFib = 0
    currVal = 1
    lastVal = 0

    if (n==0):
        nFib = 0
    elif (n==1):
        nFib = 1
    else: 
        for i in range(2, n+1):
            nFib = currVal + lastVal
            lastVal = currVal
            currVal = nFib
    return  nFib

def fibonacci_Re(n):
    fVal = 0

    if (n==0):
        return 0
    elif (n==1):
        return 1
    else: 
        fVal = fibonacci_Re(n-1) + fibonacci_Re(n-2)
    return fVal

def main():

    # REPLACE THIS TO WHATEVER NUMBER YOU LIKE FOR A FACTORIAL RETURN
    n = 7
    
    print('\nFor n = ', n, '\n')
    print(n, 'factorial =',factorial_It(n), ' (from iterative solution)')
    print(n, 'factorial =', factorial_Re(n), ' (from recursive solution)')

    print('\nThe ',n, 'th value of the Fibonacci Sequence is: ', end = '')
    print( fibonacci_It(n), ' (ITERATIVE SOLUTION)')
    print('The ',n, 'th value of the Fibonacci Sequence is: ', end = '')
    print( fibonacci_It(n), ' (RECURSIVE SOLUTION)\n')

if __name__ == "__main__":
    main()