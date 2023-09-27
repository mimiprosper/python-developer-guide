class Employee:
    
    # optimising memory with slots for parent class   
    __slots__ = ("name", "age", "salary")
    
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        
        
class Developer(Employee):
    # optimising memory with slots for child class 
    __slots__ = ("framework", )
    
    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus
               
        
employee1 = Developer("dan", 35, 20000, "flask")
print(employee1.__slots__)