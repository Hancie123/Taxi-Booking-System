from tkinter import *
import customtkinter
from datetime import date, time
from tkinter import ttk

app=customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenwidth()
app.minsize(screen_width, screen_height)
app.state('zoomed')
app.title('Customer Dashboard | Taxi Booking System')
app.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

#+++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
left_frame=customtkinter.CTkFrame(master=app, width=300, corner_radius=0)
left_frame.pack(side=LEFT, fill=BOTH)
app.mainloop()

