def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operators = {
    '1': ('+', add),
    '2': ('-', subtract),
    '3': ('*', multiply),
    '4': ('/', divide)
}

while True:
    num1 = float(input("Enter the first number: "))

    print("Select operation:")
    for key, (symbol, _) in operators.items():
        print(f"{key}. {symbol}")
    print("0. Exit")

    choice = input("Enter your choice (0-4): ")

    if choice == '0':
        break

    if choice not in operators:
        print("Invalid choice. Please try again.")
        continue

    num2 = float(input("Enter the second number: "))

    _, operation = operators[choice]
    result = operation(num1, num2)
    print(f"{num1} {operation.__name__} {num2} = {result}")
    print()

