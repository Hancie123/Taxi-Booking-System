from tkinter import *
from tkinter import messagebox
from test.regex import timevalidation

app=Tk()
app.geometry("500x400")
app.title("Hancie e-Learning Studio")


def check():
    txt = text.get()
    timeResult=timevalidation(txt)
    if timeResult==True:
        messagebox.showinfo("Info","The time is valid")
    else:
        messagebox.showerror("Error","Invalid time")


text=Entry(app,font=("Times New Roman",16))
text.pack()

btn=Button(app,text="Check Time",font=("Times New Roman",16), command=check)
btn.pack()


app.mainloop()