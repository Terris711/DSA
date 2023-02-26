from treeNode import TreeNode

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

    
# Condition for a tree is balance: 1/ The difference between leftHeight and rightHeight not more than 1 2/ left and right branches of tree is balance
    def isBalanced(self):
        return self._isBalanced(self.root)
    
    def _isBalanced(self, root): 
        if self.root is None:
            return True
        leftHeight = self._findHeight(root.leftchild)
        rightHeight =self._findHeight(root.rightchild)

        if (abs(leftHeight - rightHeight) <= 1) and self._isBalanced(root.rightchild) is True and self._isBalanced(root.leftchild) is True:
            return True
        return False
