fav_num = {"Michael": [3, 5], "Josh": [64, 1024], "Thomas": [5, 8], "Fake": [39867153, 1], "Ben": [1, 3]}

for person, numbers in fav_num.items():
    print("Name: " + person + "\nFavorite Numbers:")
    for num in numbers:
        print(num)
    print("\n")