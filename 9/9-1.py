class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("We are " + self.name + ", and we serve " + self.type + " food.")

    def open_restaurant(self):
        print(self.name + " is now open!")

restaurant = Restaurant("Twelves", "Italian")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()