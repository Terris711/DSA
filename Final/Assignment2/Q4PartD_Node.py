# Thi Van Anh Duong - 90023112
# Question 4 - Part D
# 

class TreeNode(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False

        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = TreeNode(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = TreeNode(data)
                return True

    def minValueNode(self, node):
        current = node
        while current.leftChild is not None:
            current = current.leftChild
        return current

    def maxValueNode(self, node):
        current = node
        while current.rightChild is not None:
            current = current.rightChild
        return current

    def height(self):
        return self._heightRec(self.root)
    
    def _heightRec(self, currNode):
        if currNode == None:
            height = -1
        else:
            leftHeight = self._heightRec(currNode.leftChild)
            rightHeight = self._heightRec(currNode.rightChild)

            if leftHeight > rightHeight:
                height = leftHight + 1
            else:
                height = rightHeight + 1

        return height

    def delete(self, data, root):
        
        if self is None:
            return None

        if data < self.data:
            self.leftChild = self.leftChild.delete(data, root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data, root)
        else:
            if self.leftChild is None:
                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data, root)

                temp = self.rightChild
                self = None
                return temp

            elif self.rightChild is none:
                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data, root)

                temp = self.leftChild
                self = None
                return temp
            
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data, root)

        return self
    
    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    
    def preorder(self): 
        if self:
            print(str(self.data), end = " ")
            if self.leftChild:
                self.leftChild.preorder()       
            if self.rightChild:
                self.rightChild.preorder()


    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = " ")
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = " ")

    def sorted_4_5_num(self):
        if self:
            if self.leftChild:
                self.leftChild.sorted_4_5_num()
            if int(self.data) % 4 == 0 and int(self.data) % 5 == 0:
                print(str(self.data), end = " ")
            if self.rightChild:
                self.rightChild.sorted_4_5_num()

