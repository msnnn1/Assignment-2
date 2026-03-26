movies = {}
for i in range(3):
    print("Enter details for movie", i+1)
    title = input("Title: ")
    director = input("Director: ")
    year = input("Year: ")
    rating = input("Rating: ")
    movies[title] = {"Director": director, "Year": year, "Rating": rating}

for title, info in movies.items():
    print("\nTitle:", title)
    for key, value in info.items():
        print(key + ":", value)