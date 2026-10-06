# class Person:
#     def m1(self):
#         print("m1 in parent ")
#     def m2(self):
#         print("m2 in parent class")
#     def showdetails(self):
#         print("showdetails")
# class Student(Person):
#     def m1(self): #Redefine-completely modify/extend the functionality
#         super().m1() #overriding
#         print("inside child class m1")
#     def m3(self):
#         print("m3")
# s=Student()
# s.m1()
# s.m2()
# s.m3()
# s.showdetails()



# class Person:
#     def __init__(self):
#         self.name=input("Enter your name: ")
#         self.age=int(input("Enter your age: "))
#     def showdetails(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter your roll no: "))
#     def studentdetails(self):
#         super().showdetails()
#         print("Roll No: ",self.rollno)
# s=Student()
# s.studentdetails()



# class Company:
#     def __init__(self):
#         self.name=input("Enter company name: ")
#     def showdetails(self):
#         print("Company name: ",self.name)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("Enter id: "))
#         self.designation=input("Enter designation: ")
#         self.salary=int(input("Enter salary: "))
#     def getsalary(self):
#         print("Salary of ",empid,":",self.salary)
#     def showemployeedetails(self):
#         print("Employee Id: ",self.empid)
#         print("Designation: ",self.designation)
#         print("Salary: ",self.salary)
# e=Employee()
# e.showdetails()
# e.showemployeedetails()








