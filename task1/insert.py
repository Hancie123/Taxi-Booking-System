from task1.driver import Driver
from ManagerDriver import saveDriver
from tkinter import *
import customtkinter

class Insert():
    def __init__(self, root):
        self.root=root
        self.root.title("Hancie Phago")
        self.root.geometry("500x400")

        self.id=StringVar()
        self.name=StringVar()
        self.lbl=StringVar()

        id=customtkinter.CTkEntry(self.root, textvariable=self.id)
        id.pack()

        values=['Male','Femail']
        name=customtkinter.CTkComboBox(self.root, values=values)
        name.pack()

        lbl=customtkinter.CTkEntry(self.root, textvariable=self.lbl, placeholder_text="Enter", placeholder_text_color="red")
        lbl.pack()

        def save():
            d=Driver(self.id.get(), name.get(), self.lbl.get())
            r=saveDriver(d)
            if r==True:
                print("Saved")
            else:
                print("Error")

        btn=customtkinter.CTkButton(self.root, text="Save", command=save)
        btn.pack()

        def clar():
            self.id.set('')
            self.name.set('')
            self.lbl.set('')

        btn2=Button(self.root, text="Clear", command=clar)
        btn2.pack()




if __name__=='__main__':
    root=Tk()
    Insert(root)
    root.mainloop()


