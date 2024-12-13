#Designing SSC and FSC Detailed Marks Certificate in Python

#Data Input
class Student:
    def __init__(self,name,fatherName,rollNumber,school,boardName,yearOfPassing):
        self.name=name
        self.fatherName=fatherName
        self.rollNumber=rollNumber
        self.school=school
        self.boardName=boardName
        self.yearOfPassing=yearOfPassing
        self.marks={}
        self.totalMarks=0
        self.percentage=0
        self.grade=""

    def inputMarks(self,subjects):
        print(f"Enter Marks for {self.name}:")
        for subject in subjects:
            while True:
                try:
                    mark=float(input(f"{subject}: "))
                    if 0<=mark<=100:
                        self.marks[subject]=mark
                        break
                    else:
                        print("Marks should be in between 0 and 100.")

                except ValueError:
                    print("Invalid input. Please enter a number")

    def calculateResults(self):
        self.totalMarks=sum(self.marks.values())
        self.percentage=(self.totalMarks / (len(self.marks)*100))*100
        if self.percentage>=90:
            self.grade="A++"
        elif self.percentage>=80:
            self.grade="A"                             
        elif self.percentage>=70:
            self.grade="B"                             
        elif self.percentage>=60:
            self.grade="C"                             
        else:
            self.grade="Fail"                             
    
    def generateCertificate(self):
        header=f"Board:{self.boardName}\nSchool/College{self.school}\nYear of Passing: {self.yearOfPassing}\n"
        studentInfo=f"Name:{self.name}\nFather's Name:{self.fatherName}\nRoll Number:{self.rollNumber}\n"
        marksTable="Subjects          Marks\n"
        for subject,mark in self.marks.items():
            marksTable+=f"{subject:<15} {mark}\n"

        footer=f"Total Marks{self.totalMarks}\nPercentage:{self.percentage}\nGrade:{self.grade}\n"

        certificate=f"{header}\n{studentInfo}\n{marksTable}\n{footer}\n"
        print(certificate)
        return certificate

    def saveCertificate(self):
        fileName=f"DMC {self.rollNumber}.txt"
        with open(fileName,"w") as file:
            file.write(self.generateCertificate())
        print(f"Certificate save as {fileName}.")


class SSC_student(Student):
    def __init__(self, name, fatherName, rollNumber, school, boardName, yearOfPassing):
        super().__init__(name, fatherName, rollNumber, school, boardName, yearOfPassing)
        self.subjects=["English", "Urdu", "Mathematics", "Science", "Islamiyat", "Pakistan Studies"]


class FSC_student(Student):
    def __init__(self, name, fatherName, rollNumber, school, boardName, yearOfPassing):
        super().__init__(name, fatherName, rollNumber, school, boardName, yearOfPassing)
        self.subjects = ["English", "Urdu", "Physics", "Chemistry", "Biology/Mathematics", "Computer Science"]

def main():
    print("Marksheet Generator")
    print("1. SSC Student\n2. FSC Student")
    choice=input("Enter Your Choice: ")

    if choice=="1":
        student=SSC_student(
            input("Name: "),
            input("Father's Name: "),
            input("Roll Number: "),
            input("School Name: "),
            input("Board Name: "),
            input("Year of Passing: "),
        )
        student.inputMarks(student.subjects)
        student.calculateResults()
        student.generateCertificate()
        student.saveCertificate()
    elif choice=="2":
        student=FSC_student(
            input("Name: "),
            input("Father's Name: "),
            input("Roll Number: "),
            input("College Name: "),
            input("Board Name: "),
            input("Year of Passing: "),
        )
        student.inputMarks(student.subjects)
        student.calculateResults()
        student.generateCertificate()
        student.saveCertificate()
    else:
        print("Invalid Choice.")

if __name__=="__main__":
    main()