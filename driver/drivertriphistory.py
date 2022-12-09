from tkinter import *
import customtkinter
from tkinter import ttk

from dbms.driver_history_backend import customer_driver_history
from dbms.driver_management import driver_trip_history
from libs import Global


class DriverHistory():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("{} Trip History".format(Global.currentDriver[1]))
        self.main.resizable(0, 0)
        frame_width = 900
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate+50, y_cordinate+50))
        self.main.bind("<Escape>", lambda e:self.main.destroy())
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        font1 = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')

        topFrame = customtkinter.CTkFrame(self.main, height=80)
        topFrame.pack(side=TOP, fill=BOTH)

        titlelabel = customtkinter.CTkLabel(topFrame, text='{} Trip History'.format(Global.currentDriver[1]), font=font1)
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#2b2b2b",
                         foreground="white",
                         rowheight=25,
                         fieldbackground="#2b2b2b",
                         bordercolor="#343638",
                         borderwidth=0,
                         font=('Times New Roman', 16))
        style1.map('Treeview', background=[('selected', '#22559b')])

        style1.configure("Treeview.Heading",
                         background="#565b5e",
                         foreground="white",
                         relief="flat",
                         font=('Times New Roman', 17))
        style1.map("Treeview.Heading",
                   background=[('active', '#3484F0')], )

        treeView=ttk.Treeview(self.main)
        treeView.pack(side=BOTTOM, fill=BOTH, expand=True)
        treeView['columns']=('cid', 'name','date', 'time','pickupaddress','dropoffaddress')
        treeView.column('#0', width=0, stretch=0)
        treeView.column('cid', width=100, anchor=CENTER)
        treeView.column('name', width=100, anchor=CENTER)
        treeView.column('date', width=100, anchor=CENTER)
        treeView.column('time', width=100, anchor=CENTER)
        treeView.column('pickupaddress', width=100, anchor=CENTER)
        treeView.column('dropoffaddress', width=100, anchor=CENTER)


        treeView.heading('#0', text='', anchor=CENTER)
        treeView.heading('cid',text='Customer ID', anchor=CENTER)
        treeView.heading('name', text='Customer Name', anchor=CENTER)
        treeView.heading('date', text='Date', anchor=CENTER)
        treeView.heading('time', text='Time', anchor=CENTER)
        treeView.heading('pickupaddress', text='Pickup address', anchor=CENTER)
        treeView.heading('dropoffaddress', text='Dropoff address', anchor=CENTER)


        driverid=Entry(self.main)
        driverid.insert(0, Global.currentDriver[0])


        def triphistory():
            id=driverid.get()

            driverResult=driver_trip_history(id)

            for ro in driverResult:
                treeView.insert(parent='', index='end', values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))


        triphistory()







if __name__=='__main__':
    main=customtkinter.CTk()
    DriverHistory(main)
    main.mainloop()