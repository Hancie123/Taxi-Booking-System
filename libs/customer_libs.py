
class Customer_Libs():
    def __init__(self, cid=0, name=None, dob=None, gender=None, mobile=None, email=None,
                 address=None, password=None, credit=None, status=None):
        self.cid=cid
        self.name=name
        self.dob=dob
        self.gender=gender
        self.mobile=mobile
        self.email=email
        self.address=address
        self.password=password
        self.credit=credit
        self.status=status

    #Getters
    def getCid(self):
        return self.cid

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

    def getPassword(self):
        return self.password

    def getCredit(self):
        return self.credit

    def getStatus(self):
        return self.status

    #setter
    def setCid(self, cid):
        self.cid=cid

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

    def setPassword(self, password):
        self.password=password

    def setCredit(self, credit):
        self.credit=credit

    def setStatus(self, status):
        self.status=status

    def __str__(self):
        return ('{},{},{},{},{},{},{},{},{},{}'.format(self.cid, self.name, self.dob, self.gender, self.mobile, self.email, self.address, self.password, self.credit, self.status))

