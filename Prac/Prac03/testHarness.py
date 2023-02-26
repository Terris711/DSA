from testStack import testStack
from testQueue import testQueue
from testCQueue import testCircularQueue
from testSQueue import testShufflingQueue
from equationSolver import solver

# Menu

print("-----------INSTRUCTION OF USING-------------")
print('Here are some programs you can try: ')
print('1: Testing Stack')
print('2: Testing Queue')
print('3: Testing Circular Queue')
print('4: Testing Shuffling Queue')
print('5: Equation Solver')

option = int(input("Enter your option: "))

if option == 1:
    testStack()

elif option == 2:
    testQueue()

elif option == 3:
    testCircularQueue()

elif option == 4:
    testShufflingQueue()

elif option == 5:
    equation = input("Enter an operator: ")
    solver(equation)

