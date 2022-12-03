
class BookingLibs():

    def __init__(self, bookingid=0, pickupaddress=None, date=None, time=None,dropoffaddress=None, bookingstatus=None, cid=None, did=None):

        self.bookingid=bookingid
        self.pickupaddress=pickupaddress
        self.date=date
        self.time=time
        self.dropoffaddress=dropoffaddress
        self.bookingstatus=bookingstatus
        self.cid=cid
        self.did=did

    #Getter
    def getBookingid(self):
        return self.bookingid

    def getPickupaddress(self):
        return self.pickupaddress

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getDropoffaddress(self):
        return self.dropoffaddress

    def getBookingstatus(self):
        return self.bookingstatus

    def getCid(self):
        return self.cid

    def getDid(self):
        return self.did