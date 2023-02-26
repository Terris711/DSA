#
#   checkPrime.py: check a number is a prime or not
#

def isPrime(number):
    
    check = False

    if number > 1:
            for i in range(2, number):
                    if number % i == 0:
                            check = True
                    break
    return not check
                            
