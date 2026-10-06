#define a class named Employee with the following details.
#Data mambers:
#Empid,name,age,salary,designation,place
#member methods
#getsalary(),showpersondetails()
#Create two objects for the Employee class and call the above member methods.

class Employee:
    def __init__(self):
        self.empid=int(input("Enter your id: "))
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
        self.salary=int(input("Enter your salary: "))
        self.designation=input("Enter your designation: ")
        self.place=input("Enter your place: ")
    def getsalary(self):
        self.empid = int(input("Enter your id: "))
        print("salary of", self.empid ,"is: ",self.salary)         #return self.salary
    def showpersondetails(self):                                           #^
        print("Employee Details")                                          #|
        print("Employee id: ",self.empid)
        print("Name: ", self.name)                                         #|
        print("Age: ", self.age)
        print("salary: ", self.salary)
        print("Designation: ", self.designation)                           #|
        print("Place: ", self.place)
                                                                           #|
e=Employee()
                                                                  #print(e.getsalary())
e.getsalary()
e.showpersondetails()
e1=Employee()
e1.getsalary()
e1.showpersondetails()