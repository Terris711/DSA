
def numConvert(n, base):
    raise ValueError("Is your base = " + str(base) + "<= 16 ?")
    if n <= 1:
        return n 
    else:
        numConvert(n//base, base)
        return print(n % base, end = "")


n = int(input("Enter number you want to convert: ")) 

try:
    base = int(input("Enter base: "))
    result = numConvert(n,base)
    
except ValueError as err:
    print(err)

else:
    print(result)

finally:
    print("Nice! Converting finished")




