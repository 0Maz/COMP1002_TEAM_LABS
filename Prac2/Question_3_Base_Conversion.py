# NUMBER CONVERSIONS:
#   Make a recursive algorithm for converting decimals to other bases.
#
# Author:   Luke Riedel (22224109)
# Date:     11/08/2025

def convert_base(n,base):
    n = int(n)
    base = int(base)
    if n < base:
        return str(n)
    else:
        return str(convert_base((n//base), base)) + str(n % base)


class BoundError(Exception):
    """Raised when a number is out of bounds of a specified region."""
    pass


def main():
    try:
        #  Replace 'n' and 'base' here...  
        n = 123456789
        base = 2

        if base < 2 or base > 16 or n < 0:
            raise BoundError()
        print(f"\nResult = {convert_base(n, base)}\n")
            
    except (NameError, UnboundLocalError):
        print(
            "\nError: Variable 'n' or 'base' is a string, not an integer"
            " or float.\n"
            )
    except BoundError:
        print(
            f"\n'n' or 'base' out of bounds:\n"
            f"\t - 'n' must be 0 or greater.\t\t Currently: {n}\n" 
            f"\t - 'base' must be from 2 to 16.\t\t Currently: {base}\n"
            )


if __name__ == "__main__":
    main()