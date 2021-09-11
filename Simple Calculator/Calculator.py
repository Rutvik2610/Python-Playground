from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    is_calculating = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while is_calculating:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type '1' to continue calculating with {answer}"
                       f"\nType '2' to start a new calculation\nType '3' to exit:\n").lower()
        if choice == "1":
            num1 = answer
        elif choice == "2":
            calculator()
        elif choice == "3":
            is_calculating = False
            return


calculator()
