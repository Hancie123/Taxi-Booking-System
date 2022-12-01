import tkinter
from tkinter import *
import customtkinter
from datetime import date, time
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from datetime import time, date
import math
import tkinter as tk
import time
from time import strftime
import geocoder
import tkintermapview
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
from PIL import ImageTk, Image
import pandas
from tkintermapview import TkinterMapView
from tkcalendar import DateEntry, Calendar
from tktimepicker import AnalogPicker, AnalogThemes, constants
from customer import login, customerprofile
from libs import Global




class Customer_Dashboard(customtkinter.CTk):

    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.root.title("Customer Dashboard | Taxi Booking System")
        # self.root.screen_width = root.winfo_screenwidth()
        # self.root.screen_height = root.winfo_screenwidth()
        # self.root.minsize(self.root.screen_width, self.root.screen_height)
        self.root.state('zoomed')
        self.root.bind('<Escape>', lambda e: root.destroy())
        self.root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        #++++++++++++++++++++++++++++++Menu+++++++++++++++++++++++++++++++=
        parent_menu=Menu(self.root)

        def exit():
            self.root.destroy()

        def logout():
            self.root.destroy()
            root=customtkinter.CTk()
            login2=login.Login(root)
            root.mainloop()

        file=Menu(parent_menu, tearoff=0)
        file.add_command(label="Open")
        file.add_command(label="Logout", command=logout)
        file.add_command(label="Exit", command=exit)

        parent_menu.add_cascade(label="File", menu=file)
        self.root.config(menu=parent_menu)

        #++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        titlefont = customtkinter.CTkFont(family='Times New Roman', size=25, weight='normal')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        labelfont=customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        sidemenufont = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')



        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.root, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=(10,0), pady=10)

        Cover_Image = Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(left_frame, image=photo1, bg="#2a2d2e")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=font720)
        l1.place(x=90, y=150)
        my_time()

        assigndriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame, text="Dashboard             ", hover_color='black',
                                                   font=sidemenufont, width=200,
                                                   image=assigndriver_btn_image, fg_color='#2a2d2e')
        assigndriver_btn.place(x=40, y=250)

        def open_profile():
            main = customtkinter.CTkToplevel()
            customerprofile.CustomerProfile(main)
            main.mainloop()

        profile_img = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-account-solid-24.png'))
        profile_btn = customtkinter.CTkButton(master=left_frame, text="My Profile            ", hover_color='black',font=sidemenufont, width=200,command=open_profile, image=profile_img, fg_color='#2a2d2e')
        profile_btn.place(x=40, y=300)

        managecustomers_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        managecustomers_btn = customtkinter.CTkButton(master=left_frame, text="Booking History     ", hover_color='black',font=sidemenufont, width=200,image=managecustomers_btn_image, fg_color='#2a2d2e')
        managecustomers_btn.place(x=40, y=350)

        managedrivers_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\car-regular-24.png'))
        managedrivers_btn = customtkinter.CTkButton(master=left_frame, text="Drivers History     ", hover_color='black',font=sidemenufont, width=200,image=managedrivers_btn_image, fg_color='#2a2d2e')
        managedrivers_btn.place(x=40, y=400)

        billing_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\id-card-regular-24.png'))
        billing_btn = customtkinter.CTkButton(master=left_frame, text="Billing                   ", hover_color='black',font=sidemenufont, width=200,image=billing_btn_image, fg_color='#2a2d2e')
        billing_btn.place(x=40, y=450)

        viewcustomer_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\key-solid-24.png'))
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="Change Password     ", hover_color='black',font=sidemenufont, width=200,image=viewcustomer_btn_image, fg_color='#2a2d2e')
        viewcustomer_btn.place(x=40, y=500)

        viewdriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\export-regular-24.png'))
        viewdriver_btn = customtkinter.CTkButton(master=left_frame, text="Export Data           ", hover_color='black',font=sidemenufont, width=200,image=viewdriver_btn_image, fg_color='#2a2d2e')
        viewdriver_btn.place(x=40, y=550)

        def logout():
            self.root.destroy()
            root=customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        logout_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame, text="Logout                 ", fg_color='#2a2d2e',
                                             hover_color='black',
                                             font=sidemenufont, width=200,
                                           command=logout,  image=logout_btn_image)
        logout_btn.place(x=40, y=600)

        themelbl=customtkinter.CTkLabel(left_frame, text="Appearance Mode:", font=sidemenufont)
        themelbl.place(x=50, y=650)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)

        combobox = customtkinter.CTkComboBox(master=left_frame,values=["dark", "system", 'light'],command=combobox_callback, font=sidemenufont)
        combobox.place(x=55, y=690)
        combobox.set("dark")  # set initial value



        #++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++
        Top_Frame=customtkinter.CTkFrame(master=self.root, height=100)
        Top_Frame.pack(side=TOP,fill=BOTH, padx=10, pady=10)

        title_lbl = customtkinter.CTkLabel(master=Top_Frame, text="TAXI BOOKING SYSTEM",font=('', 16, 'bold'))
        title_lbl.pack(side=LEFT, pady=20, padx=10)

        # log_name_lbl=customtkinter.CTkLabel(master=Top_Frame, text="Welcome: {}".format(Global.currentUser[1]),
        #                                     font=titlefont)
        # log_name_lbl.pack(side=RIGHT, pady=20, padx=10)

        #+++++++++++++++++++++++++++++++Bottom Frame++++++++++++++++++++++++++++++++++++++++

        parent_tab=customtkinter.CTkTabview(self.root)
        parent_tab.pack(side=TOP, fill=BOTH, padx=10, pady=(0,20), expand=TRUE)

        #++++++++++++++++++++++Home Tab Frame+++++++++++++++++++++++++++++++++++++++++++
        parent_tab.add("Home")




        #+++++++++++++++++++++++++Welcome Label+++++++++++++++++++
        # welcome_lbl=customtkinter.CTkLabel(master=parent_tab.tab('Home'), text="Welcome {}".format(Global.currentUser[1]), font=titlefont)
        # welcome_lbl.place(x=10,y=20)

        pickup_address_lbl=customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pick up address: ",font=labelfont)
        pickup_address_lbl.place(x=50, y=140)

        pickup_address_txt=customtkinter.CTkEntry(master=parent_tab.tab('Home'), font=font720, width=250)
        pickup_address_txt.place(x=230, y=140)

        date_lbl = customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pick up date: ",font=labelfont)
        date_lbl.place(x=50, y=210)

        dt=date.today()
        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='white',
                        arrowcolor='white')

        date_lbl_txt = DateEntry(parent_tab.tab('Home'), font=('Times New Roman', 20,'normal'), width=22, date_pattern='yyyy-MM-dd',
                                 selectmode='day', style='my.DateEntry', background="green", bordercolor="red",
                               selectbackground="green", mindate=dt, disableddaybackground ="grey")
        date_lbl_txt.place(x=285, y=260)

        pickup_lbl=customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pickup time:", font=labelfont)
        pickup_lbl.place(x=50, y=270)

        def updateTime(time):
            pick_up_time_lbl.insert(0, str("{}:{} {}".format(*time)))

        def time720():
            top = customtkinter.CTkToplevel(parent_tab.tab('Home'))
            top.title("Taxi Booking System")
            top.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
            top.resizable(0,0)
            frame_width = 400
            frame_height = 500
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            top.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))
            time_picker = AnalogPicker(top, type=constants.HOURS12)
            time_picker.pack(expand=True, fill="both")
            theme = AnalogThemes(time_picker)
            theme.setDracula()
            ok_btn = customtkinter.CTkButton(master=top, text="Ok",command=lambda: updateTime(time_picker.time()))
            ok_btn.pack()

        time = ()

        pick_up_time_lbl = customtkinter.CTkEntry(master=parent_tab.tab('Home'),font=font720,  width=250)
        pick_up_time_lbl.place(x=230, y=270)

        time_img=customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\time-five-regular-24.png"))
        pic_up_time_btn = customtkinter.CTkButton(master=parent_tab.tab('Home'),image=time_img,text="", fg_color="black", command=time720, font=font720, width=50)
        pic_up_time_btn.place(x=490, y=270)

        dropoff_lbl = customtkinter.CTkLabel(parent_tab.tab('Home'), text="Drop off address:", font=labelfont )
        dropoff_lbl.place(x=50, y=330)

        dropoff_txt = customtkinter.CTkEntry(master=parent_tab.tab('Home'), font=font720, width=250)
        dropoff_txt.place(x=230, y=330)

        booking_btn=customtkinter.CTkButton(master=parent_tab.tab('Home'), text="Request Booking", font=labelfont)
        booking_btn.place(x=230, y=400)


        # myloc = geocoder.ip('me')
        # map_widget = tkintermapview.TkinterMapView(parent_tab.tab('Home'), width=300)
        # map_widget.set_address(myloc, marker=True)
        # map_widget.pack(side=RIGHT, fill=BOTH, pady=(10),padx=(0,10))


        #++++++++++++++++++++++Update Booking+++++++++++++++++++++++++
        parent_tab.add("Update Booking")

        tab5_frame=customtkinter.CTkFrame(master=parent_tab.tab('Update Booking'))
        tab5_frame.pack(fill=BOTH, expand=True)


        parent_tab.add("Riding History")


        parent_tab.add("Report")
        parent_tab.tab('Report').configure(fg_color="white")

        #++++++++++++++++++++++++++Activity Tab Frame++++++++++++++++++++++
        parent_tab.add("Activity")

        tab4_frame=customtkinter.CTkFrame(master=parent_tab.tab('Activity'))
        tab4_frame.pack(fill=BOTH, expand=True)





        sql_engine = create_engine('mysql+pymysql://root:@localhost/hancie')
        db_connection = sql_engine.connect()

        my_colors = [(.9, .4, .6), (.1, .3, .8)]
        query = 'SELECT * FROM daily_expenses'
        df = pandas.read_sql(query, db_connection, index_col='category')
        fig = df.plot.bar(title="Hancie Phago", y='amount', figsize=(6, 6), color=my_colors, legend=True,
                          grid=False).get_figure()


        plot = FigureCanvasTkAgg(fig, parent_tab.tab('Report'))
        plot.get_tk_widget().place(x=5, y=5)


        query = "SELECT *  FROM daily_expenses"
        df = pandas.read_sql(query, db_connection, index_col='date')
        fig2 = df.plot.line(title="Loan Amount", y='amount', figsize=(5.5, 6)).get_figure();



        plot2 = FigureCanvasTkAgg(fig2, parent_tab.tab('Report'))
        plot2.get_tk_widget().place(x=800, y=5)







if __name__=='__main__':
    root=customtkinter.CTk()
    Customer_Dashboard(root)
    root.mainloop()





