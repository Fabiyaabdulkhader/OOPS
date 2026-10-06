#Define a class Book with the following descriptions:
#data members
#bookname,bookid,authorid,authorname,price,booktitle
#member methods
#getauthorid(),getauthorname(),getbooktitle(),getprice(),
#setauthorid(),setauthorname(),setbooktitle(),setprice()
#create two objects and call the above methods

class Book:
    def __init__(self):
        self.bname=input("Enter bookname: ")
        self.bid=input("Enter bookid: ")
        self.aid=input("Enter authorid: ")
        self.aname=input("Enter authorname: ")
        self.price=float(input("Enter price: "))
        self.btitle=input("Enter booktitle: ")
    def getauthorid(self):
        print("Author id: ",self.aid)
    def getauthorname(self):
        print("Author name: ",self.aname)
    def getbooktitle(self):
        print("Book title: ",self.btitle)
    def getprice(self):
        print("Price: ",self.price)
    def setauthorid(self):
        self.aid=input("Enter new author id: ")
        self.getauthorid()
    def setauthorname(self):
        self.aname=input("Enter new author name: ")
        self.getauthorname()
    def setbooktitle(self):
        self.btitle=input("Enter new book title: ")
        self.getbooktitle()
    def setprice(self):
        self.price=int(input("Enter new book price: "))
        self.getprice()
print("Enter details of book 1")
b=Book()
print("Enter details of book 2")
b1=Book()
print("   Book 1 Details    ")
b.getauthorid()
b.getauthorname()
b.getbooktitle()
b.getprice()
print("   Book 2 Details    ")
b1.getauthorid()
b1.getauthorname()
b1.getbooktitle()
b1.getprice()
print("   Update book 1 Details   ")
b.setauthorid()
b.setauthorname()
b.setbooktitle()
b.setprice()
print("   Updated Details   ")
b.getauthorid()
b.getauthorname()
b.getbooktitle()
b.getprice()


