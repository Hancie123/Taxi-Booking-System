
class Driver_Libs():
    def __init__(self, did=0, name=None, mobile=None, email=None,license=None, password=None, status=None):
        self.did=did
        self.name=name
        self.mobile=mobile
        self.email=email
        self.license=license
        self.password=password
        self.status=status

    #getter
    def getDid(self):
        return self.did

    def getName(self):
        return self.name

    def getMobile(self):
        return self.mobile

    def getEmail(self):
        return self.email

    def getLicense(self):
        return self.license

    def getPassword(self):
        return self.password

    def getStatus(self):
        return self.status

    #setter
    def setDid(self, did):
        self.did=did

    def setName(self, name):
        self.name=name

    def setMobile(self, mobile):
        self.mobile=mobile

    def setEmail(self, email):
        self.email=email

    def setLicense(self, license):
        self.license=license

    def setPassword(self, password):
        self.password=password

    def setStatus(self, status):
        self.status=status

    def __str__(self):
        return ('{},{},{},{},{},{},{}'.format(self.did, self.name, self.mobile, self.email, self.license, self.password, self.status))


