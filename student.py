#Define a class named Student with the following details:
#data members:
#sname,rollno,class,mark1,mark2,mark3.
#Member methods
#calculate(),Calculates the total and average
#showdetals()-displays the details of a student with average mark
#create one object for the class and call the above member methods

class Student:
    def __init__(self):
        self.sname=input("Enter student name: ")
        self.rollno=int(input("Enter rollno: "))
        self.sclass=input("Enter class: ")
        self.mark1=float(input("Enter mark1: "))
        self.mark2 = float(input("Enter mark2: "))
        self.mark3 = float(input("Enter mark3: "))
    def calculate(self):
        self.total=self.mark1+self.mark2+self.mark3
        self.average=self.total/3
    def showdetails(self):
        print("   Student Details    ")
        print("Student Name: ",self.sname)
        print("Roll No: ",self.rollno)
        print("Class: ",self.sclass)
        print("Mark 1: ",self.mark1)
        print("Mark 2: ",self.mark2)
        print("Mark 3: ",self.mark3)
        print("Total: ",self.total)
        print("Average: ",self.average)
s=Student()
s.calculate()
s.showdetails()


