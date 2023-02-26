from DSABinarySearchTree import BinarySearchTree
from DSATreeNode import TreeNode

Tree = BinarySearchTree()

print("Now, we will try to modify the list!")
print()

print("1. Insert Nodes")
print("2. Delete Nodes")
print("3. Number of tree elements")
print("4. Find Max Value")
print("5. Find Min Value")
print("6. Print key & value")
print("7. Print IN ORDER")
print("8. Print PRE ORDER")
print("9. Print POST ORDER")
print("10. Display the tree")
print("11. Find Height of tree")
print("12. Check balance of tree")
print("13. Exit")
print()
activity = int(input("Enter your option: "))
while activity != 13:
    if activity == 1:
       key = int(input("Enter key: "))
       value = input("Enter value: ")
       Tree.put(key, value)

    elif activity == 2:
        root = None
        keydelete = int(input("Enter the node you wanna delete: "))
        Tree.deleteNode(keydelete)
        
    elif activity == 3:
        print(Tree.getElements())
        
    elif activity == 4:
        print(Tree.findMax())
        
    elif activity == 5:
        print(Tree.findMin())
       
    elif activity == 6:
        key = int(input("Enter key you wanna search: "))
        print(Tree.get(key))
                              
    elif activity == 7:
        print(Tree.inOrder())

    elif activity == 8:
        print(Tree.preOrder())
    
    elif activity == 9:
        print(Tree.postOrder())
    
    elif activity == 10:
        space = 0
        height = Tree.findHeight()
        Tree.printBinaryTree(space, height)

    elif activity == 11:
        print(Tree.findHeight())
    
    elif activity == 12:
        print(Tree.isBalanced())
    
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






