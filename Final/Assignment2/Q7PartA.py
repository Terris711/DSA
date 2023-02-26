# Hash table using quadratic probing

import numpy as np


def hash1(key):
        checksum = 3445
        for i in range (0, len(key)):
            ch = key[i]
            checksum = checksum + ord(ch)
        hashIdx = checksum % 27
        return hashIdx

    
def hashing(table, table_size, arr):
        
        # Looping through the array to find the hash index
        for i in range(len(arr)):
            # Find the hash value
            hashVal = hash1(arr[i])

            # Insert to table if there is no collision
            if table[hashVal] == 0:
                    table[hashVal] = arr[i]

            else:
            # If there is a collision --> loop through all possible quadratic values and find a suitable one
                for j in range(table_size):
                      # Find the new hash value
                      new_hashVal = (hashVal + j*j) % table_size

                      if table[new_hashVal] == 0:
                              # If no more collision , insert to the table
                              table[new_hashVal] = arr[i]
                              break


    
def hashdisplay(arr, n):
            for i in range(n):
                    print(arr[i], end= " |")
            print()


def main():
        arrKey = ["24", "31", "1234", "456", "789", "890", "93"]

        table_size = 27

        # initialize hash table
        hashTable = np.zeros(27, dtype = object)

        hashing(hashTable, table_size, arrKey)


        hashdisplay(hashTable, table_size)    



if __name__ == "__main__":
        main()       

    
