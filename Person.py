# parent class Person 
class Person():
    def __init__(self, name, age, color, weight, ):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
        
    # method of parent class
    def info(self):
        print(f'{self.name}, am {self.age}, {self.color} in complexion')
     
    # method of parent class   
    def walk(self):
        print(f'{self.name} can walk')
    
     # method of parent class     
    def pays(self):
        print(f' {self.name} pays taxes to the government')
    
    # method of parent class   
    def eat(self):
        print(f' {self.name} like to eat at home')
        
        
        
# class Result --> instantiation
class Result():
    def __init__(self, score=200, grade="2nd", remark="very good"):
        self.score = score
        self.grade = grade
        self.remark = remark
        
    def show_result(self, name):
        self.name = name
        print(f' {self.name} Result: score = {self.score}, grade = {self.grade}, remarks = {self.remark} ')
        
       
# child class student --> inheritance       
class Student(Person):
    def __init__(self, name, age, color, weight) :
        super().__init__(name, age, color, weight)
        
    # using an instance of class Result
        self.result = Result()
     
    # method overriding of parent class Person
    def walk(self):
        print(f'{self.name} walks to school to learn')
        
    # method overiding of parent class Person
    def pays(self):
        print(f'{self.name} does not pay taxes, still a student')
        
    # method of child class
    def read(self):
        print('A student reads his books')
        
         
# overriding method of parent class Person
# new_student.pays()

# call method of the child class
# new_student.read()
