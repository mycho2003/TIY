pet = {"name": "mojo", "color": "brown", "age": 4, "species": "dog"}
pet_0 = {"name": "goldie", "color": "rainbow", "age": 1, "species": "goldfish"}
pet_1 = {"name": "bob", "color": "white", "age": 1000, "species": "rock"}
pets = [pet, pet_0, pet_1]

for animal in pets:
    print("Name: " + animal["name"].title() + "\nColor: " + animal["color"].title() + "\nAge: ", animal["age"], "\nThis pet is a " + animal["species"] + "\n")
