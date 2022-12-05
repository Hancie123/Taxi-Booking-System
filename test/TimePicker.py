import tkinter
from tkinter import *
import customtkinter
from tktimepicker import AnalogPicker, AnalogThemes, constants

root = Tk()
root.geometry("500x300")
root.title("Hancie e-Learning Studio")

def get_time():
    top = tkinter.Toplevel(root)
    time_lbl.delete(0, len(time_lbl.get()))
    time_picker = AnalogPicker(top, type=constants.HOURS12)
    time_picker.pack(expand=True, fill="both")

    theme = AnalogThemes(time_picker)
    theme.setNavyBlue()
    ok_btn = customtkinter.CTkButton(master=top, text="ok", command=lambda: updateTime(time_picker.time()))
    ok_btn.pack()

time = ()

def updateTime(time):
    time_lbl.insert(0,str("{}:{} {}".format(*time)))

time_lbl = customtkinter.CTkEntry(master=root)
time_lbl.place(x=100, y=20)

time_btn = customtkinter.CTkButton(master=root, text="Get Time", command=get_time)
time_btn.place(x=250, y=20)


root.mainloop()