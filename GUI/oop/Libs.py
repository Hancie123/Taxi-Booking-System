class Book():

    def __init__(self, bid=0, title=None, writer=None, published=None, price=0):
        self.bid=bid
        self.title=title
        self.writer=writer
        self.published=published
        self.price=price

    #Getters
    def getBID(self):
        return self.bid

    def getTitle(self):
        return self.title

    def getWriter(self):
        return self.writer

    def getPublished(self):
        return self.published

    def getPrice(self):
        return self.price

    #setters
    def setBID(self, bid):
        self.bid=bid

    def setTitle(self, title):
        self.title=title

    def setWriter(self, writer):
        self.writer=writer

    def setPublished(self, published):
        self.published=published

    def setPrice(self, price):
        self.price=price

    def __str__(self):
        return ("{},{},{},{},{}".format(self.bid, self.title, self.writer, self.published, self.price))