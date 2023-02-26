#Activity 5: Sorting a file
# Student ID: 90023112
# Student Name: Thi Van Anh Duong

from DSAsorts import *
import csv


# Reading the file

with open('studentFile.csv', 'w') as output:
    studentFile = csv.writer(output)
    fileobj = open('RandomNames7000.csv', 'r')
    data = fileobj.readlines()
    fileobj.close()

    sortedData = [] # Store students' ID & Names

    for line in data:
        splitline = line.strip().split(',')
        sortedData.append(splitline)
    
# Sorting the file

    bubbleSort(sortedData)
    selectionSort(sortedData)
    insertionSort(sortedData)

    for i in range(len(sortedData)):
        studentFile.writerow(sortedData[i])
output.close()



        


