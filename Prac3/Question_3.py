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

class TwoAdjacentOperatorsError(Exception):
    """Raised if two operators are side by side i.e. ++ ,  +* , ..."""
    pass 

class BracketNotClosedError(Exception):
    """Rasied if a bracket is not closed inside the Infix equation."""
    

def precedence(operator):
    """Returns the precedence of operaters with respect to BIMDAS."""
    if operator in '+-':
        return 1
    elif operator in '*/':
        return 2
    elif operator == '^':
        return 3
    return 0

def noSpaces(equation):
    """Checks that no two operators are together (without spaces) in the infix"""
    for i in range(len(equation)):
        if equation[i] in '+-*/' and equation[i+1] in '+-*/':
            return True


    return False 

def bracketCheck(equation):
    open = 0
    close = 0
    for i in range(len(equation)):
        if equation[i] == '(':
            open += 1
        elif equation[i] == ')':
            close += 1
    if open == close:
        return False
    elif open != close:
        return True

def parseInfixToPostfix(equation):

    infixArray = np.array(equation.split())
    postfix = []                            # postfix empty array 
    operators = np.array([])                # holding array for operator stack 
    operatorStack = DSAStack(operators)     # operator stack

    if noSpaces(equation):  # e.g. ' *+ ' (where they are directly next to each other)
        raise TwoAdjacentOperatorsError("TwoAdjacentOperatorsError: There are two adjacent operators in the equation. ")
    
    if noSpaces(infixArray): # e.g. ' * + ' (where they are next to each other, but spaced out)
        raise TwoAdjacentOperatorsError("TwoAdjacentOperatorsError: There are two ajacent operators ")
    
    if bracketCheck(equation):
        raise BracketNotClosedError("BracketNotClosedError: At least one set of brackets not closed. ")
    

    for term in infixArray:

        if term == '(':
            operatorStack.push(term)
            
        elif term == ')':
            # if a close bracket occurs, pop() everything off until the '( is reached' 
            while not operatorStack.isEmpty() and operatorStack.top() != '(':
                postfix.append(operatorStack.pop())

            if not operatorStack.isEmpty():
                # since we dont have '(' or ')' in postfix, pop off the orginal '(' as it was just for holding
                operatorStack.pop()

        elif term in '+-*/^':
            while (not operatorStack.isEmpty() and operatorStack.top != '(' 
                   and precedence(operatorStack.top()) >= precedence(term)):
                postfix.append(operatorStack.pop())
            operatorStack.push(term)

        else: # every other number and letter
            postfix.append(term)    

    while not operatorStack.isEmpty():          
        postfix.append(operatorStack.pop())    # pops off the remaining terms to postfix 

    return postfix

def evaluatePostfix(postfix):
    
    postfixArray = np.array(postfix.split())
    evaluateArray = np.array([])
    evaluateStack = DSAStack(evaluateArray)

    for term in postfixArray:
        if term not in '+-*/^':
            evaluateStack.push(term)
        else: 
            b = float(evaluateStack.pop())
            a = float(evaluateStack.pop())

            if term == '+':
                evaluateStack.push(a+b)
            if term == '-':
                evaluateStack.push(a-b)
            if term == '*':
                evaluateStack.push(a*b)
            if term == '/':
                evaluateStack.push(a/b)
            if term == '^':
                evaluateStack.push(a**b)
          
    return evaluateStack.array[0]

def main():

    # CHANGE THE EQUATION BELOW: 
    equation = " ( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )" 
    
    print(f"The original equation: \t{equation}")
    postfix = ' '.join(parseInfixToPostfix(equation))   # ' '.join joins the string together
    print(f"The postfix equation: \t {postfix}")
    print(f"The evaluated postfix equation is: \t{evaluatePostfix(postfix)}")
    
if __name__ == "__main__":
    main()

