class NoteBook():
    def __init__(self, nid=0, pages=0, price=0):
        self.nid=nid
        self.pages=pages
        self.price=price
    def getNID(self):
        return self.nid
    def getPages(self):
        return self.pages
    def getPrice(self):
        return self.price
    def setNID(self, nid):
        self.nid=nid
    def setPages(self, pages):
        self.pages=pages
    def setPrice(self, price):
        self.price=price
    def __str__(self):
        return("{}, {}, {}".format(self.nid, self.pages, self.price))
