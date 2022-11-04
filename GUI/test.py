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

canva=Canvas(app, width=500, height=500, bg="grey")
coord=10,10, 400,400
# arc=canva.create_arc(coord, start=0, extent=180, fill="green")
# circle=canva.create_oval(100,100,20,20, fill="red", outline="yellow")
line=canva.create_line(0,0,500,500)
line2=canva.create_line(0,500,500,0)

line3=canva.create_line(0,20, 500, 30)

line5=canva.create_rectangle(200,100, 300,200, fill="red")

line6=canva.create_text(200,300, text="Hancie Phago", fill="blue")

line7=canva.create_oval(0,200,300,500, fill="green")
canva.pack()

import matplotlib.pyplot as plt
import numpy as np

import platform

print(platform.platform())
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.version().split('.')[2])
print(platform.machine())


app.mainloop()