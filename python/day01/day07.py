#ValueError - wrong value/type of value
#ZeroDivisionError - dividing by zero
#NameError - using a variable that doesn't exist

#try:
 #   number = 10/0
  #  print(number)

#except ZeroDivisionError:
 #   print("cannot divide by zero")

#import calculator

#print(calculator.add(10, 5))
#print(calculator.multiply(4, 3))


#from calculator import subtract

#result = subtract(20, 8)

#print(result)

#math.ceil() - ceil() means round UP to the next whole number

#import math

#print(math.ceil(7.1))

#math.floor() - floor() does the opposite - it rounds DOWN

#import math

#print(math.floor(7.9))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    result = None

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        try:
            result = divide(num1, num2)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    
    else:
        print("Invalid operation")

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")
