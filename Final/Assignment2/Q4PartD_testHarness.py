# Thi Van Anh Duong - 90023112
# Question 4 - Part D
# 


from Q4PartD_Node import TreeNode
from Q4PartD_Tree import Tree

def main():

    Banana = Tree()

    Banana.insert(120)
    Banana.insert(16)
    Banana.insert(20)
    Banana.insert(125)
    Banana.insert(59)
    Banana.insert(60)
    Banana.insert(4)
    Banana.insert(45)
    Banana.insert(80)
    Banana.insert(36)
    Banana.insert(40)
    Banana.insert(15)


    Banana.preorder()
    Banana.inorder()
    Banana.postorder()
    Banana.sorted_4_5_num()

    print("Number of Banana leaves: ", Banana.getCount())
    



if __name__ == "__main__":
    main()
