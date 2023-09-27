class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


# inheritance
class Tester(Employee):
    def run_tests(self):
        print(f"testing is started be {self.name} ...")
        print("test are done")
        
        
# inheritance       
class Developer(Employee):
    # method overriding
    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus
        
employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("greg", 45, 40000)

employee2.increase_salary(20, 30)
print(employee2.salary)
