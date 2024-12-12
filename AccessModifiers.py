#  Scenario 1: Public Access Modifier

# Scenario: Bank Account
#  Create a BankAccount class that contains three public attributes: account_number, account_holder, and balance.
# Allow the balance to be directly accessed and modified from outside the class.

# Tasks:
#  Implement the BankAccount class with the account_number, account_holder, and balance attributes as public.
#  Write methods to display and modify the balance directly.
#  Create an instance of BankAccount, access its attributes, and modify the balance outside the class.

# Expected Output:
#  You should be able to directly modify account_number and balance from outside the class.
# The methods should work without restrictions.

# class BankAccount:
#     def __init__(self,account_number,account_holder,balance):
#         self.account_number=account_number #public 
#         self.account_holder=account_holder #public
#         self.balance=balance #public

#     def displayBalance(self):
#         return f"Current Balance : {self.balance}"

#     def modifyBalance(self,new_balance):
#         self.balance=new_balance
#         return f"Balance updated : {self.balance}"


# account =BankAccount("12345678","Amir",1000)

# print("Initial Account Details:")

# print(f"Account Number:{account.account_number}")
# print(f"Account Holder:{account.account_holder}")
# print(account.displayBalance())

# account.balance+=100


# account.modifyBalance(account.balance+10000)
# print(account.displayBalance())

# Scenario 2: Protected Access Modifier

# Scenario: Student Information
# Create a class Student with protected attributes _name and _age.
# Implement a method display_info() that prints the name and age of the student.
# Create a subclass GraduatedStudent that inherits from Student, and add a method get_graduation_year() to access the protected attributes from the parent class.
# Demonstrate how to access the protected attributes from within the class and subclass, and attempt to access them directly from outside the class.

# Tasks:
# Implement the Student class with protected attributes _name and _age.
# Implement the display_info() method.
# Implement the GraduatedStudent subclass, adding the get_graduation_year() method to access the protected attributes.
# Create instances of both classes and demonstrate attribute access within and outside the class.

# Expected Output:
# You can access the protected attributes from within the subclass.
# Attempting to access protected attributes directly from outside the class should issue a warning or allow access with caution.

class StudentInfo:
    def __init__(self,name,age):
        self._name=name #protected
        self._age=age #protected

    def displayInfo(self):
        return f"Name:{self._name}\nAge:{self._age}"    

class graduatedStudent(StudentInfo):
    def __init__(self,name,age,gratuationYear):
        super().__init__(name,age)
        self.gratuationYear=gratuationYear

    def getGraduationYear(self):
        return f"Name:{self._name}\nAge:{self._age}\nGratuation Year :{self.gratuationYear}"    


student=StudentInfo("Amir",54) 
Graduation=graduatedStudent("Amir",54,2025)
print(Graduation.getGraduationYear())

print(student._name)
# print(student.displayInfo())

# Scenario 3: Private Access Modifier

# Scenario: Company Employee
# Create a class Employee with private attributes __name and __salary.
# Define methods to set (set_salary()) and get (get_salary()) the private attribute __salary.
# Demonstrate how the private attributes can only be accessed via getter and setter methods, and show what happens when you try to access them directly from outside the class.

# Tasks:
# Implement the Employee class with private attributes __name and __salary.
# Implement the set_salary() and get_salary() methods to modify and access the private attributes.
# Create an instance of Employee and demonstrate how private attributes can be accessed using the methods and what happens when you try to access them directly.

# Expected Output:
# Direct access to private attributes should raise an AttributeError.
# The private attributes should only be accessible via methods like get_salary() and set_salary().

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def setSalary(self,newSalary):
        self.__salary=newSalary
        return f"Updated Sallary:{self.__salary}"

    def get_salary(self):
        return(f" Name is:{self.__name}\nYour salary is: {self.__salary}")
                

    

employee=Employee("Kamran",100)
print(employee.get_salary())
print(employee.setSalary(100000))

