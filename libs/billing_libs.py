
class BillingLibs():
    def __init__(self, billingid=0, name=None, km=None, unit=None, total=None, bookingid=None, date=None):
        self.billingid=billingid
        self.name=name
        self.km=km
        self.unit=unit
        self.total=total
        self.bookingid=bookingid
        self.date=date

    def getBillingid(self):
        return self.billingid

    def getName(self):
        return self.name

    def getKm(self):
        return self.km

    def getUnit(self):
        return self.unit

    def getTotal(self):
        return self.total

    def getBookingid(self):
        return self.bookingid

    def getDate(self):
        return self.date


    def setBilling(self, billingid):
        self.billingid=billingid

    def setName(self, name):
        self.name=name

    def setKm(self, km):
        self.km=km

    def setUnit(self, unit):
        self.unit=unit

    def setTotal(self, total):
        self.total=total

    def setBookingid(self, bookingid):
        self.bookingid=bookingid

    def setDate(self, date):
        self.date=date


    def __str__(self):
        return ('{},{},{},{},{},{},{}'.format(self.billingid, self.name, self.km, self.unit, self.total, self.bookingid, self.date))






