

class Driver():
    def __init__(self, did=0, name=None, licenseno=None):
        self.did=did
        self.name=name
        self.licenseno=licenseno

    #Getters
    def getDid(self):
        return self.did

    def getName(self):
        return self.name

    def getLicenseno(self):
        return self.licenseno

    #Setters

    def setDid(self, did):
        self.did=did

    def setName(self, name):
        self.name=name

    def setLicenseno(self, licenseno):
        self.licenseno=licenseno

    #toString
    def __str__(self):
        return ("{},{},{}".format(self.did, self.name,self.licenseno))
