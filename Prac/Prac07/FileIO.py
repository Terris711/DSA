#
# FileIO.py - processing RandomNames7000.csv by using hashtable (seperate chaining)
#

from DSAHashEntry import HashEntry, HashTable
import csv

Hash = HashTable(1000)

with open("RandomNames7000.csv","r") as fileObj:
    data = fileObj.readlines()
    for line in data:
            splitline = line.strip().split(",")
            Hash.put(int(splitline[0]), splitline[1])
            #print(splitline)
fileObj.close()

Hash.hashdisplay()

# Run "python3 FileIO.py >> HashStudent.txt" to store the output
