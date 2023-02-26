# Thi Van Anh Duong - 90023112
# Question 4 - Part D
# 

from Q4PartD_Node import TreeNode

class Tree(object):

    def __init__(self):
        self.root = None
        self.count = 0
    
    def getCount(self):
        return self.count
    
    def insert(self, data):
        if self.root:
            self.count += 1
            return self.root.insert(data)
        else:
            self.count += 1
            self.root = TreeNode(data)
            return True
    
    def delete(self, data):
        if self.root is not None:
            self.count -= 1
            return self.root.delete(data, self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preorder(self):
        print("Preorder: ", end = "")
        if self.root is not None:
            self.root.preorder()
        print()
        
    def inorder(self):
        print("Inorder: ", end = "")
        if self.root is not None:
            self.root.inorder()
        print()
        
    def postorder(self):
        print("Postorder: ", end = "")
        if self.root is not None:
            self.root.postorder()
            print()

    def sorted_4_5_num(self):
        print("Entries divisible by 4 and 5 in the tree: ", end = "")
        if self.root is not None:
            self.root.sorted_4_5_num()
        print()

        
