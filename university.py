#assignment 
#University system display information of
#Classes: person(super class), and subclasses:Student, lecturer and staff
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
     print( f"Name: {self.name}, Age: {self.age}")
     
class Student(Person):
    def __init__(self, name, age, student_id, course, year ,CGPA):
       
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.CGPA = CGPA
        
        
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}course: {self.course}, Year: {self.year}, CGPA: {self.CGPA}")
class Lecturer(Person):
    def __init__(self, name, age, employee_id, department, salary):
        
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_info(self):
        
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}, salary: {self.salary}")
class Staff(Person):
    def __init__(self, name, age, employee_id, position, salary):
        
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def display_info(self):
    
        print(f"Staff Name: {self.name}, Age:{self.age}, Employee ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary}")
        
        #creating objects
        
        
student1 = Student("Leo", 21, "S12345", "software engineering",3, 4.8)
lecturer1 = Lecturer("Dr.Jeff", 45, "E67890", "Networks", 800000)
staff1 = Staff("John", 35, "E54321", "cleaner", 50000)
student1.display_info()
print()
lecturer1.display_info()
print()
staff1.display_info()