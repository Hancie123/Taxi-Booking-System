import tkinter as tk
import customtkinter

from tktimepicker import AnalogPicker, AnalogThemes, constants


def updateTime(time):
    time_lbl.insert(0,str("{}:{} {}".format(*time))) # remove 3rd flower bracket in case of 24 hrs time


def get_time():

    top = tk.Toplevel(root)

    time_picker = AnalogPicker(top, type=constants.HOURS12)
    time_picker.pack(expand=True, fill="both")

    theme = AnalogThemes(time_picker)
    theme.setNavyBlue()
    ok_btn = customtkinter.CTkButton(master=top, text="ok", command=lambda: updateTime(time_picker.time()))
    ok_btn.pack()



root = tk.Tk()
root.geometry("500x300")

time = ()

time_lbl = customtkinter.CTkEntry(master=root, text="Time:")
time_lbl.place(x=100, y=20)

time_btn = customtkinter.CTkButton(master=root, text="Get Time", command=get_time)
time_btn.place(x=250, y=20)

root.mainloop()