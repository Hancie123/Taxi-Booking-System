import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
from datetime import time, date
import math
import tkinter as tk
import time
from time import strftime

from driver import driver_registration


class Admin_Dashboard(customtkinter.CTk):
    def __init__(self, main):

        self.main=main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme('blue')
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        self.main.minsize(screen_width, screen_height)
        self.main.title("Taxi Booking System Admin Dashboard")
        self.main.state('zoomed')
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        def exit():
            self.main.destroy()

        menubar = Menu(self.main)

        file = Menu(menubar, tearoff=0)
        file.add_command(label="Account")
        file.add_separator()
        file.add_command(label="Exit", command=exit)
        menubar.add_cascade(label="File", menu=file)

        about = Menu(menubar, tearoff=0)
        about.add_command(label="About")
        menubar.add_cascade(label="About", menu=about)

        self.main.config(menu=menubar)

        north_frame = customtkinter.CTkFrame(master=self.main, height=80, corner_radius=0)
        north_frame.pack(side=TOP, fill=BOTH)

        date1 = date.today()
        today_date_lbl = customtkinter.CTkLabel(north_frame, text='Current Date: 'f"{date1:%a, %b %d %Y}",
                                                text_font=('', 14, 'normal'))
        today_date_lbl.place(x=1060, y=25)

        logout_combo = customtkinter.CTkComboBox(master=north_frame, values=['View Profile', 'Logout'],
                                                 text_font=('', 14, 'normal'))
        logout_combo.place(x=1350, y=25)

        title_image = ImageTk.PhotoImage(
            Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\small_logo.png'))
        title_image_label = Label(north_frame, image=title_image, bg="#2a2d2e")
        title_image_label.place(x=50, y=10)

        title_lbl = customtkinter.CTkLabel(master=north_frame, text="Welcome Hancie Phago",
                                           text_font=('Tahoma', 18, 'bold'))
        title_lbl.place(x=140, y=25)

        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.main, width=300, corner_radius=0)
        left_frame.pack(side=LEFT, fill=BOTH)

        user_image = ImageTk.PhotoImage(Image.open(
            "E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label = Label(left_frame, image=user_image, bg="#2a2d2e")
        user_image_label.image = user_image
        user_image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, text_font=('Tahoma', 14))
        l1.place(x=70, y=150)
        my_time()

        sep = ttk.Separator(left_frame, orient='horizontal')
        sep.place(relx=0, rely=0, relwidth=1)



        l1 = customtkinter.CTkLabel(master=left_frame, text_font=('Tahoma', 14))
        l1.place(x=75, y=150)


        assigndriver_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame, text="Assign Drivers   ", hover_color='black', text_font=('Times New Roman', 14, 'normal'), width=200,image=assigndriver_btn_image, fg_color='#2a2d2e')
        assigndriver_btn.place(x=40, y=200)

        payment_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\paypal-logo-24.png'))
        payment_btn = customtkinter.CTkButton(master=left_frame, text="Payment            ", hover_color='black', text_font=('Times New Roman', 14, 'normal'), width=200,image=payment_btn_image, fg_color='#2a2d2e')
        payment_btn.place(x=40, y=250)

        managecustomers_btn_image = ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        managecustomers_btn = customtkinter.CTkButton(master=left_frame, text="Add Customers", hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=managecustomers_btn_image, fg_color='#2a2d2e')
        managecustomers_btn.place(x=40, y=300)

        def add_driver_gui():

            driver = customtkinter.CTkToplevel()
            driver_registration.DriverRegistration(driver)
            driver.mainloop()

        managedrivers_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\car-regular-24.png'))
        managedrivers_btn = customtkinter.CTkButton(master=left_frame,command=add_driver_gui, text="Add Drivers     ", hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=managedrivers_btn_image, fg_color='#2a2d2e')
        managedrivers_btn.place(x=40, y=350)

        manageemployees_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\id-card-regular-24.png'))
        manageemployees_btn = customtkinter.CTkButton(master=left_frame, text="Add Employees", hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=manageemployees_btn_image, fg_color='#2a2d2e')
        manageemployees_btn.place(x=40, y=400)

        viewcustomer_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="View Customers", hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=viewcustomer_btn_image, fg_color='#2a2d2e')
        viewcustomer_btn.place(x=40, y=450)

        viewdriver_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
        viewdriver_btn = customtkinter.CTkButton(master=left_frame, text="View Drivers    ", hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=viewdriver_btn_image, fg_color='#2a2d2e')
        viewdriver_btn.place(x=40, y=500)

        logout_btn_image = ImageTk.PhotoImage(Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame, text="Logout              ", fg_color='#2a2d2e',hover_color='black',text_font=('Times New Roman', 14, 'normal'), width=200,image=logout_btn_image)
        logout_btn.place(x=40, y=550)

        # +++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++
        frame = customtkinter.CTkFrame(master=self.main, width=1200, height=650, corner_radius=20)
        frame.place(x=320, y=100)

        frame1 = customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
        frame1.place(x=20, y=20)
        frame1_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\dollar-regular-48.png'))
        frame1_label = Label(frame1, text="Total Earning", fg="white", image=frame1_image, bg='#343638')
        frame1_label.place(x=20, y=40)
        frame1_label2 = customtkinter.CTkLabel(master=frame1, text="Total \nEarning", text_font=('', 19, 'bold'))
        frame1_label2.place(x=80, y=20)
        frame1_label3 = customtkinter.CTkLabel(master=frame1, text="$ 2000", text_font=('', 19, 'bold'))
        frame1_label3.place(x=80, y=100)

        frame2 = customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
        frame2.place(x=320, y=20)
        frame2_image = ImageTk.PhotoImage(Image.open(
            'E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-detail-solid-48.png'))
        frame2_label = Label(frame2, text="Total Customer", fg="white", image=frame2_image, bg='#343638')
        frame2_label.place(x=20, y=40)
        frame2_label2 = customtkinter.CTkLabel(master=frame2, text="Total \nCustomers", text_font=('', 19, 'bold'))
        frame2_label2.place(x=80, y=20)
        frame2_label3 = customtkinter.CTkLabel(master=frame2, text="30", text_font=('', 19, 'bold'))
        frame2_label3.place(x=80, y=100)

        frame3 = customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
        frame3.place(x=620, y=20)
        frame3_image = ImageTk.PhotoImage(Image.open(
            'E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\car-regular-48.png'))
        frame3_label = Label(frame3, text="Total Drivers", fg="white", image=frame3_image, bg='#343638')
        frame3_label.place(x=20, y=40)
        frame3_label2 = customtkinter.CTkLabel(master=frame3, text="Total \nDrivers", text_font=('', 19, 'bold'))
        frame3_label2.place(x=80, y=20)
        frame3_label3 = customtkinter.CTkLabel(master=frame3, text="15", text_font=('', 19, 'bold'))
        frame3_label3.place(x=80, y=100)

        frame4 = customtkinter.CTkFrame(master=frame, width=250, height=150, corner_radius=20)
        frame4.place(x=920, y=20)
        frame4_image = ImageTk.PhotoImage(Image.open(
            'E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\book-regular-48.png'))
        frame4_label = Label(frame4, text="Total Customer", fg="white", image=frame2_image, bg='#343638')
        frame4_label.place(x=20, y=40)
        frame4_label2 = customtkinter.CTkLabel(master=frame4, text="Total \nRides", text_font=('', 19, 'bold'))
        frame4_label2.place(x=80, y=20)
        frame4_label3 = customtkinter.CTkLabel(master=frame4, text="20", text_font=('', 19, 'bold'))
        frame4_label3.place(x=80, y=100)


if __name__=='__main__':
    main=customtkinter.CTk()
    Admin_Dashboard(main)
    main.mainloop()




