# Thi Van Anh Duong - 90023112
# Question 2 - Part D
# 

def _revrse_str(Str1):
    # Base case:
    if len(Str1) == 1:
        return Str1

    else:    
         return Str1[len(Str1) - 1] + str(_revrse_str(Str1[:len(Str1) - 1]))

def revrse_str(Str1):
    try:
        return _revrse_str(Str1)
    except TypeError:
        print("Input must be a word!")

def main():
    print(revrse_str("PassDSA"));
    print(revrse_str(90));
    print(revrse_str("100"));
    print(revrse_str("Thi Van Anh Duong"));
    print(revrse_str("a"));
    

if __name__ == "__main__":
    main()


