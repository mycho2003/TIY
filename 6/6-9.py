favorite_places = {"Michael": ["Bryn Mawr", "School"], "Steff": ["Seoul"], "Bob": ["Paris", "Orlando", "Home"]}

for person, places in favorite_places.items():
    print("Name: " + person + "\nFavorite places:")
    for place in places:
        print(place)
    print("\n")
