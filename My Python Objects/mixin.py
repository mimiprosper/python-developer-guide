
class Employee:
    __slots__ = ("name", "age", "salary")
    
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
# test method resolution order        
    def has_slot(self):
        return hasattr(self, "__slots__")

# multiply inheritance and method resolution
class SlotsInspectionMixin:
    def has_slot(self):
     return hasattr(self, "__slots__")
 
               
class Developer(SlotsInspectionMixin, Employee):
    __slots__ = ("framework")
    
    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus


Employee = Developer("ben", 55, 2000, "flask")
print(Employee.has_slot())
# test method resolution order  
print(Developer.__mro__)
