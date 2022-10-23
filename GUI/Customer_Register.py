from tkinter import *
import customtkinter
from tkcalendar import *

app=Tk()
app.title("Customer Register")
app.state('zoomed')
app.resizable(False, False)
app.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
customtkinter.set_default_color_theme('blue')
customtkinter.set_appearance_mode('dark')

font=('Tahoma', 18,'bold')
font1=('Tahoma', 18,'normal')

North_Frame=customtkinter.CTkFrame(master=app, height=100, corner_radius=0)
North_Frame.pack(side=TOP, fill=BOTH)

title_lbl=customtkinter.CTkLabel(master=North_Frame, text="CUSTOMER REGISTRATION FORM", text_font=('Cambria', 26, 'bold'))
title_lbl.place(x=500, y=25)

Right_frame=customtkinter.CTkFrame(master=app)
Right_frame.pack(side=LEFT, fill=BOTH)

canva=Canvas(Right_frame, width=900, height=900, bd=0, highlightthickness=0)
canva.pack()

img=PhotoImage(file="E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Taxi.png")
canva.create_image(0,0,anchor=NW, image=img)

name_lbl=Label(app, text="Name: ", font=font)
name_lbl.place(x=630, y=200)

name_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
name_txt.place(x=740, y=200)

dob_lbl=Label(app, text="DOB: ", font=font)
dob_lbl.place(x=630, y=270)

dob_txt=DateEntry(app, font=font1, selectmode='day', width=17)
dob_txt.place(x=740, y=270)



gender_lbl=Label(app, text="Gender: ", font=font)
gender_lbl.place(x=1100, y=200)



gender_txt=customtkinter.CTkOptionMenu(master=app, fg_color='white', text_color='black',
                                       values=['Male','Female','Others'], text_font=font1, width=250)
gender_txt.set('Male')
gender_txt.place(x=1220, y=200)

mobile_lbl=Label(app, text="Mobile: ", font=font)
mobile_lbl.place(x=1100, y=270)

mobile_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
mobile_txt.place(x=1220, y=270)

address_lbl=Label(app, text="Address: ", font=font)
address_lbl.place(x=630, y=340)

address_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
address_txt.place(x=740, y=340)

email_lbl=Label(app, text="Email: ", font=font)
email_lbl.place(x=1100, y=340)

email_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
email_txt.place(x=1220, y=340)


email_lbl=Label(app, text="Email: ", font=font)
email_lbl.place(x=1100, y=340)












app.mainloop()