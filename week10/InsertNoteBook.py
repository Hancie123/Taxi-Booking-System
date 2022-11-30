# pip install tk
import sys
# Import Library
from tkinter import Tk # Window
from tkinter import Label # Label
from tkinter import Entry # Text Box
from tkinter import Button # Button
from cusInfo import Libs
from CopyManager import insert

def close():
    sys.exit()

def save():
    # reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    pages = txtPages.get()
    price = txtPrice.get()
    email=txtemail.get()
    password=txtPass.get()
    nb1 = Libs(nid, pages, price, email, password)
    result = insert(nb1)
    if(result['status']==True):
        lblmessage['text']="Save Record"
    else:
        lblmessage.config(text="Error")

# Decalre and initialize
window = Tk() # Declare window
window.geometry("250x250")
window.resizable(False, False)
window.title("Insert New Record")

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

btnSave = Button(window, text="SAVE", command=save) # calling save function
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


