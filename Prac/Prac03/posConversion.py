from DSAStack import DSAStack

def precedence(op):
    p = 0
    if op == '+' or op == '-':
        p = 1
    elif op == '*' or op == '/':
        p = 2
    return p

def posConvert(infix):
     postfix = ""
     opStack = DSAStack(100)
     for term in infix:
         if term == '(':
            opStack.push(term)
         elif term == ')':
            while opStack.top() != '(':
                postfix += opStack.pop()
            opStack.pop()

         elif term == '+' or term == '-' or term == '*' or term == "/":
            while (not opStack.isEmpty) and (opStack.top() != '(') and precedence(opStack.top) >= precedence(term):
                postfix += opStack.pop()
            opStack.push(term)
         else:
             postfix += term

     while (not opStack.isEmpty):
          postfix += opStack.pop()

     return postfix

print(posConvert('3+4*2/4'))
    
