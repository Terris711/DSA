import pickle

def testFile():
    choice = input("Choose (1) - Read a serialized file, (2) - Display the list, (3) - Write a serialized file, (X) - Exit: ").upper()
                 
    content = [1, 2, 3, 4, 5]
    while choice != "X":
        if choice == "1":
            filename = input("Enter a file: ")
            try:
                with open(filename, "rb") as fileobj:
                    obj = pickle.load(fileobj)
            except IOError:
                print("Error: Object file does not exist")

        elif choice == "2":
            for item in obj:
                print(item, end = " ")
            print()

        elif choice == "3":
            filename = input("Enter file name: ")
            print("Processing...")
            try:
                with open(filename, "wb") as fileobj:
                    pickle.dump(content, fileobj)
            except IOError:
                print("Error!")

        else:
            print("Please choose a valid option!")
    
        choice = input("Choose [1], [2], [3], [X]: ").upper()





