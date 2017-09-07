class Car:
    def __init__(self, make, model, year):
        self.make = make
        self. model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = self.year, " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has ", self.odometer, " miles on it.")

    def update_odometer(self, milage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("This is not mathematically possible, are you from our world?")

    def increment_odometer(self, miles):
        self.odometer += miles

class Battery:
    def __init__(self, size=70):
        self.size = size

    def describe(self):
        print("This car has a battery size of ", self.size, "kWh")

    def get_range(self):
        if self.size == 70:
            range = 240
        elif self.size == 85:
            range = 270

        print("This car can go approximately ", range, " miles on a full charge.")

    def upgrade(self):
        if self.size != 85:
            self.size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

Nicolas = ElectricCar("Tesla", "Odd", 2003)

Nicolas.battery.get_range()
Nicolas.battery.upgrade()
Nicolas.battery.get_range()