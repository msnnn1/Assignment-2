def find_country(countries, search):
    if search in countries:
        return countries.index(search)
    else:
        return "Not Found in List"

countries = input("Enter countries: ").split()
search = input("Enter country to search: ")
print(find_country(countries, search))