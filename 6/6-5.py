rivco = {"Mississippi": "USA", "Nile": "Egypt", "Han": "South Korea"}

for river, country in rivco.items():
    print("The " + river + " river is located in " + country)

for river in rivco:
    print(river)

for country in rivco.values():
    print(country)
