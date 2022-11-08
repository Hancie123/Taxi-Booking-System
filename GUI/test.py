from tkinter import *

class Registration:

    def __init__(self, register):
        self.register=register
        self.register.geometry("500x500")


if __name__=='__main__':
    register=Tk()
    Registration(register)
    register.mainloop()