class Hospital:
    def __init__(self):
        self.hname=input("Enter hospital name: ")
        self.location=input("Enter location: ")
    def showdetails(self):
        print("HOSPITAL DETAILS")
        print("Hospital name: ",self.hname)
        print("Location: ",self.location)
class Department:
    def __init__(self):
        self.dname=input("Enter department name: ")
        self.docname=input("Enter doctor name: ")
    def showdeptdetails(self):
        print("DEPARTMENT DETAILLS")
        print("Department name: ",self.dname)
        print("Doctor name: ",self.docname)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.pid=int(input("Enter patient id: "))
        self.pname=input("Enter patient name: ")
        self.gender=input("Enter gender: ")
        self.place=input("Enter place: ")
        self.admn_date=input("Enter admission date: ")
        self.dis_date=input("Enter discharge date: ")
    def fullsummary(self):
        print("PATIENT DETAILS")
        print("Patient ID: ",self.pid)
        print("Name:", self.pname)
        print("Gender:", self.gender)
        print("Place:", self.place)
        print("Admission Date:", self.admn_date)
        print("Discharge Date:", self.dis_date)
    def dischargedetails(self):
        print("DISCHARGE DETAILS")
        self.showdetails()
        self.showdeptdetails()
        self.fullsummary()
p=Patient()
p.dischargedetails()


