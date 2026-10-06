# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student():
    def __init__(self):
        self.rollno=int(input("Enter Roll Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Marks: "))

    def updateMarks(self):
        self.marks=float(input("Enter New Marks: "))

    def display(self):
        print("Roll Number: ", self.rollno)
        print("Name: ", self.name)
        print("Marks: ", self.marks)
l=[]
while(1):
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        a=Student()
        l.append(a)
    elif ch==2:
        num=int(input("Enter Roll Number: "))
        for i in l:
            if i.rollno==num:
                i.updateMarks()
                print("Mark Updated Successfully")
                break
        else:
            print("Student Not Found")
    elif ch==3:
        for i in l:
                i.display()
                print()
    elif ch==4:
        num = int(input("Enter Roll Number: "))
        for i in l:
            if i.rollno == num:
                i.display()
                break
        else:
            print("Student Not Found")
    elif ch==5:
        num = int(input("Enter Roll Number: "))
        for i in l:
            if i.rollno == num:
                l.remove(i)
                print("Deleted")
                break
        else:
            print("Student Not Found")
    elif ch==6:
        exit()