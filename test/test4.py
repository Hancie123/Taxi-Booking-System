from datetime import date
from tkinter import *
from tkcalendar import *


app=Tk()
app.geometry("600x500")
app.title("Hancie e-Learning Studio")

futureDate=date.today()
cal=Calendar(app, selectmode="day", background="green",
maxdate=futureDate)
cal.pack()

app.mainloop()