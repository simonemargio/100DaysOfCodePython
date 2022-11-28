"""
Project Calculator
"""

import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def min(n1, n2):
    return n1 - n2


def pr(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return False


operations = {"+": add, "-": min, "*": pr, "/": div}
choice = "n"

while True:
    if choice != "y":
        firstNumber = float(input("What's the first number?\n->"))
    operation = input("Pick an operation ( + , - , * , / )\n->")
    secondNumber = float(input("What's the next number?\n->"))

    call = operations[operation]
    result = call(firstNumber, secondNumber)
    if not result:
        result = 0
        print("Division by zero!")

    print(f"\n{firstNumber} {operation} {secondNumber} = {result}")
    choice = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n->"))
    if choice == "y":
        firstNumber = result
    else:
        break