# Thi Van Anh Duong - 90023112
# Question 3 - Part A
#

from DSAStack import DSAStack

def transStack(S1,S2,S3):
        # Transfer data from S1 to S2
        for item in S1._arr:
                while S1.getCount() != 0:
                    S2.push(S1.pop())

        # Transfer data from S2 to S3
        for items in S2._arr:
                while S2.getCount() != 0:
                        S3.push( S2.pop())
        
        print("3 Stacks after moving data:") 
        print("S1 elements: ")
        S1.display()
        print()

        print("S2 elements: ")
        S2.display()
        print()

        print("S3 elements: ")
        S3.display()
        print()

        


def main():
    # Initialize data for S1
    S1 = DSAStack(6)
    S1.push("Banana")
    S1.push("Kiwi")
    S1.push("Tomato")
    S1.push("Passion Fruit")
    S1.push("Bomb")

    S2 = DSAStack(6)
    S3 = DSAStack(6)

    
    print("3 Stacks after moving data:") 
    print("S1 elements: ")
    S1.display()
    print()

    print("S2 elements: ")
    S2.display()
    print()

    print("S3 elements: ")
    S3.display()
    print()
 
   
    transStack(S1,S2,S3)


if __name__ == "__main__":
        main()


