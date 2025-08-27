# QUESTION 3: Equation Solver: 

# Synonpsis:  
#   Writing a program that can take a string representing a mathematical
#       equation in infix form and convert it to postfix, then evaluating
#       the postfix. 
#
# Author:   Luke Riedel (22224109)
# Date:     20/08/2025

from Question_1 import DSAStack
import numpy as np

def precedence(operator):
    """Returns the precedence of operaters with respect to BIMDAS."""
    if operator in '+-':
        return 1
    elif operator in '*/':
        return 2
    elif operator == '^':
        return 3
    return 0

def parseInfixToPostfix(equation):

    infixarray = np.array(equation.split())
    postfix = []                            # postfix empty array 
    operators = np.array([])                # holding array for operator stack 
    operatorStack = DSAStack(operators)     # operator stack

    for term in infixarray:

        if term == '(':
            operatorStack.push(term)
            
        elif term == ')':
            # if a close bracket occurs, pop() everything off until the '( is reached' 
            while not operatorStack.isEmpty() and operatorStack.top() != '(':
                postfix.append(operatorStack.pop())
            if not operatorStack.isEmpty():
                # since we dont have '(' or ')' in postfix, pop off the orginal '(' as it was just for holding
                operatorStack.pop()

        elif term in '+-*/':
            while (not operatorStack.isEmpty() and operatorStack.top != '(' 
                   and precedence(operatorStack.top()) >= precedence(term)):
                postfix.append(operatorStack.pop())
            operatorStack.push(term)

        else: # every other number and letter
            postfix.append(term)    

    while not operatorStack.isEmpty():          
        postfix.append(operatorStack.pop())    # pops off the remaining terms to postfix 

    return postfix


def main():
    equation = "( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )"
    postfix = parseInfixToPostfix(equation)
    postfix_str = ' '.join(postfix)
    print(postfix_str)
    

if __name__ == "__main__":
    main()

