person = {"first_name": "Michael", "last_name": "Cho", "age": 15, "city": "Seoul"}
person_0 = {"first_name": "Josh", "last_name": "Nam", "age": 16, "city": "New York"}
person_1 = {"first_name": "Austin", "last_name": "Goldberg", "age": "8", "city": "Jamestown"}
people = [person, person_0, person_1]

for persons in people:
    print("Name: " + persons["first_name"] + " " + persons["last_name"] + "\nCity: " + persons["city"] + "\n")