from DSATreeNode import TreeNode

class BinarySearchTree():
    def __init__(self, root = None):
        self.root = root
        self.elements = 0

    def isEmpty(self):
        return self.root == None

    def hasLeftchild(self, root):
        return root.leftchild != None

    def hasRightchild(self, root):
        return root.rightchild != None

    def isLeaf(self, root):
        return root.rightchild == None and root.leftchild == None

    def hasBothChildren(self, root):
        return root.rightchild != None and root.leftchild != None

    def put(self, key, value):
        if self.isEmpty():
            self.root = TreeNode(key, value)
            self.elements += 1
        else:
            self._put(self.root, key, value) #call another recursive function with the same root and key & value
           
    def _put(self, root, key, value):
        if root.key == key:
            root.value = value # if the key insert == current key ==> overwrite the current key by the newkey
        elif key < root.key:
            if self.hasLeftchild(root):
                self._put(root.leftchild, key, value)
            else:
                root.leftchild = TreeNode(key, value)
                self.elements += 1
        else:
            if self.hasRightchild(root):
                self._put(root.rightchild, key, value)
            else:
                root.rightchild = TreeNode(key, value)
                self.elements += 1
            
    def get(self, key):
        if self.isEmpty():
            return None
        else:
            return self._get(self.root, key)

    def _get(self, root, key):
        if root.key == key:
            return root
        elif key < root.key:
            if self.hasLeftchild(root):
                self._get(root.leftchild, key)
            else:
                return None
        else:
            if self.hasRightchild(root):
                self._get(root.rightchild, key)
            else: 
                return None

    def findMax(self): # is value in the most right side of the tree
        if self.isEmpty():
            return None
        else:
            curNode = self.root
            while curNode.rightchild is not None:
                curNode = curNode.rightchild
            return curNode.key 

    def findMin(self): # is valye is in most left side of the tree
        if self.isEmpty():
            return None
        else:
            curNode = self.root
            while curNode.leftchild is not None:
                curNode = curNode.leftchild
            return curNode.key

    def getElements(self):
        return self.elements

    def inOrder(self): # Sort in ascending order: check left -> root -> right
        if self.isEmpty():
            return None
        else:
            self._inOrder(self.root) # set the current print node as new root

    def _inOrder(self, root):
        if root is None:
            return None
        else:
            self._inOrder(root.leftchild)
            print(root)
            self._inOrder(root.rightchild)


    def preOrder(self): # check root -> left -> right
        if self.isEmpty():
            return None
        else:
            self._preOrder(self.root)

    def _preOrder(self, root):
        if root is None:
            return None
        else:
            print(root)
            self._preOrder(root.leftchild)
            self._preOrder(root.rightchild)

    def postOrder(self): # check left -> right -> root
        if self.isEmpty():
            return None
        else:
            self._postOrder(self.root)
    
    def _postOrder(self, root):
        if root is None:
            return None
        else:
            self._postOrder(root.leftchild)
            self._postOrder(root.rightchild)
            print(root)

    def findHeight(self):
        return self._findHeight(self.root)

    def _findHeight(self, curNode):
        if curNode == None:
            height = -1 # No more nodes so far ==> height stop at that point
        else:
            leftHeight = self._findHeight(curNode.leftchild)
            rightHeight = self._findHeight(curNode.rightchild)

            if leftHeight > rightHeight:
                height = leftHeight + 1
            else:
                height = rightHeight + 1
            
        return height 

    
# Condition for a tree is balance: 
######1/ The difference between leftHeight and rightHeight not more than 1 
######2/ left and right branches of tree is balance
    def isBalanced(self):
        return self._isBalanced(self.root)
    
    def _isBalanced(self, curNode): 
        if curNode is None:
            return True
        else:
            leftHeight = self._findHeight(curNode.leftchild)
            rightHeight =self._findHeight(curNode.rightchild)

        if (abs(leftHeight - rightHeight) <= 1) and self._isBalanced(curNode.rightchild) is True and self._isBalanced(curNode.leftchild) is True:
            return True
        return False
    def deleteNode(self, key):
        return self._deleteNode(self.root, key)
    def _deleteNode(self, delNode, key):
        if delNode is None:
            return delNode
        #Find the delete key:

        #Case 1: if the key you want to delete < root's key ==> the deleted key should lie in the leftside
        # Use recursive function to delete it
        if key < delNode.key:
            delNode.leftchild = self._deleteNode(delNode.leftchild, key)
            
        #Case 2: Similarly, if the deleted key > root's key ==> it should lie in the right side ==> delete the key in the right side of it
        elif key > delNode.key:
            delNode.rightchild = self._deleteNode(delNode.rightchild, key)
            

        #Case 3: The last probability is root's key == deleted key
        else:
# Delete node with no child (leaves) or only 1 child
            if delNode.leftchild is None:
                temp = delNode.rightchild # case only 1 child: copy the child to the node and delete the node
                delNode = None
                self.elements -= 1
                return temp

            elif delNode.rightchild is None:
                temp = delNode.leftchild 
                delNode = None
                self.elements -= 1
                return temp

            # Delete node with 2 children:
            # Get the smallest node in the right side of tree
            temp = self.findMin(delNode.rightchild)
            # copy content of deleted Node to this node
            temp.key = delNode.key
            # detele this node ( now this node have new value)
            delNode.rightchild = self._deleteNode(delNode.rightchild, temp.key)
            self.elements -= 1
    def printBinaryTree(self, space, height):
        return self._printBinaryTree(self.root, space, height)


    def _printBinaryTree(self,curNode, space, height):
 
    # Base case
        if curNode is None:
            return None
 
    # increase distance between levels
        space += height
 
    # print right child first
        self._printBinaryTree(curNode.rightchild, space, height)
        print()
 
    # print the current node after padding with spaces
        for i in range(height, space):
            print(' ', end='')
 
        print(curNode.key, end='')
 
    # print left child
        print()
        self._printBinaryTree(curNode.leftchild, space, height)
 





