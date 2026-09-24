def calculator():
    while True:
        print("\n=== Interactive Calculator & Unit Converter ===")
        print("1. Basic Calculator")
        print("2. Kilometers to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            while True:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error:
