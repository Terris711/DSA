from DSAStack import DSAStack
from DSAQueue import DSAQueue
# my infix2postfix conversion do not work properly before I write this program

def solver(equation):
    postfix = _parseInfixToPostfix(equation)
    _evaluatePostfix(postfix)

def _evaluatePostfix(postfixQueue):
   numStack = DSAStack(100)
   answer = 0.0
   print(postfixQueue)
   for i in postfixQueue:
       #at this step, I just write according to instruction, I dont know what is postfixQueue 
       if i.isdigit():
           numStack.push(i)
       elif i == '+' or i == '-' or i == '*' or i =='/':
           op1 = int(numStack.pop())
           op2 = int(numStack.pop())
           num = _executeOperation(i, op1, op2)
           numStack.push(num)

   answer = numStack.pop()
   print(answer)

def _precedenceOf(theOp):
    p = 0
    if theOp == '+' or theOp == '-':
        p = 1
    elif theOp == '*' or theOp == '/':
        p = 2
    return p

def _executeOperation(op, op1, op2):
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2


def _parseInfixToPostfix(equation):
     postfix = ""
     opStack = DSAStack(100)
     for term in equation:
         if term == '(':
            opStack.push(term)
         elif term == ')':
            while opStack.top() != '(':
                postfix += opStack.pop()
            opStack.pop()

         elif term == '+' or term == '-' or term == '*' or term == "/":
            while (not opStack.isEmpty()) and (opStack.top() != '(') and _precedenceOf(opStack.top()) >= _precedenceOf(term):
                postfix += opStack.pop()
            opStack.push(term)
         else:
             postfix += term

     while (not opStack.isEmpty()):
          postfix += opStack.pop()

     return postfix

    
