print("=== Python Calculator ===")

while True:
    print("\nChoose operation:")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")
    print("q  Quit")

    op = input("Enter operation: ")

    if op.lower() == "q":
        print("Calculator closed. Peace ✌️")
        break

    if op not in ["+", "-", "*", "/"]:
        print("Invalid operation. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero 💀")
                continue
            result = num1 / num2

        print("Result =", result)

    except ValueError:
        print("Bro… enter numbers only 🤦‍♂️")
