class Car:
    
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = 15
        self.fuel_level = 10

    def drive(self):
        print('the car is moving')

    def fill_tank(self):
        if self.fuel_level == self.fuel_capacity:
            print('fuel tank is full!!!')
        else:
            print('fuel tank empty')

    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            #self.fuel_level = new_level
            print(f'tank within capacity {new_level} liters')
        else:
            print('The tank cannot hold that capacity')

    def add_fuel(self, amount):
        new_level = self.fuel_level + amount
        if new_level < self.fuel_capacity:
            print(f'level is now {new_level} liters')
        elif new_level == self.fuel_capacity:
            self.fill_tank()
        else:
            print('The tank cannot hold that much')

# class Battery --> creating an instantance of a class
class Battery():
    # a battery for an Electric car
    def __init__(self, size=70) -> None:
        # capacity in kwh
        self.size = size
        # charge level in percentage
        self.charge_level = 0

    def get_range(self):
        # return the battery range
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270


# inheritance 
class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year) 

        # using an instance of class Battery
        self.battery = Battery()

        # battery capacity in kwh
        self.battery_capacity = 15
        # change level in percentage
        self.battery_level = 0

    def charge(self):
        self.charge_level = 100
        print('battery is fully charged')

    # overriding the method in the super class
    def fill_tank(self):
        print('this car has no fuel tank')

# create object of ElectricCar
my_car = ElectricCar('telsa', 'Y-series', '2020')

# method of class Electriccar
my_car.charge()

# method of parent class, Car 
my_car.drive() 

# overiding method
my_car.fill_tank()

# using the instantiation class method
print(my_car.battery.get_range())

