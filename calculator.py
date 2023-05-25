#Calculator

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# User inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
result = addition(num1, num2)
print("Addition:", result)

# Subtraction
result = subtraction(num1, num2)
print("Subtraction:", result)

# Multiplication
result = multiplication(num1, num2)
print("Multiplication:", result)

# Division
result = division(num1, num2)
print("Division:", result)
