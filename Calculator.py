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


def calculator():
    operations = {"+": add, "-": subtract, "*": Multiply, "/": Division}

    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    restart = True
    while restart:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        symbol = operations[operation_symbol]

        answer = symbol(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_var = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to exit or type 't' to try again.: ").lower()
        if user_var == "y":
            num1 = answer
        elif user_var == "t":
            restart = False
            calculator()
        else:
            restart = False


calculator()
