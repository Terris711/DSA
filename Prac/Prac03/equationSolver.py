from DSAStack import DSAStack

def solver(equation):
    postfix = _parseInfixToPostfix(equation)
    _evaluatePostfix(postfix)

def _evaluatePostfix(postfixQueue):
    numStack = DSAStack(100)
    answer = 0.0
    print(f"Postfix expression: {postfixQueue}")
    for i in postfixQueue:
        if i.isdigit():
            numStack.push(int(i))
        elif i in ['+', '-', '*', '/']:
            op2 = numStack.pop()  # Note the order of popping
            op1 = numStack.pop()
            num = _executeOperation(i, op1, op2)
            numStack.push(num)

    answer = numStack.pop()
    print(f"Answer: {answer}")

def _precedenceOf(theOp):
    if theOp in ['+', '-']:
        return 1
    elif theOp in ['*', '/']:
        return 2
    return 0

def _executeOperation(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
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
        elif term in ['+', '-', '*', '/']:
            while (not opStack.isEmpty()) and (opStack.top() != '(') and _precedenceOf(opStack.top()) >= _precedenceOf(term):
                postfix += opStack.pop()
            opStack.push(term)
        else:
            postfix += term

    while not opStack.isEmpty():
        postfix += opStack.pop()

    return postfix

# Example usage:
equation = "3+(2*5)-8/4"  # Example infix expression
solver(equation)
