from DSAGraph import Graph

Graph = Graph()

filename = input("Choose a file: ")
try:
    with open(filename, "r") as graphFile:
        graphObj = graphFile.readlines()
        #print(graphObj)
        graphFile.close()

        edge = []

        for line in graphObj:
              splitline = line.strip().split(',')
              edge.append(splitline)

        print(edge)

except IOError:
    print("This file does not exist!")


# Count vertex
vertices = []
#for i in range(len(edge)):
#        print(edge[i][0])

          

# Comment:
#- Teacher, in this part, I tried to split element un my edge list but I can not.
#- Can you show us in class how to do this part. File IO is something confuse to me :<<<
