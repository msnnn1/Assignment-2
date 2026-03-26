def is_armstrong(num_str):
    num = int(num_str)
    power = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** power
    if total == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

n = input("Enter number: ")
is_armstrong(n)