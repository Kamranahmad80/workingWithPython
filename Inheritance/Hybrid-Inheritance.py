
# Scenario: Person, Student, PartTimeEmployee
# Create a Person class that contains general attributes like name and age.
# Create a Student class that inherits from Person and adds an attribute university.
# Create another class Employee that also inherits from Person and adds an attribute company.
# Finally, create a PartTimeEmployee class that inherits from both Student and Employee, representing someone who is both a student and a part-time employee.

# Tasks:
# Implement the Person class with attributes name and age.
# Implement the Student class inheriting from Person and adding the university attribute.
# Implement the Employee class inheriting from Person and adding the company attribute.
# Implement the PartTimeEmployee class inheriting from both Student and Employee.
# Create an instance of PartTimeEmployee and demonstrate the attributes and methods from all classes.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

class Student(Person):
    def __init__(self, name, age,university):
        Person.__init__(self,name, age)
        self.university=university


class Employee(Person):
    def __init__(self, name, age,company):
        Person.__init__(self,name, age)        
        self.company=company

class partTimeEmployee(Student,Employee):
    def __init__(self, name, age, university,company):
        Student.__init__(self,name,age,university)
        Employee.__init__(self,name,age,company)





partTime=partTimeEmployee("Amir",22,"Oxford","Microsoft")
print("Part Time Employee Details:")
print(f"Name:{partTime.name}\nAge:{partTime.age}\nUniversity:{partTime.university}\nCompany:{partTime.company}")
