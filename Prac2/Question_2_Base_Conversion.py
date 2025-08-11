# NUMBER CONVERSIONS:
#   Make a recurive algorithm for making decimals (base 10), to a number in base 2. 
#
# Author:   Luke Riedel (22224109)
# Date:     11/08/2025


# How converting to base 2 works:
#   - Repeatedly divide by 2, and note the remainders. 
#   - if 0, we mark 0, if 1, we mark 1. 
#   - We continue until the qotient becomes 0. 

# I will try to create my own algorithm. I am thinking of converting to strings 

def convertbase(n,base):
    n = int(n)
    base = int(base)
    if n == 0: 
        return n
    elif n == 1:
        return n
    else:
        return str(convertbase((n/base), base)) + str(n % base)

    
def main():
    n = 10
    base = 2
    print('\nResult = ', convertbase(n, base), '\n') 


if __name__ == "__main__":
    main()