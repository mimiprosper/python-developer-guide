class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def print_name(self):
        print(self.firstName, self.lastName)


# instance if the class Person
teacher = Person('Jane', 'Wilson')
teacher.print_name()


# inheritance from class person
class Lawyer(Person):
    pass


# instance of the class Lawyer
barrister_john = Lawyer('emma', 'gills')
barrister_john.print_name()


# inheritance from class person
class Doctor(Person):

    # this overrides the method of the parent class Person
    def __init__(self, firstname, lastname, gender):
        Person.__init__(self, firstname, lastname)
        self.firstName = firstname
        self.lastName = lastname
        self.gender = gender

    # class Doctor's method
    def print_info(self):
        print('Hello my name is', self.firstName, self.lastName, 'am a', self.gender)


doctor_who = Doctor('josh', 'shaw', 'male')
doctor_who.print_info()  # class Doctor's method

# class Doctor inherits class Person's method
doctor_who.print_name()
