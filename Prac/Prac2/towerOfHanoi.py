def moveDisk(src,dest):
    print("Moving top disk from tower %s to tower %s" %(src,dest))
    

def towers(n, src, dest, space):
    
    tmp = 6 - src - dest
    print("%s tower(%s,%s,%s)" %(space, n, src, dest))
    print("%s    n = %s, src = %s, dest = %s, tmp = %s" %(space, n, src, dest, tmp))
    
    if n == 1:
        moveDisk(src, dest)
    else:
        towers(n-1, src, dest, space+"    ")
        moveDisk(src, dest)
        towers(n - 1, tmp, dest, space+"    ")


towers(5,1,3, "")
