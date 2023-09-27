class Employee:

    # Name Mangling in __salary in line 29, 35 it blocks execution on line 44

    # passing self to instantiate method
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    # turning instance to a string that is readable
    def __str__(self):
        return f"{self.name} is {self.age} years old, is a {self.position} with a {self.salary} salary "

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('miminuim wage is 1000')
        # not public attribute via name mangling
        self.__salary = salary

    def get_salary(self):
        # return f"${self.salary}"
        # return round(self.salary, 2)
        return self.__salary  # not public attribute via name mangling


# employee1 & employee2 instances
employee1 = Employee("emma", 45, "software developer", 1200)
employee2 = Employee("Mpappe", 35, "tester", 1000)

# employee1.set_salary(2000)
# print(employee1.get_salary())

print(employee1.__salary)
