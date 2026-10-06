# 1.Create a class named Circle with an attribute radius.
#Use a constructor to initialize the radius by accepting input from the user.
#Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.

class Circle:
    def __init__(self):
        self.radius=float(input("Enter Radius: "))
    def getarea(self):
        area=3.14*self.radius*self.radius
        print("Area =",area)
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print("Perimeter =",perimeter)

c=Circle()
c.getarea()
c.getperimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.accno=input("Enter Account Number: ")
        self.accname=input("Enter Account Holder Name: ")
        self.balance=float(input("Enter Balance: "))
    def withdraw(self):
        amount=float(input("Enter Amount to Withdraw: "))
        self.balance=self.balance-amount
    def deposit(self):
        amount=float(input("Enter Amount to Deposit: "))
        self.balance=self.balance+amount
    def showbalance(self):
        print("Current Balance =",self.balance)

a=Account()
#a.showbalance()
b=Account()
#b.showbalance
l=[a,b]
for i in l:
    print(f"Account number: {i.accno} Name: {i.accname} Balance: {i.balance}")