from tkinter import *
from tkinter import ttk
import customtkinter

app=customtkinter.CTk()
app.title("Hancie e-Learning Studio")

frame_width=500
frame_height=500
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
x_cordinate=int((screen_width/2)-(frame_width/2))
y_cordinate=int((screen_height/2)-(frame_height/2))
app.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=app,
                                     values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.pack(padx=20, pady=10)
combobox.set("option 2")  # set initial value

app.mainloop()