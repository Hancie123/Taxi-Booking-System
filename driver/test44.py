
from tkinter import *
from PIL import ImageTk, Image

def switch():
    strimage=str(btn['image'])
    print(type(strimage))
    print(strimage[2:])



app=Tk()

app.geometry("500x200")



image1=ImageTk.PhotoImage(Image.open('left.png'))
image2=ImageTk.PhotoImage(Image.open('right.png'))

btn=Button(app,text="OK",command=switch, image=image1, width=200)
btn.pack()


app.mainloop()