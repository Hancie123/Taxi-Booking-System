
class c2():
    def __init__(self):
        self.n1=None
        self.n2=None
        self.n3=None

    def setN1(self,n1):
        self.n1=n1

    def getN1(self):
        return self.n1

    def setN2(self,n2):
        self.n2=n2

    def getN2(self):
        return self.n2

    def setN3(self,n3):
        self.n3=n3

    def getN3(self):
        return self.n3

    def __str__(self):
        return str(self.n1 +self.n2 + self.n3)



