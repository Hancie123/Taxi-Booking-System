from tkinter import *
import datetime

from test import Global


class learn():
    def __init__(self, root):
        self.root=root
        self.root.title("Hancie e-Learning Studio")
        self.root.geometry("500x400")

        num=100
        Global.data=num



if __name__=='__main__':
    root=Tk()
    learn(root)
    root.mainloop()