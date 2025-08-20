# QUESTION 3: Equation Solver: 

# Synonpsis:  
#   Writing a program that can take a string representing a mathematical
#       equation in infix form and convert it to postfix, then evaluating
#       the postfix. 
#
# Author:   Luke Riedel (22224109)
# Date:     20/08/2025



from Question_1 import DSAStack
from Question_1 import DSAQueue
import numpy as np

def operatorStack(equation):
    """Create and use the stack of operators in an equation, in the form of a string"""
    operator_stack = DSAStack(np.array([]))
    for i in range(len(equation)):
        if equation[i] == '(':
            DSAStack.push(i)



def main():
    equation = "( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )"
    operatorStack(equation)
    


if __name__ == "__main__":
    main()

