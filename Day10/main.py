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

    previous_answer = None

    while True:

        if previous_answer:
            num1 = previous_answer
        else:
            num1 = float(input("What is the first number?: "))

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(answer)

        do_calculating = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ").lower()
        
        if do_calculating == "y":
            previous_answer = answer
        else:
            break
    
    calculator()

calculator()