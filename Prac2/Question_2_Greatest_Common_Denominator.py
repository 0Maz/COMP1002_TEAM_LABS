# GREATEST COMMON DENOMINATOR
#  Search online (or make your own) recursive algorithm for finding the Greatest Common Denominator. 
#  Implement it in Java or Python.
#
# Author:   Mwansa Nawale (22225746)
# Date:     12/08/2025
# 
# Reference: https://madooei.github.io/recursion/03-gcd/ 
#
# gcd(a,b)=gcd(a′,b)=gcd(b,a)
# When b=0 that mean it is a facotor (a%b = 0)
#

def gcd(a,b):
    if(b==0):
        return a
    else:
        print("a: ", a, " b: ", b)
        return gcd(b,a%b)

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if a < 0 or b < 0:
            print("Please enter non-negative integers.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

GCD=gcd(a,b)
print("GCD is: ")
print(GCD)