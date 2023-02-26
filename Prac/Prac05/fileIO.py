import pickle
from DSATreeNode import TreeNode
from DSABinarySearchTree import BinarySearchTree

Tree = BinarySearchTree()

print("[1]. Read a CSV file")
print("[2]. Read a serialized file")
print("[3]. Display the tree")
print("[4]. Write a CSV file")
print("[5]. Write a seralized file")
print("[X]. Exit")

choice = input("Enter your option: ").upper()
data = [20, 45, 3, 14, 7, 96, 55]
value = ["A","B","C", "D","E","F"]
while choice != "X":

    if choice == "1":
        filename = input("Choose a file: ")
        with open(filename, "r") as dataFile:
            fileobj = dataFile.readlines()

    elif choice == "2":
        filename = input("Choose a file: ")
        try:
            with open(filename, "rb") as dataFile:
                fileobj = pickle.load(dataFile)
        except IOError:
            print("Error: File does not exist!")

    elif choice == "3":
        Tree = BinarySearchTree()
        for key in data:
            for value in data:
                Tree.put(key, value)
        space = 0
        height = Tree.findHeight()
        Tree.printBinaryTree(space, height)

    elif choice == "4":
        treePath = input("Choose: [1] Preorder, [2] Inorder, [3] Postorder\n")
        if treePath == "1":
            Tree.preOrder()
        elif treePath == "2":
            Tree.inOrder()
        elif treePath == "3":
            Tree.postOrder()
        else:
            print("Please enter a valid option!!")
    elif choice == "5":
        filename = input("Choose a file: ")
        print("Processing...")
        try:
            with open(filename, "wb") as dataFile:
                pickle.dump(data, dataFile)
        except IOError:
            print("Error")
    else:
        print("Please choose a valid option!")

    choice = input("Enter your option: ").upper()


