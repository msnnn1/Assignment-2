def count_numbers(lst):
    result = {}
    for num in lst:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

lst = list(map(int, input("Enter numbers: ").split()))
print(count_numbers(lst))