# My first class
# class Person:
#     name = ''
#     age = ''
#     height = 0
#     gender = ''
#
#     def eat(self):
#         print("every body eats")
#
#     def walks(self):
#         print('everyone walks')
#
#     def sleeps(self):
#         print('we all sleep at night')
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age


# class constructor
class Person:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def eat(self):
        print("every body eats")

    def walks(self):
        print('everyone walks')

    def sleeps(self):
        print('we all sleep at night')

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
