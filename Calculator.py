from ASCII_ART import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def Multiply(n1, n2):
    return n1 * n2


def Division(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": Multiply, "/": Division}

num1 = int(input("What's the first number?: "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

symbol = operations[operation_symbol]

first_answer = symbol(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")


def another_one(var_answer):
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    symbol = operations[operation_symbol]
    second_answer = symbol(var_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    return second_answer


Total = first_answer
restart = True
while restart:
    user_var = input(f"Type 'y' to continue calculating with {Total}, or type 'n' to exit.: ").lower()
    if user_var == "n":
        restart = False
    else:
        answer = another_one(Total)
        Total = answer
