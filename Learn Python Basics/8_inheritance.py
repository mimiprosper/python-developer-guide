class Person:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def eat(self):
        print("every body EATS")

    def walks(self):
        print('everyone WALKS')

    def sleeps(self):
        print('we all SLEEP at night')

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student(Person):
    rollNumber = '0'
    marks = '100'

    def takeExam(self):
        print('writes EXAMS')


student_1 = Student('emma', 30, 6, 'male')

# class Student inherits the function of Person
student_1.sleeps()
student_1.walks()
student_1.eat()

student_1.takeExam()
