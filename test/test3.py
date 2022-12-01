import tkinter
from tkinter import *
from PIL import ImageTk, Image
from test import test1
import customtkinter


class test():
    def __init__(self, main720):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main720=main720
        self.main720.geometry("500x400")

        def open():
            main=customtkinter.CTkToplevel()
            test1.test720(main)
            main.mainloop()



        tabview = customtkinter.CTkTabview(main720)
        tabview.pack(padx=20, pady=20)

        tabview.add("tab 1")  # add tab at the end
        tabview.add("tab 2")  # add tab at the end
        tabview.set("tab 2")  # set currently visible tab

        tab=customtkinter.CTkTabview(main720)
        tab.pack()
        tab.add("Hancie1")
        tab.add("Nitesh")

        btn = Button(tab.tab('Hancie1'), text="Open", command=open)
        btn.pack()


if __name__=='__main__':
    main720=customtkinter.CTk()
    test(main720)
    main720.mainloop()