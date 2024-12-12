# scenario 1: Single Inheritance

#scenario : Employee and Manager
# You are tasked with creating an Employee class that contains general information about employees (name, age, salary).
# Now, create a Manager class that inherits from Employee and adds a department attribute.
# The Manager class should also have a method to display both employee and department details.

# Tasks:
# Implement the Employee class with attributes name, age, salary.
# Implement the Manager class inheriting from Employee and add the department attribute.
# Create instances of both classes and test.

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department

    def display(self):
        return f"Employee Details:\nDepartment:{self.department}\nName:{self.name}\nAge:{self.age}\nsalary:{self.salary}"
    

employ1=Employee("Amir",44,20000)
employ2=Employee("Habib",44,1000)
manager=Manager("Habib",44,1000,"Finance")
print(employ1.name)
print(employ2.name)
print(manager.display())


