moods = ["pizza", "falafel", "carrot cake"]
foods = moods[:]
moods.append("cannoli")
foods.append("ice cream")
print("Foods I like: \n")
for food in moods:
    print(food)
print("\nFoods my friend likes: \n")
for food in foods:
    print(food)