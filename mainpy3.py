# Program to make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    # Optional: handle division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Get input from user
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Perform calculations and display results
print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))
print("Quotient:", divide(num1, num2))
