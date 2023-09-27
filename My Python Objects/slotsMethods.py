from dataclasses import dataclass

# this also using inbuilt repr() for print out
@dataclass(slots = True)
class Project:
    name: str
    payment: int
    client : str
    
    def notify_client(self):
        print(f"notify client about the {self.name} change ")
    
class Employee:
    def __init__(self, name, age, salary, project) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project
      
p = Project("john", 8000, "cyborb")
# composition
e = Employee("luke", 45, 8000, p)
print(e.project)