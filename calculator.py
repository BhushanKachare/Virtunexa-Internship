import math

def calculator():
    history = []  # To store calculation history

    while True:
        print("\nOptions: add (+), subtract (-), multiply (*), divide (/), modulus (%), exponentiation (**), square root (sqrt), quit")
        operation = input("Enter operation: ").strip().lower()

        if operation == 'quit':
            confirm = input("Are you sure you want to quit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Exiting calculator.")
                break
            else:
                continue

        if operation == 'sqrt':
            try:
                num = float(input("Enter the number: "))
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                else:
                    result = math.sqrt(num)
                    print(f"Result: {result}")
                    history.append(f"sqrt({num}) = {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation in ('add', '+'):
                result = num1 + num2
                print(f"Result: {result}")
                history.append(f"{num1} + {num2} = {result}")
            elif operation in ('subtract', '-'):
                result = num1 - num2
                print(f"Result: {result}")
                history.append(f"{num1} - {num2} = {result}")
            elif operation in ('multiply', '*'):
                result = num1 * num2
                print(f"Result: {result}")
                history.append(f"{num1} * {num2} = {result}")
            elif operation in ('divide', '/'):
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"Result: {result}")
                    history.append(f"{num1} / {num2} = {result}")
            elif operation in ('modulus', '%'):
                result = num1 % num2
                print(f"Result: {result}")
                history.append(f"{num1} % {num2} = {result}")
            elif operation in ('exponentiation', '**'):
                result = num1 ** num2
                print(f"Result: {result}")
                history.append(f"{num1} ** {num2} = {result}")
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Save history to a file
    with open('calculation_history.txt', 'w') as file:
        file.write("Calculation History:\n")
        for entry in history:
            file.write(entry + "\n")

    print("Calculation history saved to 'calculation_history.txt'.")

calculator()
