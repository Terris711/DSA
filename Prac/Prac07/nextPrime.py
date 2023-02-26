#
# nextPrime.py: Finding the next prime number
#

def nextPrime(number):
    nextP = number + 1
    for i in range(2, nextP):
            if nextP % i == 0:
                    nextP += 1
            else:
                    return nextP
