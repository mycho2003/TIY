sandwich_orders = ["s", "a", "n", "d"]
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(finished_sandwich + "!")
    finished_sandwiches.append(finished_sandwich)
print("Here are all of the finished sandwiches:")
for sandw in finished_sandwiches:
    print(sandw)