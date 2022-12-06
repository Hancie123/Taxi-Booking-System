from tkinter import *
import customtkinter
import pandas
from PIL import ImageTk, Image
from matplotlib import axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from time import strftime

from dbms.driver_management import update_DriverStatus, driver_select_all
from libs import Global
from libs.driver_libs import Driver_Libs


#++++++++++++++++++++++++++++++++GUI DESIGNING++++++++++++++++++++++++++++++++
class Driver_Dashboard():

    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        self.main.title("Driver Dashboard")
        self.main.state('zoomed')
        self.main.bind('<Escape>', lambda e: main.destroy())
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        titlefont = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        labelfont = customtkinter.CTkFont(family='Times New Roman', size=22, weight='normal')
        sidemenufont = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        messagefont = customtkinter.CTkFont(family='Times New Roman', size=16, weight='normal')

        driverid=Entry(self.main)
        driverid.insert(0, Global.currentDriver[0])

#++++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++
        leftFrame=customtkinter.CTkFrame(self.main, width=300)
        leftFrame.pack(side=LEFT, fill=BOTH)

        Cover_Image = Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(leftFrame, image=photo1, bg="#2a2d2e")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=100, y=40)

        def switch():
            global is_on

            if is_on:
                toggleButton.config(image=off)
                is_on = False
                driveridd = driverid.get()
                driverInfo = Driver_Libs(did=driveridd, driverstatus='Inactive')
                updateresult = update_DriverStatus(driverInfo)
                if updateresult == True:
                    toogleLABEL.configure(text="Driver {} is Inactive".format(Global.currentDriver[0]))

            else:
                toggleButton.config(image=on)
                is_on = True
                driveridd = driverid.get()
                driverInfo = Driver_Libs(did=driveridd, driverstatus='Active')
                updateresult = update_DriverStatus(driverInfo)
                if updateresult == True:
                    toogleLABEL.configure(text="Driver {} is Active".format(Global.currentDriver[0]))


        on = ImageTk.PhotoImage(
            Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\left.png'))
        off = ImageTk.PhotoImage(
            Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\right.png'))

        toggleButton = Button(leftFrame, bg="#2a2d2e", image=on, bd=0, command=switch, activebackground="#2a2d2e")
        toggleButton.place(x=80, y=300)
        def my_time():

            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=leftFrame, font=sidemenufont)
        l1.place(x=90, y=150)
        my_time()

        global is_on
        is_on = True

        # Define our switch function

        def switch2():
            global is_on
            driverid1=driverid.get()
            selectResult=driver_select_all(driverid1)
            if selectResult!=None:
                if selectResult[7]=='Active':
                    toggleButton.config(image=on)
                elif selectResult[7]=='Inactive':
                    toggleButton.config(image=off)
                    print("This is inactive")
            else:
                pass


        switch2()




        toogleLABEL=customtkinter.CTkLabel(leftFrame, text='', font=sidemenufont)
        toogleLABEL.place(x=80, y=350)

        themelbl = customtkinter.CTkLabel(leftFrame, text="Appearance Mode:", font=sidemenufont)
        themelbl.place(x=50, y=650)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice=='light':
                Cover_Image_label['bg']="#dbdbdb"
                toggleButton['bg']="#dbdbdb"
            if choice=='dark':
                Cover_Image_label['bg'] = "#2b2b2b"
                toggleButton['bg'] = "#2b2b2b"


        combobox = customtkinter.CTkComboBox(master=leftFrame, values=["dark",'light'],
                                             command=combobox_callback, font=sidemenufont)
        combobox.place(x=55, y=690)
        combobox.set("dark")

        #+++++++++++++++++++++++++++Top Label++++++++++++++++++++++++++=
        welcomelbl=customtkinter.CTkLabel(master=self.main, text="Welcome Neuve Limbu", font=sidemenufont)
        welcomelbl.place(x=350, y=20)

        messagelabel = customtkinter.CTkLabel(master=self.main, text="You have 2 new riding request", font=messagefont)
        messagelabel.place(x=380, y=50)

        logoutbtn=customtkinter.CTkButton(master=self.main, text="Logout", font=('', 14),text_color="white", fg_color="black", hover_color="red")
        logoutbtn.place(x=1350, y=20)

#++++++++++++++++++++++++++++Top Frame++++++++++++++++++++++++++++++++++++++++++++++
        topFrame=customtkinter.CTkFrame(self.main, height=220)
        topFrame.pack(side=TOP, fill=BOTH, pady=(80,10), padx=10)

        ridingCompleted=customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        ridingCompleted.place(x=40, y=10)

        ridingLabel=customtkinter.CTkLabel(master=ridingCompleted, text="Total Riding \nCompleted 4", font=labelfont)
        ridingLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        totalbooked = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalbooked.place(x=330, y=10)

        totalactive = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalactive.place(x=620, y=10)

        totalpaid = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalpaid.place(x=910, y=10)

#++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame=customtkinter.CTkFrame(self.main)
        centerFrame.pack(side=TOP, fill=BOTH, expand=True, pady=(0,10), padx=10)

if __name__=='__main__':
    main=customtkinter.CTk()
    Driver_Dashboard(main)
    main.mainloop()
