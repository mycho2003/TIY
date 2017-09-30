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