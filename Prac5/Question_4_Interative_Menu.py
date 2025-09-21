# QUESTION 4: INTERACTIVE MENU
#   Create an interactive meu for users to add, delete, and diplay the
#   BST created in the previous 3 questions. 

from Question_1_Binary_Search_Tree import DSABinarySearchTree


def main():

    binarySearchTree = DSABinarySearchTree()

    option = None

    while option != "E":
        print("\n\n--------INTERACTIVE LINKED LIST--------\n")
        print("\nPick an option \n"
        "\n\t(A) Add \n\t(R) Remove  \n\t(D) Display  \n\t(E) Exit\n")

        option = input()
        print()

        if option == "E" : 
            break 
        elif option == "A" :
            try: 
                ans = input("Pick an integer to insert:\t")
                binarySearchTree.insert(int(ans), "Value")
            except ValueError:
                print("\nValueError: Input was not valid, please try again.")
                pass
        elif option == "R" :
            try: 
                if binarySearchTree.count() == 0:
                    print("RemoveError: Cannot remove, BST is empty. Please Add (A) a value first.")
                    pass
                else:
                    binarySearchTree.inOrderTraveral()
                    ans = input("\nPlease select a number from the list above. (Type 'end' to exit)\t")
                    if ans == "end":
                        pass
                    else: 
                        binarySearchTree.delete(int(ans))
            except ValueError:
                print("\nValueError: Input was not an integer, please try again.")
        elif option == "D" : 
            try:
                if binarySearchTree.count() == 0:
                    print("\nDisplayError: BST is empty - Nothing to Display.")
                else:
                    print("Please pick a number from the following options:")
                    print("\n\t1.\tIn-Order Traversal")
                    print("\n\t2.\tPre-Order Traversal")
                    print("\n\t3.\tPost-Order Traversal")
                    ans = int(input("\n\t"))
                    if ans == 1:
                        print("\nIn-Order Traversal sequence:\t", end = '')
                        binarySearchTree.inOrderTraveral()
                    elif ans == 2:
                        print("\nPre-Order Traversal sequence:\t", end = '')
                        binarySearchTree.preOrderTraveral()
                    elif ans == 3:
                        print("\nPost-Order Traversal sequence:\t", end = '')
                        binarySearchTree.postOrderTraveral()
                    else:
                        print("\nInputError: Please pick one of the provided options.")
            except ValueError:
                print("\nValueError: Input was not valid. ")
        else: 
            print("InputError: Please enter one of the provided functions")
    return


if __name__ == '__main__':
    main()