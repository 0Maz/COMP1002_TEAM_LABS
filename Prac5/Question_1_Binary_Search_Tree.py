# Binary Search Tree
#  Create a Binary Search Tree Implemetation
# Author:   Mwansa Nawale (22225746)
# Date:     13/09/2025
#
# Dependecies. 
#
# References: DSA Lecture 4

class DSATreeNode():

    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None
    
    def __str__(self):
        return f"Key: {self._key} Value: {self._value}"


class DSABinarySearchTree():

    def __init__(self):
        self._root = None
        
    def find(self, key):
        return self._findRec(key, self._root)
    
    def _findRec(self, key, cur):
        if cur is None:     #Base case: not found
            raise ValueError(f"Key {key} not found")     
        elif key == cur._key:   #Base case: Found
            return cur._value
        elif key < cur._key: #Go Left (recursive)
            return self._findRec(key, cur._left)
        else:   #Got Right(recursive)
            return self._findRec(key, cur._right)

    def insert(self, key, value):
        self._root = self._insertRec(key, value, self._root)

    def _insertRec(self, key, value, cur):
        updateNode = cur
        if cur == None:  # Base Case: Found
            #create a new node
            return DSATreeNode(key, value)
        elif key == cur._key:    # Base Case: Key already exists
            raise ValueError("Key: ", str(key), " Already exists")
        elif key < cur._key:
            cur._left = self._insertRec(key, value, cur._left)
        else:
            cur._right = self._insertRec(key, value, cur._right)
        return cur

    def delete(self, key):
        pass

    def display(self):
        pass

    #from lecture
    def height(self):
        return self._heightRec(self._root)
    
    def _heightRec(self, curNode):
        leftHt, rightHt = 0, 0
        if curNode == None: #Base case - no more along this branch
            htSoFar = -1
        else:
            leftHt = self._heightRec(curNode._left) #calc left height
            rightHt = self._heightRec(curNode._right) #calc right height
        if leftHt > rightHt:
            htSoFar = leftHt + 1
        else:
            htSoFar = rightHt + 1
        return htSoFar


    def min(self):
        curNode = self._root
        while(curNode._left != None):
            curNode = curNode._left
        minKey = curNode._key
        return minKey

    def max(self):
        curNode = self._root
        while(curNode._right != None):
            curNode = curNode._right
        minKey = curNode._key
        return minKey


def main():
    print("Testing node creation")
    myNode = DSATreeNode(1, "one")
    print(myNode)

    print("\nTesting BST Insertion")
    myTree = DSABinarySearchTree()
    # Insert multiple nodes
    myTree.insert(4, "four")
    myTree.insert(2, "two")
    myTree.insert(6, "six")
    myTree.insert(1, "one")
    myTree.insert(3, "three")
    myTree.insert(5, "five")
    myTree.insert(7, "seven")

    # Test find
    print("\nTesting find:")
    for key in [4, 2, 6, 1, 3, 5, 7]:
        print(f"Key {key}: {myTree.find(key)}")

    # Test min and max
    print("\nTesting min and max:")
    print("Min key:", myTree.min())
    print("Max key:", myTree.max())

    # Test height
    print("\nTesting height:")
    print("Tree height:", myTree.height())

    # Test find for missing key
    print("\nTesting find for missing key:")
    try:
        print(myTree.find(10))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()