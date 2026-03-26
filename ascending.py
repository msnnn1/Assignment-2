numbers = list(map(int, input("Enter numbers: ").split()))
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(unique_numbers)