Pi = ["BBQ", "Pepperoni", "Cheese"]
for pizza in Pi:
    print("I really like " + pizza + " pizza")
print("I like pizza, but it makes my stomach hurt.")
friend_pizzas = Pi[:]
Pi.append("Flatbread")
friend_pizzas.append("Cheese Crust")
print("My favorite pizzas are: \n")
for pizza in Pi:
    print(pizza)
print("\nMy friend's favorite pizzas are: \n")
for fizza in friend_pizzas:
    print(fizza)