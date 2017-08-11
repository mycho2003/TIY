cities = {"Jamestown": {"country": "USA", "population": 3, "fact": "First colony in America"},
          "Michaelville": {"country": "South Korea", "population": 4, "fact": "A lot of math"},
          "Isabellapolis": {"country": "France", "population": 5, "fact": "Recognized for art"}}

for city, info in cities.items():
    print("City: " + city + "\nFacts: ")
    for category, fact in info.items():
        print(category.title() + ": " + str(fact))
    print("\n")