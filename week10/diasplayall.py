# pip install tk
import sys
# Import Library
from tkinter import * # Window
from cusInfo import Libs
from notebookmanager import all

def close():
    sys.exit()

def getAll():

    cust=all()
    if cust==None:
        print("Record not found")

    else:
        print(cust)



# Decalre and initialize
window = Tk() # Declare window
window.geometry("250x250")
window.resizable(False, False)
window.title("Dispaly All")

lblNID = Label(window, text="ID: ")
lblPages = Label(window, text="Name: ")
lblPrice = Label(window, text="Dob: ")
lblemail=Label(window, text="Email")
Password = Label(window, text="Password: ")

txtNID = Entry(window, width=20)
txtPages = Entry(window, width=20)
txtPrice = Entry(window, width=20)
txtemail = Entry(window, width=20)
txtPass = Entry(window, width=20)

btnSave = Button(window, text="All", command=getAll) # calling save function
btnClose=Button(window, text="CLOSE", command=close)

lblNID.place(x=20, y=10)
txtNID.place(x=100, y=10)

lblPages.place(x=20, y=40)
txtPages.place(x=100, y=40)

lblPrice.place(x=20, y=70)
txtPrice.place(x=100, y=70)

lblemail.place(x=20, y=100)
txtemail.place(x=100, y=100)

Password.place(x=20, y=130)
txtPass.place(x=100, y=130)

lblmessage=Label(window, text="")
lblmessage.place(x=100, y=150)

btnSave.place(x=100, y=200)
btnClose.place(x=150, y=200)

window.mainloop() # Display window

