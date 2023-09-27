# parent class Person 
class Person():
    def __init__(self, name, age, color, weight, ) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
        
    # method of parent class
    def info(self):
        print(f'{self.name}, am {self.age}, {self.color} in complexion')
     
    # method of parent class   
    def walk(self):
        print(f'{self.name} walks to the workshop every week days')
    
     # method of parent class     
    def pays(self):
        print(f' {self.name} pays taxes to the government')
    
    # method of parent class   
    def eat(self):
        print(f' {self.name} like to eat at home')
        
# class Teacher --> instantiation
class Teacher():
    def __init__(self, name='Sam Duru', subject='maths') -> None:
        self.name = name
        self.subject = subject
                
    def display_info(self):
        print(f' My teacher is {self.name} he is our {self.subject} teacher ')
    
    # method of class Teacher   
    def teach(self):
        print(f'My Teachers supervise, teach and mentor the students ')
        
# child class student --> inheritance       
class Student(Person):
    def __init__(self, name, age, color, weight) -> None:
        super().__init__(name, age, color, weight)
        
    # using an instance of class Teacher
        self.teacher = Teacher()
     
    # method overriding of parent class
    def walk(self):
        print(f'{self.name} walks to school to learn')
        
    # method overiding of parent class
    def pays(self):
        print(f'{self.name} does not pay taxes')
        
    # method of child class
    def read(self):
        print('A student reads his books')
        
         
        
# create object of class student   
new_student = Student('abram', 33, 'dark', 75)
#new_student.pays()

# using the instantiation class Teacher methods
new_student.teacher.teach() 
new_student.teacher.display_info()
