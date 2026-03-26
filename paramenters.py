def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

def floor_division(a, b):
    if b != 0:
        return a // b
    return "Cannot divide by zero"

def exponentiation(a, b):
    return a ** b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", addition(a, b))
print("Multiplication:", multiplication(a, b))
print("Division:", division(a, b))
print("Floor Division:", floor_division(a, b))
print("Exponentiation:", exponentiation(a, b))