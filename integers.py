def calculate(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Quotient: Cannot divide by zero")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calculate(a, b)