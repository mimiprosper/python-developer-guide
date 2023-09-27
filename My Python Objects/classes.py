class Employee:

    # passing self to instantiate method
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    # magic method, special method, dunder method
    # turning instance to a string that is readable
    def __str__(self):
        return f"{self.name} is {self.age} years old, is a {self.position} with a {self.salary} salary "

    # magic method, special method, dunder method
    # turning instance to a string that is readable with upper commas
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
        
    # magic method, special method, dunder method example - double underscores on both sides
    def __add__(self, other_employee):
        # Eg combines their age and returns a new Employee
        return Employee("Charles", self.age + other_employee.age, "dev", 2000)


# employee1 & employee2 instances
employee1 = Employee("emma", 45, "software developer", 200000)
employee2 = Employee("Mpappe", 35, "tester", 100000)

print(employee1)
#print(repr(employee1))
#print(eval(repr(employee1)))

#employee3 = employee1.__add__(employee2)
#employee3 = employee1 + employee2
#print(employee3)

#print(eval("2 + 3"))