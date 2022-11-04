from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
from datetime import time, date
import math
import tkinter as tk
import time
from time import strftime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('blue')
app=customtkinter.CTk()
screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
app.minsize(screen_width, screen_height)
app.title("Taxi Booking System Admin Dashboard")
app.state('zoomed')
app.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")



def exit():
    app.destroy()

menubar=Menu(app)

file=Menu(menubar, tearoff=0)
file.add_command(label="Account")
file.add_separator()
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file)

about=Menu(menubar, tearoff=0)
about.add_command(label="About")
menubar.add_cascade(label="About", menu=about)


app.config(menu=menubar)


north_frame=customtkinter.CTkFrame(master=app, height=80, corner_radius=0)
north_frame.pack(side=TOP, fill=BOTH)

date=date.today()
today_date_lbl=customtkinter.CTkLabel(north_frame, text='Current Date: 'f"{date:%a, %b %d %Y}", text_font=('', 14,'normal'))
today_date_lbl.place(x=1060, y=25)

logout_combo=customtkinter.CTkComboBox(master=north_frame, values=['View Profile','Logout'], text_font=('', 14,'normal'))
logout_combo.place(x=1350, y=25)

title_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\small_logo.png'))
title_image_label=Label(north_frame, image=title_image, bg="#2a2d2e")
title_image_label.place(x=50, y=10)

title_lbl=customtkinter.CTkLabel(master=north_frame, text="Welcome Hancie Phago", text_font=('Tahoma', 18, 'bold'))
title_lbl.place(x=140, y=25)

#+++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
left_frame=customtkinter.CTkFrame(master=app, width=300, corner_radius=0)
left_frame.pack(side=LEFT, fill=BOTH)

sep=ttk.Separator(left_frame, orient='horizontal')
sep.place(relx=0, rely=0, relwidth=1)

width, height = 250, 250  # set the variables
c_width, c_height = width - 5, height - 5
c1 = tk.Canvas(left_frame, width=c_width, height=c_height, bg='#2a2d2e', highlightthickness=0)
c1.place(x=100, y=20)
dial = c1.create_oval(10, 10, 150, 150, width=8, outline='#FF0000', fill='#FFFFFF')
x, y = 76, 76  # center
x1, y1, x2, y2 = x, y, x, 10  # second needle
center = c1.create_oval(x - 4, y - 4, x + 4, y + 4, fill='#c0c0c0')
r1 = 70  # dial lines for one minute
r2 = 50  # for hour numbers  after the lines
rs = 50  # length of second needle
rm = 45  # length of minute needle
rh = 30  # lenght of hour needle
in_degree = 0
in_degree_s = int(time.strftime('%S')) * 6  # local second
in_degree_m = int(time.strftime('%M')) * 6  # local minutes
in_degree_h = int(time.strftime('%I')) * 30  # 12 hour format
if (in_degree_h == 360):
    in_degree_h = 0  # adjusting 12 O'clock to 0
