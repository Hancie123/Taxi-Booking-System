#declare temp variables
from GUI.oop.Libs import Book

bid=title=writer=published=price=None


#input
bid=int(input("Enter booking ID: "))
title=input("Enter book title: ")
writer=input("Enter writer: ")
published=int(input("Published year: "))
price=int(input("Enter price of book: "))


book1=Book(bid,title, writer, published, price)
print(book1)