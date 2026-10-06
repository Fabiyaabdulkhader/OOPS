# write a menu-driven python program for a banking system using a class
# Account to perform the following operations:
#
# 1.create an account
# 2.withdraw money
# 3.deposit money
# 4.display balance
# 5.exit
#
# store account details in a list and search accounts using the
# account number.
# display "Account Not Found" if the account does not exist


class Account():
    def __init__(self):
        self.accno=int(input("Enter Account Number: "))
        self.accname=input("Enter Account Holder Name: ")
        self.balance=float(input("Enter Balance: "))
    def withdraw(self):
        amount=float(input("Enter Amount to Withdraw: "))
        self.balance=self.balance-amount
        self.showbalance()
    def deposit(self):
        amount=float(input("Enter Amount to Deposit: "))
        self.balance=self.balance+amount
        self.showbalance()
    def showbalance(self):
        print("Balance amount =",self.balance)
l=[]
while(1):
    print("Menu Driven Program")
    print("1.Create an account")
    print("2.Withdraw Money")
    print("3.Deposit Money")
    print("4.Display Balance")
    print("5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        a=Account()
        l.append(a)
        #print(l)
    elif ch==2:
        num=int(input("Enter Account Number: "))
        for i in l:
            if i.accno==num:
                i.withdraw()
                break
        else:
            print("Account Not Found")
    elif ch==3:
        num = int(input("Enter Account Number: "))
        for i in l:
            if i.accno == num:
                i.deposit()
                break
        else:
            print("Account Not Found")
    elif ch==4:
        num = int(input("Enter Account Number: "))
        for i in l:
            if i.accno == num:
                i.showbalance()
                break
        else:
            print("Account Not Found")
    elif ch==5:
        exit()









# class Person:
#     def __init__(self):
#         self.name = input("Enter Name: ")
#         self.age = int(input("Enter Age: "))
#
#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno = int(input("Enter Roll Number: "))
#
#     def show_studentdetails(self):
#         print("Roll Number:", self.rollno)
#
#
#
# s = Student()
#
#
# s.show_details()
# s.show_studentdetails()