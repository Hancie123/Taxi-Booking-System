from tkinter import *
import customtkinter


app=Tk()
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
app.minsize(screen_width, screen_height)
app.title("Amin Dashboard")
app.state('zoomed')

north_frame=customtkinter.CTkFrame(master=app, height=100, corner_radius=0)
north_frame.pack(side=TOP, fill=BOTH)

title_lbl=Label(north_frame, text="Admin Dashboard", font=('Tahoma', 18, 'bold'))
title_lbl.place(x=200, y=20)



app.mainloop()