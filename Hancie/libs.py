
class Libs():
    def __init__(self, cid=0,name=None, dob=None, email=None, password=None):
        self.cid=cid
        self.name=name
        self.dob=dob
        self.email=email
        self.password=password

    #Getter
    def getCid(self):
        return self.cid

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    #setter
    def setCid(self, cid):
        self.cid=cid

    def setName(self, name):
        self.name=name

    def setDob(self, dob):
        self.dob=dob

    def setEmail(self, email):
        self.email=email

    def setPassword(self, password):
        self.password=password

    def __str__(self):
        return ('{},{},{},{},{}'.format(self.cid,
    self.name, self.dob, self.email, self.password))