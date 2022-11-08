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
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
from PIL import ImageTk, Image
import pandas
from tkintermapview import TkinterMapView
from GUI import Login
from tkcalendar import DateEntry, Calendar
from tktimepicker import AnalogPicker, AnalogThemes, constants


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
            login2=Login.Login(root)
            root.mainloop()

        file=Menu(parent_menu, tearoff=0)
        file.add_command(label="Open")
        file.add_command(label="Logout", command=logout)
        file.add_command(label="Exit", command=exit)

        parent_menu.add_cascade(label="File", menu=file)
        self.root.config(menu=parent_menu)



        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.root, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=(10,0), pady=10)

        user_image=ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label=Label(left_frame, image=user_image, bg="#2a2d2e")
        user_image_label.image=user_image
        user_image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, text_font=('Tahoma', 14))
        l1.place(x=70, y=150)
        my_time()

        assigndriver_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame, text="Dashboard             ", hover_color='black',
                                                   text_font=('Times New Roman', 14, 'normal'), width=200,
                                                   image=assigndriver_btn_image, fg_color='#2a2d2e')
        assigndriver_btn.place(x=40, y=250)

        payment_btn_image = ImageTk.PhotoImage(
            Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-account-solid-24.png'))
        payment_btn = customtkinter.CTkButton(master=left_frame, text="My Profile            ", hover_color='black',
                                              text_font=('Times New Roman', 14, 'normal'), width=200,
                                              image=payment_btn_image, fg_color='#2a2d2e')
        payment_btn.place(x=40, y=300)

        managecustomers_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        managecustomers_btn = customtkinter.CTkButton(master=left_frame, text="Booking History     ", hover_color='black',
                                                      text_font=('Times New Roman', 14, 'normal'), width=200,
                                                      image=managecustomers_btn_image, fg_color='#2a2d2e')
        managecustomers_btn.place(x=40, y=350)

        managedrivers_btn_image = ImageTk.PhotoImage(
            Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\car-regular-24.png'))
        managedrivers_btn = customtkinter.CTkButton(master=left_frame, text="Drivers History     ", hover_color='black',
                                                    text_font=('Times New Roman', 14, 'normal'), width=200,
                                                    image=managedrivers_btn_image, fg_color='#2a2d2e')
        managedrivers_btn.place(x=40, y=400)

        manageemployees_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\id-card-regular-24.png'))
        manageemployees_btn = customtkinter.CTkButton(master=left_frame, text="Billing                 ", hover_color='black',
                                                      text_font=('Times New Roman', 14, 'normal'), width=200,
                                                      image=manageemployees_btn_image, fg_color='#2a2d2e')
        manageemployees_btn.place(x=40, y=450)

        viewcustomer_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\key-solid-24.png'))
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="Change Password     ", hover_color='black',
                                                   text_font=('Times New Roman', 14, 'normal'), width=200,
                                                   image=viewcustomer_btn_image, fg_color='#2a2d2e')
        viewcustomer_btn.place(x=40, y=500)

        viewdriver_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\export-regular-24.png'))
        viewdriver_btn = customtkinter.CTkButton(master=left_frame, text="Export Data           ", hover_color='black',
                                                 text_font=('Times New Roman', 14, 'normal'), width=200,
                                                 image=viewdriver_btn_image, fg_color='#2a2d2e')
        viewdriver_btn.place(x=40, y=550)

        logout_btn_image = ImageTk.PhotoImage(Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame, text="Logout                 ", fg_color='#2a2d2e',
                                             hover_color='black',
                                             text_font=('Times New Roman', 14, 'normal'), width=200,
                                             image=logout_btn_image)
        logout_btn.place(x=40, y=600)

        #++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++
        Top_Frame=customtkinter.CTkFrame(master=self.root, height=100, relief=SUNKEN)
        Top_Frame.pack(side=TOP,fill=BOTH, padx=10, pady=10)

        title_lbl = customtkinter.CTkLabel(master=Top_Frame, text="TAXI BOOKING SYSTEM",text_font=('', 16, 'bold'))
        title_lbl.pack(side=LEFT, pady=20, padx=10)

        log_name_lbl=customtkinter.CTkLabel(master=Top_Frame, text="Logged in as: Hancie Phago",
                                            text_font=('',14,'bold'))
        log_name_lbl.pack(side=RIGHT, pady=20, padx=10)

        #+++++++++++++++++++++++++++++++Bottom Frame++++++++++++++++++++++++++++++++++++++++
        # Buttom_Frame = customtkinter.CTkFrame(master=self.root, height=700, relief=SUNKEN)
        # Buttom_Frame.pack(side=BOTTOM, fill=BOTH, padx=10, pady=(0,20))

        style = Style()
        style.theme_create("MyStyle", parent="alt",
                           settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [7, 7]}, }},
                           )
        style.theme_use("MyStyle")
        style.configure('TNotebook.Tab', background="#2a2d2e")
        style.configure('TNotebook.Tab', foreground="white")



        parent_tab=ttk.Notebook(self.root, style='Custom.TNotebook')
        parent_tab.pack(side=TOP, fill=BOTH, padx=10, pady=(0,20), expand=TRUE)

        #++++++++++++++++++++++Home Tab Frame+++++++++++++++++++++++++++++++++++++++++++
        tab1=Frame(parent_tab)
        parent_tab.add(tab1, text="Home")

        tab1_frame=customtkinter.CTkFrame(master=tab1)
        tab1_frame.pack(fill=BOTH,expand=True)

        #+++++++++++++++++++++++++Welcome Label+++++++++++++++++++
        welcome_lbl=customtkinter.CTkLabel(master=tab1_frame, text="Welcome Hancie Phago!", text_font=('', 16,'bold'))
        welcome_lbl.place(x=10,y=20)

        form_font=('Bodoni',15,'normal')

        pickup_address_lbl=Label(tab1_frame, text="Pick up address: ", bg="#2a2d2e", fg="white", font=form_font)
        pickup_address_lbl.place(x=50, y=180)

        pickup_address_txt=customtkinter.CTkEntry(master=tab1_frame, text_font=form_font, width=250)
        pickup_address_txt.place(x=230, y=140)

        date_lbl = Label(tab1_frame, text="Pick up date: ", bg="#2a2d2e", fg="white", font=form_font)
        date_lbl.place(x=50, y=260)

        dt=date.today()
        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='white',
                        arrowcolor='white')

        date_lbl_txt = DateEntry(tab1_frame, font=form_font,width=20,date_pattern='yyyy-MM-dd',
                                 selectmode='day', style='my.DateEntry', background="green", bordercolor="red",
                                 selectbackground="green", mindate=dt, disableddaybackground ="grey")
        date_lbl_txt.place(x=285, y=260)

        pickup_lbl=Label(tab1_frame, text="Pickup time:", font=form_font, bg="#2a2d2e", fg="white",)
        pickup_lbl.place(x=50, y=340)

        def updateTime(time):
            pick_up_time_lbl.insert(0, str("{}:{} {}".format(*time)))

        def time720():
            top = tk.Toplevel(tab1_frame)
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
            ok_btn = customtkinter.CTkButton(master=top, text="Ok", fg_color="#2a2d2e",command=lambda: updateTime(time_picker.time()))
            ok_btn.pack()

        time = ()

        pick_up_time_lbl = customtkinter.CTkEntry(master=tab1_frame,text_font=form_font,  width=250)
        pick_up_time_lbl.place(x=230, y=260)

        time_img=ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\time-five-regular-24.png"))
        pic_up_time_btn = customtkinter.CTkButton(master=tab1_frame,image=time_img,text="", fg_color="black", command=time720, text_font=form_font, width=50)
        pic_up_time_btn.place(x=490, y=260)

        dropoff_lbl = Label(tab1_frame, text="Drop off address:", font=('Bodoni',15,'normal'),bg="#2a2d2e", fg="white", )
        dropoff_lbl.place(x=50, y=410)

        dropoff_txt = customtkinter.CTkEntry(master=tab1_frame, text_font=form_font, width=250)
        dropoff_txt.place(x=230, y=320)

        booking_btn=customtkinter.CTkButton(master=tab1_frame, text="Request Booking", text_font=('Bodoni',17,'normal'))
        booking_btn.place(x=230, y=400)


        myloc = geocoder.ip('me')
        map_widget = TkinterMapView(tab1_frame, width=750, height=765, corner_radius=20)
        map_widget.set_address(myloc, marker=True)
        map_widget.pack(side=RIGHT, fill=BOTH, pady=(10),padx=(0,10))


        #++++++++++++++++++++++Update Booking+++++++++++++++++++++++++
        tab5=Frame(parent_tab)
        parent_tab.add(tab5, text="Update Booking")

        tab5_frame=customtkinter.CTkFrame(master=tab5)
        tab5_frame.pack(fill=BOTH, expand=True)

        tab1_frame=customtkinter.CTkFrame(master=tab1)
        tab1_frame.pack(fill=BOTH, expand=True)

        tab2=Frame(parent_tab)
        parent_tab.add(tab2, text="Riding History")

        tab3=Frame(parent_tab, background="#ffffff")
        parent_tab.add(tab3, text="Report")

        #++++++++++++++++++++++++++Activity Tab Frame++++++++++++++++++++++
        tab4=Frame(parent_tab,)
        parent_tab.add(tab4, text="Activity")

        tab4_frame=customtkinter.CTkFrame(master=tab4)
        tab4_frame.pack(fill=BOTH, expand=True)





        sql_engine = create_engine('mysql+pymysql://root:@localhost/hancie')
        db_connection = sql_engine.connect()

        my_colors = [(.9, .4, .6), (.1, .3, .8)]
        query = 'SELECT * FROM daily_expenses'
        df = pandas.read_sql(query, db_connection, index_col='category')
        fig = df.plot.bar(title="Hancie Phago", y='amount', figsize=(6, 6), color=my_colors, legend=True,
                          grid=False).get_figure()


        plot = FigureCanvasTkAgg(fig, tab3)
        plot.get_tk_widget().place(x=5, y=5)


        query = "SELECT *  FROM daily_expenses"
        df = pandas.read_sql(query, db_connection, index_col='date')
        fig2 = df.plot.line(title="Loan Amount", y='amount', figsize=(5.5, 6)).get_figure();



        plot2 = FigureCanvasTkAgg(fig2, tab3)
        plot2.get_tk_widget().place(x=800, y=5)







if __name__=='__main__':
    root=customtkinter.CTk()
    Customer_Dashboard(root)
    root.mainloop()





