class Car:
    engineType = 'petrol'

    def __init__(self, model, weight):
        self.model = model
        self.weight = weight

    def printinfo(self):
        print('the car engine type', Car.engineType)


toyota = Car('japanese make', 24)
benz = Car('german make', 30)

# modifying an attribute
# benz.model = 'good european spec'

# delete an attribute
# del benz.weight

toyota.printinfo()
print(benz.model, benz.weight)
