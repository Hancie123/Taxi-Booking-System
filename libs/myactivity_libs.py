

class MyActivity():
    def __init__(self, myid=0,system=None, model=None, machine=None, processor=None, date=None, date2=None, cid=0 ):
        self.myid=myid
        self.system=system
        self.model=model
        self.machine=machine
        self.processor=processor
        self.date=date
        self.date2=date2
        self.cid=cid

    def getMyid(self):
        return self.myid

    def getSystem(self):
        return self.system

    def getModel(self):
        return self.model

    def getMachine(self):
        return self.machine

    def getProcessor(self):
        return self.processor

    def getDate(self):
        return self.date

    def getDate2(self):
        return self.date2

    def getCid(self):
        return self.cid

    #setter

    def setMyid(self, myid):
        self.myid=myid

    def setSystem(self, system):
        self.system=system

    def setModel(self, model):
        self.model=model

    def setMachine(self, machine):
        self.machine=machine

    def setProcessor(self, processor):
        self.processor=processor

    def setDate(self, date):
        self.date=date

    def setDate2(self, date2):
        self.date2=date2

    def setCid(self, cid):
        self.cid=cid


    def __str__(self):
        return ('{},{},{},{},{},{},{},{}'.format(self.myid, self.system, self.model, self.machine, self.processor, self.date, self.date2, self.cid))
