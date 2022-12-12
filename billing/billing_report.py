from tkinter import *

import pandas
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import customtkinter

class CustomerReport():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Customer Report")
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        self.main.title("Taxi Booking System")
        self.main.resizable(0, 0)
        frame_width = 900
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate + 200, y_cordinate))

        font1 = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')

        topFrame=customtkinter.CTkFrame(self.main, height=100)
        topFrame.pack(side=TOP, fill=BOTH)

        titlelabel=customtkinter.CTkLabel(topFrame, text='CUSTOMER REPORT', font=font1)
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame=Frame(self.main, bg="white")
        frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        create_engine1=create_engine('mysql+pymysql://root:@localhost/taxi_booking_system')
        dbConnection=create_engine1.connect()

        query='select gender,count(cid) as Customer from customers group by gender'
        df=pandas.read_sql(query, dbConnection, index_col='gender')
        fig=df.plot.pie(title="No. of Male and Female Accounts", y='Customer',autopct='%1.0f%%', figsize=(5,5)).get_figure()
        plot2=FigureCanvasTkAgg(fig, frame)
        plot2.get_tk_widget().place(x=20, y=30)


        query2='select *,count(cid) as ID from booking group by date'
        df2=pandas.read_sql(query2, dbConnection, index_col='date')
        fig2=df2.plot.line(title="Daily Customer Booking Analysis", y='ID', figsize=(5,5)).get_figure()
        plot2=FigureCanvasTkAgg(fig2, frame)
        plot2.get_tk_widget().place(x=550, y=0)



if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerReport(main)
    main.mainloop()