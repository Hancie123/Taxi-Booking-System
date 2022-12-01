from tkinter import *
from PIL import ImageTk, Image
import customtkinter

class test720(customtkinter.CTk):
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        self.main.title("Hancie Phago")
        self.main.geometry("500x400")

        def slider_event(value):
            print(value)

        slider = customtkinter.CTkSlider(master=self.main, from_=0, to=100, command=slider_event)
        slider.place(relx=0.5, rely=0.5, anchor=CENTER)

        progressbar = customtkinter.CTkProgressBar(master=self.main)
        progressbar.set(0.9)
        progressbar.pack(padx=20, pady=10)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)

        combobox = customtkinter.CTkComboBox(master=self.main,
                                             values=["system", "light", 'dark'],
                                             command=combobox_callback)
        combobox.pack(padx=20, pady=10)
        combobox.set("light")  # set initial value




if __name__=='__main__':
    main=customtkinter.CTk()
    test720(main)
    main.mainloop()

