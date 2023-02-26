class TreeNode():
    def __init__ (self, key = None, value = None, leftchild = None, rightchild = None):
        self.key = key
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild

    def __str__(self):
        return("Key: " + str(self.key) + " Value: " + str(self.value))