h = iter(['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
# second=c1.create_line(x1,y1,x2,y2,arrow='last',width=1)
for i in range(0, 60):
    in_radian = math.radians(in_degree)
    if (i % 5 == 0):
        ratio = 0.85  # Long marks ( lines )
        t1 = x + r2 * math.sin(in_radian)  # coordinate to add text ( hour numbers )
        t2 = x - r2 * math.cos(in_radian)  # coordinate to add text ( hour numbers )
        c1.create_text(t1, t2, fill='blue', font="Times 14  bold", text=next(h))  # number added
    else:
        ratio = 0.9  # small marks ( lines )

    x1 = x + ratio * r1 * math.sin(in_radian)
    y1 = y - ratio * r1 * math.cos(in_radian)
    x2 = x + r1 * math.sin(in_radian)
    y2 = y - r1 * math.cos(in_radian)
    c1.create_line(x1, y1, x2, y2, width=1)  # draw the line for segment
    in_degree = in_degree + 6  # increment for next segment
# End of Marking on the dial with hour numbers
# Initialize the second needle based on local seconds value
in_radian = math.radians(in_degree_s)
x2 = x + rs * math.sin(in_radian)
y2 = y - rs * math.cos(in_radian)
second = c1.create_line(x, y, x2, y2, fill='red', width=2)  # draw the second needle


def my_second():
    global in_degree_s, second
    in_radian = math.radians(in_degree_s)
    c1.delete(second)  # delete the needle
    x2 = x + rs * math.sin(in_radian)  # Horizontal coordinate of outer edge
    y2 = y - rs * math.cos(in_radian)  # vertical coordinate of outer adge
    second = c1.create_line(x, y, x2, y2, arrow='last', fill='red', width=2)
    if (in_degree_s >= 360):  # one rotattion is over if reached 360
        in_degree_s = 0  # start from zero angle again
        my_minute()  # call the minute needle to move one segment.
    in_degree_s = in_degree_s + 6  # increment of one segment is 6 degree
    c1.after(1000, my_second)  # timer calling recrusive after 1 second


# End of second
# Initialize Minutes needle based on local time minute value
in_radian = math.radians(in_degree_m)
x2 = x + rm * math.sin(in_radian)
y2 = y - rm * math.cos(in_radian)
minute = c1.create_line(x, y, x2, y2, width=4, fill='green')


def my_minute():
    global in_degree_m, minute
    in_degree_m = in_degree_m + 6  # increment for each segment
    in_radian = math.radians(in_degree_m)  # coverting to radian
    c1.delete(minute)  # delete the previous needle
    x2 = x + rm * math.sin(in_radian)  # Horizontal coordinate of outer edge
    y2 = y - rm * math.cos(in_radian)  # vertical coordinate of outer dege
    minute = c1.create_line(x, y, x2, y2, width=4, fill='green')
    my_hour()  # calling hour needle to move
    if (in_degree_m >= 360):  # One rotation of 360 degree is over
        in_degree_m = 0


# initialize hour needle based on local hour
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7
in_degree_h = in_degree_h + (in_degree_m * 0.0833333)
in_radian = math.radians(in_degree_h)
x2 = x + rh * math.sin(in_radian)
y2 = y - rh * math.cos(in_radian)
hour = c1.create_line(x, y, x2, y2, width=6, fill='#a83e32')

def my_hour():
    global in_degree_h, hour
    in_degree_h = in_degree_h + 0.5  # increment in each step
    in_radian = math.radians(in_degree_h)  # in radian
    c1.delete(hour)  # deleting hour needle
    x2 = x + rh * math.sin(in_radian)  # Horizontal coordinate for outer edge
    y2 = y - rh * math.cos(in_radian)  # vertical coordinate for outer adge
    hour = c1.create_line(x, y, x2, y2, width=6, fill='#a83e32')
    if (in_degree_h >= 360):
        in_degree_h = 0


my_second()


def my_time():
    time_string = strftime('%I:%M:%S %p')  # time format
    l1.configure(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds

l1 = customtkinter.CTkLabel(master=left_frame, text_font=('Tahoma', 14))
l1.place(x=75, y=150)
my_time()



assigndriver_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
assigndriver_btn=customtkinter.CTkButton(master=left_frame, text="Assign Drivers   ", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=assigndriver_btn_image, fg_color='#2a2d2e')
assigndriver_btn.place(x=40, y=200)

payment_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\paypal-logo-24.png'))
payment_btn=customtkinter.CTkButton(master=left_frame, text="Payment            ", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=payment_btn_image, fg_color='#2a2d2e')
payment_btn.place(x=40, y=250)

managecustomers_btn_image=ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
managecustomers_btn=customtkinter.CTkButton(master=left_frame, text="Add Customers", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=managecustomers_btn_image, fg_color='#2a2d2e')
managecustomers_btn.place(x=40, y=300)

managedrivers_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\car-regular-24.png'))
managedrivers_btn=customtkinter.CTkButton(master=left_frame, text="Add Drivers     ", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=managedrivers_btn_image, fg_color='#2a2d2e')
managedrivers_btn.place(x=40, y=350)

manageemployees_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\id-card-regular-24.png'))
manageemployees_btn=customtkinter.CTkButton(master=left_frame, text="Add Employees", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=manageemployees_btn_image, fg_color='#2a2d2e')
manageemployees_btn.place(x=40, y=400)


viewcustomer_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
viewcustomer_btn=customtkinter.CTkButton(master=left_frame, text="View Customers", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=viewcustomer_btn_image, fg_color='#2a2d2e')
viewcustomer_btn.place(x=40, y=450)

viewdriver_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
viewdriver_btn=customtkinter.CTkButton(master=left_frame, text="View Drivers    ", hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=viewdriver_btn_image, fg_color='#2a2d2e')
viewdriver_btn.place(x=40, y=500)

logout_btn_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
logout_btn=customtkinter.CTkButton(master=left_frame, text="Logout              ", fg_color='#2a2d2e', hover_color='black',
                            text_font=('Times New Roman', 14,'normal'), width=200, image=logout_btn_image)
logout_btn.place(x=40, y=550)

#+++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++
frame=customtkinter.CTkFrame(master=app, width=1200, height=650, corner_radius=20)
frame.place(x=320, y=100)


frame1=customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
frame1.place(x=20, y=20)
frame1_image=ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\dollar-regular-48.png'))
frame1_label=Label(frame1, text="Total Earning", fg="white", image=frame1_image, bg='#343638')
frame1_label.place(x=20, y=40)
frame1_label2=customtkinter.CTkLabel(master=frame1, text="Total \nEarning", text_font=('', 19,'bold'))
frame1_label2.place(x=80, y=20)
frame1_label3=customtkinter.CTkLabel(master=frame1, text="$ 2000", text_font=('', 19,'bold'))
frame1_label3.place(x=80, y=100)


frame2=customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
frame2.place(x=320, y=20)
frame2_image=ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-detail-solid-48.png'))
frame2_label=Label(frame2, text="Total Customer", fg="white", image=frame2_image, bg='#343638')
frame2_label.place(x=20, y=40)
frame2_label2=customtkinter.CTkLabel(master=frame2, text="Total \nCustomers", text_font=('', 19,'bold'))
frame2_label2.place(x=80, y=20)
frame2_label3=customtkinter.CTkLabel(master=frame2, text="30", text_font=('', 19,'bold'))
frame2_label3.place(x=80, y=100)

frame3=customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
frame3.place(x=620, y=20)
frame3_image=ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\car-regular-48.png'))
frame3_label=Label(frame3, text="Total Drivers", fg="white", image=frame3_image, bg='#343638')
frame3_label.place(x=20, y=40)
frame3_label2=customtkinter.CTkLabel(master=frame3, text="Total \nDrivers", text_font=('', 19,'bold'))
frame3_label2.place(x=80, y=20)
frame3_label3=customtkinter.CTkLabel(master=frame3, text="15", text_font=('', 19,'bold'))
frame3_label3.place(x=80, y=100)

frame4=customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
frame4.place(x=920, y=20)
frame4_image=ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\book-regular-48.png'))
frame4_label=Label(frame4, text="Total Customer", fg="white", image=frame2_image, bg='#343638')
frame4_label.place(x=20, y=40)
frame4_label2=customtkinter.CTkLabel(master=frame4, text="Total \nRides", text_font=('', 19,'bold'))
frame4_label2.place(x=80, y=20)
frame4_label3=customtkinter.CTkLabel(master=frame4, text="20", text_font=('', 19,'bold'))
frame4_label3.place(x=80, y=100)









app.mainloop()