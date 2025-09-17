# Binary Search Tree
#  Create a Binary Search Tree Implemetation
# Author:   Mwansa Nawale (22225746)
# Date:     13/09/2025
#
# Dependecies. 
#
# References: DSA Lecture 4

from LLQMethod import DSAQueue

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
        # updateNode = cur                                  you might need to delete this
        try:
            if cur == None:  # Base Case: Found
                #create a new node
                return DSATreeNode(key, value)
            elif key == cur._key:    # Base Case: Key already exists
                raise ValueError
            elif key < cur._key:
                cur._left = self._insertRec(key, value, cur._left)
            else:
                cur._right = self._insertRec(key, value, cur._right)
            return cur
        except ValueError:
            print(f"ValueError: Key: '{str(key)}' Already exists")
            return cur

    def delete(self, key):
        return self.deleteRec(self._root, key)
    
    """def deleteRec(self, node, key):
        
        if node is None:
            return None         # The tree is empty
        if key < node._key:     # Search left
            node._left = self.deleteRec(node._left, key)
        elif key > node._key:    # Search right
            node.right = self.deleteRec(node._right, key)
        
        else: # Now pick out of the three cases
            if node._left is None and node._right is None:
                return None
            elif node._left is None:
                return node._right
            elif node._right is None:
                return node._left
            else:
                sucessor = self.leftMostNode(node._right)
                node._key = sucessor._key
                node._right = self.deleteRec(node._right, sucessor._key)  
        return node"""

    def deleteRec(self, key, curNode):
        updateNode = curNode
        if curNode is None:
            return None
        elif key == curNode._key:
            updateNode = self.deleteNode(key, curNode)
        elif key < curNode._key < 0: #FSAF?????
            curNode._left = self.deleteRec(key, curNode._left)
        else:
            curNode._right = self.deleteRec(key, curNode._right)

    def deleteNode(self, key, delNode):
        updateNode = None

        if delNode.getLeft is None and delNode._right is None: #No children
            updateNode = None # No children
        elif delNode._left is not None and delNode._right is None: #1 child left
            updateNode = delNode._left
        elif delNode._left is None and delNode._right is not None: #1 child right
            updateNode = delNode._right 
        else: #two children
            updateNode = self.promoteSuccessor(delNode._right)
            if updateNode != delNode._right:
                updateNode._right = delNode._right
            updateNode._left = delNode.left
        return updateNode


    def promoteSuccessor(self, cur):
        successor = cur 
        if cur.getLeft is None:
            successor = cur
        else:
            if cur.getLeft is not None:
                successor = self.promoteSuccessor(cur._left)
            if successor == cur._left:
                cur._left = successor._right 
                

    def leftMostNode(self, node):
    # Find the left most minimum
        current = node 
        while current._left is not None:
            current = current._left  
        return 

    def display(self):
        pass

    def height(self):
        return self._heightRec(self._root)
    
    def _heightRec(self, curNode):
        #from lecture
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

    def balance(self): 
        """Returns a percentage along with a left / right bias"""
        
        if self._root is None:    # base case, must be balanced
            return 0 
        leftHeight = self._heightRec(self._root._left)
        rightHeight = self._heightRec(self._root._right)
        balanceValue = leftHeight - rightHeight
        balancePercent = (100 - 100 * abs(balanceValue) / self.count())

        if balanceValue > 0: 
            return print(f"Tree is Left-Bias ({balancePercent}% balanced)")
        elif balanceValue < 0: 
            return print(f"Tree is Right-Bias ({balancePercent}% balanced)")
        else: 
            return print(f"Tree has no bias (100% balanced)")
        
    def count(self):
        return self._countRec(self._root)
    
    def _countRec(self, root):
        if root is None:
            return 0    # base case, empty tree returns coutn of 0
        else:
            return self._countRec(root._left) + self._countRec(root._right) + 1
        
    def inOrderTraveral(self):
        """Returns in-order traversal of BST in the form of a linked list"""
        inOrderQueue = DSAQueue()
        self._inOrderRec(self._root, inOrderQueue)

        for i in range(self.count()):
            print(inOrderQueue.dequeue()._key, end = ' ')
        print()

    def _inOrderRec(self, node, queue):
        if node is not None:
            self._inOrderRec(node._left, queue)
            queue.enqueue(node)
            self._inOrderRec(node._right, queue)

    def preOrderTraveral(self):
        """Returns pre-order traversal of BST in the form of a linked list"""
        preOrderQueue = DSAQueue()
        self._preOrderRec(self._root, preOrderQueue)

        for i in range(self.count()):
            print(preOrderQueue.dequeue()._key, end = ' ')
        print() 
    
    def _preOrderRec(self, node, queue):
        if node is not None:
            queue.enqueue(node)
            self._preOrderRec(node._left, queue)
            self._preOrderRec(node._right, queue) 
    
    def postOrderTraveral(self):
        """Returns pre-order traversal of BST in the form of a linked list"""
        postOrderQueue = DSAQueue()
        self._postOrderRec(self._root, postOrderQueue)

        for i in range(self.count()):
            print(postOrderQueue.dequeue()._key, end = ' ')
        print() 
    
    def _postOrderRec(self, node, queue):
        if node is not None:
            self._postOrderRec(node._left, queue)
            self._postOrderRec(node._right, queue) 
            queue.enqueue(node)

        
def main():

    print("\n----------------------------------------")
    print("\nTESTING OUTPUT:\n")

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

    print('\nTesting Tree Balance:')
    
    #Test Initial Balance
    print(myTree.balance(),'\n')    # should be balanced

    #  Inserting 9, should increase count by 1 and throw off balance
    print(f"Insterting 9")           
    myTree.insert(9, 'temp')
    print("Testing Tree Balance")
    myTree.balance()
    print(f"Count of the tree is: {myTree.count()}\n")
    
    # Inserting 0, should increase count by 1, and restore balance
    print(f"Insterting 0")
    myTree.insert(0, 'temp')
    print("Testing Tree Balance Again...")
    myTree.balance()
    print(f"Count of the tree is: {myTree.count()}\n")

    # Testing In-OrderTraversal:
    print("In Order Traversal...")
    myTree.inOrderTraveral()

    # Testing Pre-OrderTraversal:
    print("\nPre-Order Traversal...")
    myTree.preOrderTraveral()

    # Testing Post-Order Traversal
    print("\nTesting Post-Order Traversal...")
    myTree.postOrderTraveral()

    # Testing Deletion: 
    print("\nTesting Deletion of Nodes")
    myTree.delete(5)
    print("deleting 5")
    print("In Order Traversal")
    myTree.inOrderTraveral()
    

    print("----------------------------------------\n") # end of testing area


if __name__ == "__main__":
    main()