from tkinter import *

class Sushant():
    def __init__(self, main):
        self.main=main
        self.main.title("Sushant Shah")
        self.main.geometry("500x400")
        self.main.config(bg="#28c7fa")

        myfont=('Times New Roman', 16,'bold')

        idlabel=Label(self.main,  text="ID: ", font=myfont)
        idlabel.place(x=100, y=50)

        idtext=Entry(self.main, font=myfont)
        idtext.place(x=200, y=50)


if __name__=='__main__':
    main=Tk()
    Sushant(main)
    main.mainloop()
