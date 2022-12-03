import tkinter
from tkinter import *
import geocoder
import tkintermapview
from PIL import ImageTk, Image
from test import test1
import customtkinter


class test():
    def __init__(self, main720):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main720=main720
        self.main720.geometry("500x400")

        frame=customtkinter.CTkFrame(self.main720, bg_color="red")
        frame.pack()

        myloc = geocoder.ip('me')
        map_widget = tkintermapview.TkinterMapView(frame, width=300)
        map_widget.set_address(myloc, marker=True)
        map_widget.pack(side=RIGHT, fill=BOTH, pady=(10),padx=(0,10))

if __name__=='__main__':
    main720=customtkinter.CTk()
    test(main720)
    main720.mainloop()