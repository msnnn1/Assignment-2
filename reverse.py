def sort_reverse(names):
    return sorted(names, reverse=True)

names = input("Enter names: ").split()
print(sort_reverse(names))