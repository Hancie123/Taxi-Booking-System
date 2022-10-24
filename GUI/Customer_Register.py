from tkinter import *
import customtkinter
from tkcalendar import *
from PIL import ImageTk, Image
from datetime import date

app=Tk()
app.title("Customer Register")
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
app.minsize(screen_width, screen_height)
app.state('zoomed')
app.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
customtkinter.set_default_color_theme('blue')
customtkinter.set_appearance_mode('dark')

font=('Tahoma', 18,'bold')
font1=('Tahoma', 18,'normal')

North_Frame=customtkinter.CTkFrame(master=app, height=100, corner_radius=0)
North_Frame.pack(side=TOP, fill=BOTH)

title_lbl=customtkinter.CTkLabel(master=North_Frame, text="CUSTOMER REGISTRATION FORM", text_font=('Cambria', 26, 'bold'))
title_lbl.place(x=500, y=25)

back_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\back.png')
photo=ImageTk.PhotoImage(back_image)
back_image_label=Label(North_Frame, image=photo, bg="#2a2d2e")
back_image_label.image=photo
back_image_label.place(x=20, y=25)



Right_frame=customtkinter.CTkFrame(master=app)
Right_frame.pack(side=LEFT, fill=BOTH)

canva=Canvas(Right_frame, width=900, height=900, bd=0, highlightthickness=0)
canva.pack()

img=PhotoImage(file="E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Taxi.png")
canva.create_image(0,0,anchor=NW, image=img)

name_lbl=Label(app, text="Name: ", font=font)
name_lbl.place(x=630, y=200)

name_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
name_txt.place(x=760, y=200)

dob_lbl=Label(app, text="DOB: ", font=font)
dob_lbl.place(x=630, y=270)

dt=date.today()
dob_txt=DateEntry(app, font=font1, selectmode='day', width=17, mindate=dt)

dob_txt.place(x=760, y=270)



gender_lbl=Label(app, text="Gender: ", font=font)
gender_lbl.place(x=1100, y=200)



gender_txt=customtkinter.CTkOptionMenu(master=app, fg_color='white', text_color='black',
                                       values=['Male','Female','Others'], text_font=font1, width=250)
gender_txt.set('Male')
gender_txt.place(x=1240, y=200)

mobile_lbl=Label(app, text="Mobile: ", font=font)
mobile_lbl.place(x=1100, y=270)

mobile_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
mobile_txt.place(x=1240, y=270)

address_lbl=Label(app, text="Address: ", font=font)
address_lbl.place(x=630, y=340)

address_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
address_txt.place(x=760, y=340)

email_lbl=Label(app, text="Email: ", font=font)
email_lbl.place(x=1100, y=340)

email_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
email_txt.place(x=1240, y=340)


password_lbl=Label(app, text="Password: ", font=font)
password_lbl.place(x=630, y=410)

password_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
password_txt.place(x=760, y=410)

credit_lbl=Label(app, text="Credit No: ", font=font)
credit_lbl.place(x=1100, y=410)

credit_txt=customtkinter.CTkEntry(master=app, text="", fg_color='white', text_color='black', text_font=font1, width=250)
credit_txt.place(x=1240, y=410)

register_btn_image=ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit.png"))
register_btn=customtkinter.CTkButton(master=app, text="Register", image=register_btn_image,hover_color='black', text_font=('Tahoma', 20, 'bold'))
register_btn.place(x=1000, y=530)

back_lbl=customtkinter.CTkLabel(master=app, text="Already have an account", text_font=('Tahoma', 14, 'normal'),
                                text_color='black')
back_lbl.place(x=950, y=590)

back_btn=customtkinter.CTkButton(master=app, text="SIGN IN", width=100, text_font=('Tahoma', 14, 'bold'), hover_color='black')
back_btn.place(x=1170, y=590)



app.mainloop()