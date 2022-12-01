

class Admin_Libs():
    def __init__(self, aid=0, name=None, dob=None, email=None, mobile=None, address=None, password=None):
        self.aid=aid
        self.name=name
        self.dob=dob
        self.email=email
        self.mobile=mobile
        self.address=address
        self.password=password

    def getAid(self):
        return self.aid

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def getEmail(self):
        return self.email

    def getMobile(self):
        return self.mobile

    def getAddress(self):
        return self.address

    def getPassword(self):
        return self.password


    def setAid(self, aid):
        self.aid=aid

    def setName(self, name):
        self.name=name

    def setDob(self, dob):
        self.dob=dob

    def setEmail(self, email):
        self.email=email

    def setMobile(self, mobile):
        self.mobile=mobile

    def setAddress(self, address):
        self.address=address

    def setPassword(self, password):
        self.password=password

    def __str__(self):
        return ('{},{},{},{},{},{},{}'.format(self.aid, self.name, self.dob, self.email, self.mobile, self.address, self.password))


