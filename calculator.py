print("select operation to perform")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter operation (1/2/3/4): ")


if operation == "1":
    # Code for addition
    print("Addition selected")
elif operation == "2":
    # Code for subtraction
    print("Subtraction selected")
elif operation == "3":
    # Code for multiplication
    print("Multiplication selected")
elif operation == "4":
    # Code for division
    print("Division selected")
else:
    # Handle invalid operation
    print("Invalid operation")

operation = input()

if operation == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("Result:", result)
elif operation == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("Result:", result)
elif operation == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("Result:", result)
elif operation == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")


print("Go Sleep Now you Sangura")
