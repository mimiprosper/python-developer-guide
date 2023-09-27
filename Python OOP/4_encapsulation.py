class Car:
    def __init__(self, speed, color):
        # underscore on speed & color make these attributes private
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        # underscore on speed & color make these attributes private... not accessible
        self.__speed = value

    def get_speed(self):
        # underscore on speed & color make these attributes private... not accessible
        return self.__speed


ford = Car(250, 'blue')
toyota = Car(300, 'green')
honda = Car(350, 'red')

# the set_speed method & speed attribute are used to reassign values to private attributes
ford.set_speed(600)
ford.speed = 800


print(ford.get_speed())
print(ford.speed)
# print(ford.color)
