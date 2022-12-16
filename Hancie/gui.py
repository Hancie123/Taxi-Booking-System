from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from Hancie.backend import insert_record
from Hancie.libs import Libs


class Hancie():
    def __init__(self, main):
        self.main=main
        self.main.title("Hancie e-Learning Studio")
        self.main.geometry("500x400")

        myfont=('Tahoma',16)

        namelbl=Label(self.main, text="Name:", font=myfont)
        namelbl.place(x=20, y=50)

        nametxt=Entry(self.main, font=myfont)
        nametxt.place(x=120, y=50)

        doblbl=Label(self.main, text="DOB:", font=myfont)
        doblbl.place(x=20, y=100)

        dobtxt=DateEntry(self.main, font=myfont)
        dobtxt.place(x=120, y=100)

        emailbl = Label(self.main, text="Email:", font=myfont)
        emailbl.place(x=20, y=150)

        emailtxt = Entry(self.main, font=myfont)
        emailtxt.place(x=120, y=150)

        passwordlbl = Label(self.main, text="Password:", font=myfont)
        passwordlbl.place(x=20, y=200)

        passwordtxt = Entry(self.main, font=myfont)
        passwordtxt.place(x=120, y=200)

        def register():
            name=nametxt.get()
            dob=dobtxt.get()
            email=emailtxt.get()
            password=passwordtxt.get()

            customer=Libs(cid='', name=name, dob=dob, email=email, password=password)
            result=insert_record(customer)
            if result==True:
                messagebox.showinfo("Customer","The data is registered")
            else:
                messagebox.showerror("Customer","Error Occurred")


        savebtn = Button(self.main,command=register, font=myfont, text="Save")
        savebtn.place(x=120, y=250)






if __name__=='__main__':
    main=Tk()
    Hancie(main)
    main.mainloop()