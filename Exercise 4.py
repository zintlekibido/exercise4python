
# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruitlist= ["apple", "banana", "cherry", "orange", "pear"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruitlist:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    print(i**2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
while True:
    print("\nOptions:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to exit")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
        
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print(math_operations.add(num1, num2))
        elif user_input == "subtract":
            print(math_operations.subtract(num1, num2))
        elif user_input == "multiply":
            print(math_operations.multiply(num1, num2))
        elif user_input == "divide":
            print(math_operations.divide(num1, num2))
            
    else:
        print("Invalid input")
