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

from customer import customer_management
from dbms.customer_backend import total_customer
from driver import driver_registration
from employees import employees_management


class Admin_Dashboard(customtkinter.CTk):
    def __init__(self, main):

        self.main=main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme('blue')
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        self.main.minsize(screen_width, screen_height)
        self.main.title("Taxi Booking System Admin Dashboard | Designed by Hancie Phago")
        self.main.state('zoomed')
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        titlefont = customtkinter.CTkFont(family='Times New Roman', size=35, weight='normal')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        labelfont = customtkinter.CTkFont(family='Times New Roman', size=25, weight='normal')
        sidemenufont = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

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
        today_date_lbl = customtkinter.CTkLabel(north_frame, text='Current Date: 'f"{date1:%a, %b %d %Y}",font=('', 14, 'normal'))
        today_date_lbl.place(x=1060, y=25)

        logout_combo = customtkinter.CTkComboBox(master=north_frame, values=['View Profile', 'Logout'],font=('', 14, 'normal'))
        logout_combo.place(x=1350, y=25)

        #+++++++++++++++++++++++++++++Title Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        title_lbl = customtkinter.CTkLabel(master=north_frame, text="Admin Dashboard",font=titlefont)
        title_lbl.place(x=50, y=25)

        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.main, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        user_image = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label = Label(left_frame, image=user_image, bg="#2b2b2b")
        user_image_label.image = user_image
        user_image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=sidemenufont)
        l1.place(x=90, y=150)
        my_time()

        def assign_driver():
            root=customtkinter.CTkToplevel()
            root.title("Taxi Booking System")
            width = 1050
            height = 450
            myscreenwidth = self.main.winfo_screenwidth()
            myscreenheight = self.main.winfo_screenheight()
            xCordinate = int((myscreenwidth / 2) - (width / 2))
            yCordinate = int((myscreenheight / 2) - (height / 2))
            root.geometry('{}x{}+{}+{}'.format(width, height, xCordinate + 200, yCordinate))
            root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
            root.resizable(0,0)
            root.mainloop()

        assigndriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame, text="Assign Drivers   ",command=assign_driver, hover_color='black', font=sidemenufont, width=200,image=assigndriver_btn_image, fg_color='#2b2b2b')
        assigndriver_btn.place(x=40, y=200)

        payment_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\paypal-logo-24.png'))
        payment_btn = customtkinter.CTkButton(master=left_frame, text="Payment            ", hover_color='black', font=sidemenufont, width=200,image=payment_btn_image, fg_color='#2b2b2b')
        payment_btn.place(x=40, y=250)

        def add_customer_gui():
            customer=customtkinter.CTkToplevel()
            customer_management.CustomerManagement(customer)
            customer.mainloop()

        managecustomers_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        managecustomers_btn = customtkinter.CTkButton(master=left_frame, text="Add Customers",command=add_customer_gui, hover_color='black',font=sidemenufont, width=200,image=managecustomers_btn_image, fg_color='#2b2b2b')
        managecustomers_btn.place(x=40, y=300)

        def add_driver_gui():
            driver = customtkinter.CTkToplevel()
            driver_registration.DriverRegistration(driver)
            driver.mainloop()

        managedrivers_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\car-regular-24.png'))
        managedrivers_btn = customtkinter.CTkButton(master=left_frame,command=add_driver_gui, text="Add Drivers     ", hover_color='black',font=sidemenufont, width=200,image=managedrivers_btn_image, fg_color='#2b2b2b')
        managedrivers_btn.place(x=40, y=350)

        def employess_gui():
            root=customtkinter.CTkToplevel()
            employees_management.EmployeesManagement(root)
            root.mainloop()

        manageemployees_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\id-card-regular-24.png'))
        manageemployees_btn = customtkinter.CTkButton(master=left_frame,command=employess_gui, text="Add Employees", hover_color='black',font=sidemenufont, width=200,image=manageemployees_btn_image, fg_color='#2b2b2b')
        manageemployees_btn.place(x=40, y=400)

        viewcustomer_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="View Customers", hover_color='black',font=sidemenufont, width=200,image=viewcustomer_btn_image, fg_color='#2b2b2b')
        viewcustomer_btn.place(x=40, y=450)

        viewdriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
        viewdriver_btn = customtkinter.CTkButton(master=left_frame, text="View Drivers    ", hover_color='black',font=sidemenufont, width=200,image=viewdriver_btn_image, fg_color='#2b2b2b')
        viewdriver_btn.place(x=40, y=500)

        logout_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame, text="Logout              ", fg_color='#2b2b2b',hover_color='black',font=sidemenufont, width=200,image=logout_btn_image)
        logout_btn.place(x=40, y=550)

        themelbl = customtkinter.CTkLabel(left_frame, text="Appearance Mode:", font=sidemenufont)
        themelbl.place(x=60, y=600)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice == 'light':
                user_image_label['bg'] = "#dbdbdb"

            if choice == 'dark':
                user_image_label['bg'] = "#2b2b2b"

        combobox = customtkinter.CTkComboBox(master=left_frame, values=["dark",'light'],
                                             command=combobox_callback, font=sidemenufont)
        combobox.place(x=65, y=630)
        combobox.set("dark")  # set initi

        # +++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++
        frame = customtkinter.CTkFrame(master=self.main, width=1200, height=650, corner_radius=20)
        frame.place(x=320, y=100)

        parent_tab=customtkinter.CTkTabview(frame, width=1170)
        parent_tab.place(x=15,y=10)

        parent_tab.add('Home')
        parent_tab.add('Services')
        parent_tab.add('View Record')

        frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame1.place(x=30, y=20)
        result = total_customer()
        frame1_label2 = customtkinter.CTkLabel(master=frame1, text="Total \nCustomers \n\n{}".format(result[0]), font=labelfont)
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)



        frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame2.place(x=310, y=20)

        frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame3.place(x=590, y=20)



        frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame4.place(x=870, y=20)



if __name__=='__main__':
    main=customtkinter.CTk()
    Admin_Dashboard(main)
    main.mainloop()




