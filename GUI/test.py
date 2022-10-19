from tkinter import *

app=Tk()

frame_width=500
frame_height=400

screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
x_cordinate=int((screen_width/2)-(frame_width/2))
y_cordinate=int((screen_height/2)-(frame_height/2))
app.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate,y_cordinate))

frame=Frame(app, bg="green", height=100, relief=GROOVE)
frame.pack(side=TOP, fill=BOTH)

lbl=Label(frame, text="Hancie Phago")
lbl.place(x=500, y=10)

frame2=Frame(app, bg="red", width=100)
frame2.pack(side="left", fill=BOTH)






app.mainloop()