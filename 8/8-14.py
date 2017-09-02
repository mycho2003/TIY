def car_d(manu, model, **other):
    car = {}
    car["manufacturer"] = manu
    car["model"] = model
    for key, value in other.items():
        car[key] = value
    return car
mecar = car_d("Toyota", "Axel", Color= "Red", Size= "Large")
print(mecar)