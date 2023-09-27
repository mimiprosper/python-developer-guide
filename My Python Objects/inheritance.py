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
    def increase_salary(self, percent, bonus):
        self.salary += self.salary * (percent/100)
        self.salary += bonus
        
     
employee1 = Tester("henderson", 40, 2000)
employee2 = Developer("paul", 55, 3000)

employee1.increase_salary(20)
print(employee1.salary)
employee1.run_tests()

employee2.increase_salary(20, 100)
print(employee2.salary)

