from tkinter import *


app=Tk()
app.geometry("500x400")
app.title("Hancie e-Learning Studio")

txt=Entry(app, font=('Times New Roman',14))
txt.bind("<Button-1>", lambda e: "break")
txt.bind("<Key>", lambda e: "break")
txt.pack()


app.mainloop()