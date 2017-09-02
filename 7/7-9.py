sandwich_orders = ["s","pastrami", "a", "pastrami", "n", "pastrami", "d"]
finished_sandwiches = []
print("We have no more pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(finished_sandwich + "!")
    finished_sandwiches.append(finished_sandwich)
print("Here are all of the finished sandwiches:")
for sandw in finished_sandwiches:
    print(sandw)