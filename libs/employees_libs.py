
class EmployeesLibs():
    def __init__(self, emid=0, name=None, dob=None, gender=None, mobile=None, email=None, address=None):
        self.emid=emid
        self.name=name
        self.dob=dob
        self.gender=gender
        self.mobile=mobile
        self.email=email
        self.address=address


    def getEmid(self):
        return self.emid

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def getGender(self):
        return self.gender

    def getMobile(self):
        return self.mobile

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address


    def setEmid(self,emid):
        self.emid=emid

    def setName(self, name):
        self.name=name

    def setDob(self, dob):
        self.dob=dob

    def setGender(self, gender):
        self.gender=gender

    def setMobile(self, mobile):
        self.mobile=mobile

    def setEmail(self, email):
        self.email=email

    def setAddress(self, address):
        self.address=address

    def __str__(self):
        return ('{},{},{},{},{},{},{}'.format(self.emid, self.name, self.dob,self.gender,self.mobile,self.email, self.address))
