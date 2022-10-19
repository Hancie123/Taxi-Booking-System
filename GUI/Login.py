import customtkinter
from tkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()
app.geometry("400x240")
app.resizable(False, False)
app.state('zoomed')


app.title("Taxi Booking System Login")
app.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

font1=('Tahoma', 15, 'bold')

north_frame=customtkinter.CTkFrame(master=app, height=100)
north_frame.pack(side=TOP, fill=BOTH)

title_label=customtkinter.CTkLabel(master=north_frame, text="TAXI BOOKING SYSTEM", text_font=('Tahoma', 18, 'bold'))
title_label.place(x=650, y=40)

frame=customtkinter.CTkFrame(master=app, width=400, height=400, corner_radius=20)
frame.pack(side=LEFT, padx=20)

canvas = Canvas(frame, width = 900, height = 900, bg="#212325", borderwidth=0, bd=0, highlightthickness=0)
canvas.pack()
img = PhotoImage(file="E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Tablet login-rafiki.png")
canvas.create_image(20,20, anchor=NW, image=img)




frame2=customtkinter.CTkFrame(master=app, width=750, height=600, corner_radius=20)
frame2.pack(side=RIGHT, padx=30)

sign_in_image = Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(frame2, image=photo, bg="#2a2d2e")
sign_in_image_label.image = photo
sign_in_image_label.place(x=380, y=50)

signin_lbl=customtkinter.CTkLabel(master=frame2, text="Sign In", text_font=font1)
signin_lbl.place(x=295, y=130)

email_lbl=customtkinter.CTkLabel(master=frame2, text="Email: ", text_font=font1)
email_lbl.place(x=200, y=200)

email_txt=customtkinter.CTkEntry(master=frame2, corner_radius=10, text_font=font1, width=200)
email_txt.place(x=330,y=200)


password_lbl=customtkinter.CTkLabel(master=frame2, text="Password: ", text_font=font1)
password_lbl.place(x=200, y=250)

password_txt=customtkinter.CTkEntry(master=frame2, corner_radius=10, text_font=font1, width=200, show="*")
password_txt.place(x=330,y=250)


# Use CTkButton instead of tkinter Button
add_login_image = ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\login.png").resize((50,50), Image.ANTIALIAS))
button = customtkinter.CTkButton(master=frame2, text="Login", image=add_login_image, borderwidth=0, corner_radius=10, text_color="white", text_font=font1)
button.place(x=340, y=350)

signup_lbl=customtkinter.CTkLabel(master=frame2, text="No account yet")
signup_lbl.place(x=300, y=420)

signup_btn=customtkinter.CTkButton(master=frame2, text="SIGN UP NOW", width=50, height=20)
signup_btn.place(x=420, y=420)


app.mainloop()