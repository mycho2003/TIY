vacation = {}
people = 0
while True:
    name = input("What is your name?").title()
    dream = input("What is the one place in the world you would like to go to the most?").title()
    vacation[name] = dream
    people += 0
    if people > 5:
        break
for person, place in vacation:
    print(person + " wants to go to " + place)
