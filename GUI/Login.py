from tkinter import *


app=Tk()
app.geometry("500x500")
app.title("Taxi Booking Login System")

#----------------Center frame----------------
frame_width=1000
frame_height=500
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
x_cordinate=int((screen_width/2)-(frame_width/2))
y_cordinate=int((screen_height/2)-(frame_height/2))
app.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))


north_frame=Frame(app, bg="green", width=50)
north_frame.pack(side=TOP)


app.mainloop()