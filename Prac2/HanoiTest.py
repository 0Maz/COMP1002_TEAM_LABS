# TOWERS OF HANOI
# 
# Author:   Mwansa Nawale (22225746), Luke Riedel (22224109)
# Date:     12/08/2025
# 
# Reference: https://madooei.github.io/recursion/03-gcd/ 
# assumuem src and dest are between 1-3
# n = number of disks

# prove base case
# assume base - 1 works (next iteration works)
# define relationship between base case and next iteration

def print_move(start, end):
    # Move disk from source to destination
    print(f"Move disk from {start} to {end}")  

def hanoi(n, start, end):
    
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - start - end  # Calculate the auxiliary/other/"middle" peg
        hanoi(n - 1, start, other) # move all the disks except the last one (n-1) to the
                                   #    "other"(not destination) peg.
        print_move(start, end)     # move the remaining (bottom) disk to the destination peg
        hanoi(n - 1, other, end)   # move the top and  n-1 disks (top 2 disks) from the "other"
                                   #    peg to the destination peg

hanoi(3, 1, 3)  # Example call to the function with 3 disks, starting from peg 1 to peg 3