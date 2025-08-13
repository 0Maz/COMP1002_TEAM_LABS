# TOWERS OF HANOI
# 
# Author:   Mwansa Nawale (22225746)
# Date:     12/08/2025
# 
# Reference: 
# assume src and dest are between 1-3
# n = number of disks


def move_disk(n, src, dest):
    """Prints the move details for a disk."""
    print("    "*n , f"Recursion Level {n}")
    print("    "*n , f"Move disk from Source {src} to Destination {dest}")
    print("    "*n , f"n={n}, src={src}, dest={dest}\n") #disk num, souce peg, desitination peg

    
def towers(n, src, dest, count=0):
    """Solves Towers of Hanoi and returns the move count."""
    if src > 3 or src < 1 or dest > 3 or dest < 1:
            raise ValueError("Source and destination pegs must be between 1 and 3.")
    if n == 1:
        move_disk(n, src, dest)
        return count + 1
    else:
        other = 6 - src - dest                        # Calculate the auxiliary/other/"middle" peg
        towers(n - 1, src, other)                     # move all the disks except the last one (n-1)(bottom) to the "other"(not destination) peg.        
        move_disk(n, src, dest)                        # move the remaining (bottom) disk to the destination peg
        count += 1
        count = towers(n - 1, other, dest, count+1)   # move the top and n-1 disks (top 2 disks) from the "other" peg to the destination peg
        return count + 1


def main():
    total_moves = towers(3, 1, 3)
    print(f"There are {total_moves} moves for this problem")


if __name__ == "__main__":
    main()
