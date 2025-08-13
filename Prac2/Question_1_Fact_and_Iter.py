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

class LessThanZeroError(Exception):
    """Exception raised for numbers that are less than zero."""
    pass


def factorial_it(n):        # Factorial function (Iterative)         
    n_fact = 1               
    for i in range(1, n+1):
        n_fact *= i
    return n_fact

def factorial_re(n):        # Factorial Recursive      
    if n == 0:
        return 1
    else: 
        return n * factorial_re(n-1)
        
def fibonacci_it(n):        # Fibbonacci Iterative
    n_fib = 0
    curr_val = 1
    last_val = 0
    if n == 0:
        n_fib = 0
    elif n == 1:
        n_fib = 1
    else: 
        for i in range(2, n+1):
            n_fib = curr_val + last_val
            last_val = curr_val
            curr_val = n_fib
    return  n_fib

def fibonacci_re(n):        # Fibbonacci Recursive
    f_val = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        f_val = fibonacci_re(n-1) + fibonacci_re(n-2)
    return f_val

def main():
    try: 
        # REPLACE THIS TO WHATEVER NUMBER YOU LIKE FOR A FACTORIAL RETURN
        
        n = -1.5

        if type(n) != int:
            raise TypeError
        elif n<0:
            raise LessThanZeroError

        print(f"\nFor n = {n}\n")
        print(f"{n} factorial = {factorial_it(n)} (ITERATIVE SOLUTION)")
        print(f"{n} factorial = {factorial_re(n)} (RECURSIVE SOLUTION)")

        print(f"\nThe {n}th value of the Fibonacci Sequence is: ", end ="")
        print(fibonacci_it(n), "(ITERATIVE SOLUTION)")
        print(f"The {n}th value of the Fibonacci Sequence is: ", end ="")
        print(fibonacci_it(n), "(RECURSIVE SOLUTION)\n")
    except TypeError:
        print("\nTypeError: 'n' is not type int.\n")
    except LessThanZeroError:
        print("\nLessThanZeroError: 'n' is less than zero.\n")
    except NameError: 
        print("\nNameError: 'n' is not an integer.\n")

if __name__ == "__main__":
    main()