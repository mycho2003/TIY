class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print("We are " + self.name + ", and we serve " + self.type + " food.")

    def open_restaurant(self):
        print(self.name + " is now open!")

    def set_number_served(self, customers):
        self.served = customers

    def increment_number_served(self, customer):
        self.served += customer

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describeflavors(self):
        print("This ice cream stand has the following flavors: ")
        for flavor in self.flavors:
            print(flavor)

Rita = IceCreamStand("Rita's", "Gelato", ["Vanilla", "Chocolate", "Mix"])

Rita.describeflavors()

"""????"""

