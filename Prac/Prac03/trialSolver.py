# This file I implemented according to my understandings but it does not work :<<<

from DSAStack import DSAStack

def isOperand(a):
    return a >= '0' and a <= '9'

operators ='+-*/'

def isOperator(a):
    return a in operators  

def getPrecedence(a):
    p = 0
    if a == '+' or a == '-':
        p = 1
    elif a == '*' or a == '/':
        p = 2
    return p      

# Convert infix to postfix
def in2pos(infix):
    postfix =""
    opStack = DSAStack(100)

    for char in infix:
        if isOperand(char):
            postfix += char
        elif char == '(':
            opStack.push(char)
        elif char == ')':
            cpop = opStack.pop()
            while cpop != '(':
                opStack += cpop
                cpop = opStack.pop()
        elif isOperator(char):
            while True:
                topChar = opStack.top()

            if opStack.isEmpty or topChar == '(':
                opStack.push(char)
                break  

            else:
                pChar = getPrecedence(char)
                pTopChar = getPrecedence(char)

                if pChar > pTopChar:
                   opStack.push(char)
                   break
                else:
                    postfix += opStack.pop() 


    while not opStack.isEmpty():
        cpop = opStack.pop()
        postfix += cpop                     
            
    return postfix


operation = "1+2*3/4"
in2pos(operation)
