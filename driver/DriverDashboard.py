from tkinter import *
import customtkinter
import pandas
from PIL import ImageTk, Image
from matplotlib import axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from time import strftime
from tkinter import ttk

from tktimepicker import AnalogThemes, AnalogPicker, constants

from customer import login
from dbms.booking_backend import total_booking, select_all, driver_update_booking
from dbms.customer_backend import total_customer
from dbms.driver_management import update_DriverStatus, driver_select_all, total_driver, driver_selectallbooking
from dbms.employees_backend import total_employees
from driver import drivertriphistory
from libs import Global
from libs.booking_libs import BookingLibs
from libs.driver_libs import Driver_Libs


#++++++++++++++++++++++++++++++++GUI DESIGNING++++++++++++++++++++++++++++++++
class Driver_Dashboard():

    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        self.main.title("Driver Dashboard | Welcome {}".format(Global.currentDriver[1]))
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

        #++++++++++++++++++++++++++++TOP FRAME+++++++++++++++++++++++++++++++++++
        topFrame=customtkinter.CTkFrame(self.main, height=80)
        topFrame.pack(side=TOP, fill=BOTH)

        # +++++++++++++++++++++++++++Top Label++++++++++++++++++++++++++=
        welcomelbl = customtkinter.CTkLabel(master=self.main, text="DRIVER DASHBOARD",fg_color="#2b2b2b", font=('Times New Roman', 25, 'bold'))
        welcomelbl.place(x=100, y=25)

        def logout():
            self.main.destroy()
            main=customtkinter.CTk()
            login.Login(main)
            main.mainloop()

        #+++++++++++++++++++++++++++++++++++LOGOUT BUTTON++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        logoutbtn = customtkinter.CTkButton(master=self.main, text="Logout",command=logout, font=('Times New Roman', 20, 'bold'), text_color="white",fg_color="black", hover_color="red")
        logoutbtn.place(x=1350, y=25)

#++++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++
        leftFrame=customtkinter.CTkFrame(self.main, width=300)
        leftFrame.pack(side=LEFT, fill=BOTH, padx=(10,0), pady=10)

        Cover_Image = Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(leftFrame, image=photo1, bg="#2a2d2e")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=100, y=40)

        def assign_driver():
            root=customtkinter.CTkToplevel()
            root.title("Taxi Booking System")
            width = 1250
            height = 450
            myscreenwidth = self.main.winfo_screenwidth()
            myscreenheight = self.main.winfo_screenheight()
            xCordinate = int((myscreenwidth / 2) - (width / 2))
            yCordinate = int((myscreenheight / 2) - (height / 2))
            root.geometry('{}x{}+{}+{}'.format(width, height, xCordinate + 100, yCordinate))
            root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
            root.resizable(0,0)

            assignbookingFrame=customtkinter.CTkFrame(root, width=400, corner_radius=20)
            assignbookingFrame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

            title11lbl=customtkinter.CTkLabel(master=assignbookingFrame, text="COMPLETE TRIPS", font=font720)
            title11lbl.place(x=110, y=20)

            bookingidlbl = customtkinter.CTkLabel(assignbookingFrame, text="ID: ",font=font720)
            bookingidlbl.place(x=30, y=100)

            bookingidtxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            bookingidtxt.place(x=140, y=100)

            datelbl = customtkinter.CTkLabel(assignbookingFrame, text="Date: ", font=font720)
            datelbl.place(x=30, y=150)

            datetxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            datetxt.place(x=140, y=150)

            namelbl = customtkinter.CTkLabel(assignbookingFrame, text="Name:", font=font720)
            namelbl.place(x=30, y=200)

            nametxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            nametxt.place(x=140, y=200)

            statuslbl = customtkinter.CTkLabel(assignbookingFrame, text="Status:", font=font720)
            statuslbl.place(x=30, y=250)

            comboData=('Completed','Incomplete')
            bookingCombo = customtkinter.CTkComboBox(assignbookingFrame,values=comboData, font=font720, width=200)
            bookingCombo.place(x=140, y=250)

            customerid=customtkinter.CTkEntry(assignbookingFrame)
            bookingid = customtkinter.CTkEntry(assignbookingFrame)


            updatebookingresultlbl = customtkinter.CTkLabel(assignbookingFrame, text="", font=font720)
            updatebookingresultlbl.place(x=80, y=390)

            assinbookingframe2 = customtkinter.CTkFrame(master=root, width=840)
            assinbookingframe2.pack(side=LEFT, fill=BOTH, padx=(0, 10), pady=10)

            bookingTable = ttk.Treeview(assinbookingframe2)
            bookingTable['columns'] = ('bookingid', 'pickupaddress', 'date', 'time', 'dropoffaddress', 'name', 'bookingstatus')
            bookingTable.column('#0', width=0, stretch=0)
            bookingTable.column('bookingid', width=100, anchor=CENTER)
            bookingTable.column('pickupaddress', width=200, anchor=CENTER)
            bookingTable.column('date', width=100, anchor=CENTER)
            bookingTable.column('time', width=100, anchor=CENTER)
            bookingTable.column('dropoffaddress', width=200, anchor=CENTER)
            bookingTable.column('name', width=150, anchor=CENTER)
            bookingTable.column('bookingstatus', width=150, anchor=CENTER)

            bookingTable.heading('#0', text='', anchor=CENTER)
            bookingTable.heading('bookingid', text='ID', anchor=CENTER)
            bookingTable.heading('pickupaddress', text='Pickup address', anchor=CENTER)
            bookingTable.heading('date', text='Date', anchor=CENTER)
            bookingTable.heading('time', text='Time', anchor=CENTER)
            bookingTable.heading('dropoffaddress', text='Dropoff address', anchor=CENTER)
            bookingTable.heading('name', text='Name', anchor=CENTER)
            bookingTable.heading('bookingstatus', text='Booking Status', anchor=CENTER)

            def bookingtable():
                id = driverid.get()
                driverResult = driver_selectallbooking(id)
                i = 0
                for x in driverResult:
                    bookingTable.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
                    i = i + 1

            bookingTable.pack(padx=10, pady=10)

            def getDriverDetail(a):
                bookingidtxt.delete(0, END)
                datetxt.delete(0, END)
                nametxt.delete(0, END)


                selectitem2 = bookingTable.selection()[0]

                bookingidtxt.insert(0, bookingTable.item(selectitem2)['values'][0])
                datetxt.insert(0, bookingTable.item(selectitem2)['values'][2])
                nametxt.insert(0, bookingTable.item(selectitem2)['values'][5])



            bookingTable.bind("<<TreeviewSelect>>", getDriverDetail)

            def update_customer_booking():

                bookingidtxt.get()
                datetxt.get()
                nametxt.get()
                driverid.get()


                updatebooking = BookingLibs(bookingstatus='Bill Pending', bookingid=bookingidtxt.get())
                updatebookingResult = driver_update_booking(updatebooking)

                driver = Driver_Libs(did=driverid.get(), driverstatus='Active')
                updateresult = update_DriverStatus(driver)

                if updatebookingResult == True:
                    updatebookingresultlbl.configure(text="The Trip is {} Successfully".format(bookingCombo.get()))
                    bookingTable.delete(*bookingTable.get_children())
                    bookingtable()
                    treeView.delete(*treeView.get_children())
                    show_booking()
                    switch2()


                else:
                    updatebookingresultlbl.configure(text="Error Occurred")

            assign_btn = customtkinter.CTkButton(assignbookingFrame, command=update_customer_booking,text="Complete Trip",font=font720, width=150)
            assign_btn.place(x=150, y=330)

            bookingtable()
            root.mainloop()

        completetrip_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        completetrip_btn = customtkinter.CTkButton(master=leftFrame, text="Complete Trips   ", command=assign_driver, hover_color='black', font=sidemenufont, width=200,image=completetrip_image, fg_color='#2b2b2b')
        completetrip_btn.place(x=40, y=250)

        payment_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\paypal-logo-24.png'))
        payment_btn = customtkinter.CTkButton(master=leftFrame, text="Payment              ", hover_color='black',font=sidemenufont, width=200, image=payment_btn_image, fg_color='#2b2b2b')
        payment_btn.place(x=40, y=300)

        def trip_history_gui():
            root=customtkinter.CTkToplevel()
            drivertriphistory.DriverHistory(root)
            root.mainloop()

        trip_image = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        trip_btn = customtkinter.CTkButton(master=leftFrame, text="Trips History        ", command=trip_history_gui,hover_color='black', font=sidemenufont, width=200,image=trip_image, fg_color='#2b2b2b')
        trip_btn.place(x=40, y=350)

        def switch():
            global is_on

            if is_on:
                toggleButton.config(image=off)
                is_on = False
                driveridd = driverid.get()
                driverInfo = Driver_Libs(did=driveridd, driverstatus='Inactive')
                updateresult = update_DriverStatus(driverInfo)
                if updateresult == True:
                    toogleLABEL.configure(text="{} is Inactive".format(Global.currentDriver[1]))

            else:
                toggleButton.config(image=on)
                is_on = True
                driveridd = driverid.get()
                driverInfo = Driver_Libs(did=driveridd, driverstatus='Active')
                updateresult = update_DriverStatus(driverInfo)
                if updateresult == True:
                    toogleLABEL.configure(text="{} is Active".format(Global.currentDriver[1]))


        on = ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\left.png'))
        off = ImageTk.PhotoImage(Image.open('E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\right.png'))

        toggleButton = Button(leftFrame, bg="#2a2d2e", image=on, bd=0, command=switch, activebackground="#2a2d2e")
        toggleButton.place(x=140, y=650)

        toogleLABEL = customtkinter.CTkLabel(leftFrame, text='', font=sidemenufont)
        toogleLABEL.place(x=45, y=560)
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
                if selectResult[6]=='Active':
                    toggleButton.config(image=on)
                    toogleLABEL.configure(text="{} is Active".format(Global.currentDriver[1]))
                elif selectResult[6]=='Inactive':
                    toggleButton.config(image=off)
                    toogleLABEL.configure(text="{} is Inactive".format(Global.currentDriver[1]))

                elif selectResult[6]=='Booked':
                    toggleButton.config(image=off)
                    toogleLABEL.configure(text="{} is Booked".format(Global.currentDriver[1]))

            else:
                pass


        switch2()




        themelbl = customtkinter.CTkLabel(leftFrame, text="Appearance Mode:", font=sidemenufont)
        themelbl.place(x=50, y=600)

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
        combobox.place(x=55, y=640)
        combobox.set("dark")



        #++++++++++++++++++++++++++++Top Frame++++++++++++++++++++++++++++++++++++++++++++++

        centerFrame = customtkinter.CTkFrame(master=self.main,corner_radius=20)
        centerFrame.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10)

        parent_tab = customtkinter.CTkTabview(centerFrame, height=240)
        parent_tab.pack(side=TOP, fill=BOTH)

        parent_tab.add('Home')
        parent_tab.add('Search')
        parent_tab.add('Records')

        # +++++++++++++++++++++++++++++++++++Home Tab 1 Frame++++++++++++++++++++++++++++++++++++
        frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame1.place(x=30, y=20)
        result = total_customer()
        tmpResult = result[0]
        frame1_label2 = customtkinter.CTkLabel(master=frame1, text="Total \nCustomers \n\n{}".format(tmpResult[0]),
                                               font=labelfont)
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 2 Frame++++++++++++++++++++++++++++++++++++
        frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame2.place(x=310, y=20)
        bookingResult = total_booking()
        bookingresult2 = bookingResult[0]
        frame2_label2 = customtkinter.CTkLabel(master=frame2, text="Total \nBookings \n\n{}".format(bookingresult2[0]),
                                               font=labelfont)
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 3 Frame++++++++++++++++++++++++++++++++++++
        frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame3.place(x=590, y=20)
        driverResult = total_driver()
        driveresult2 = driverResult[0]
        frame3_label2 = customtkinter.CTkLabel(master=frame3, text="Total \nDrivers \n\n{}".format(driveresult2[0]),
                                               font=labelfont)
        frame3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 4 Frame++++++++++++++++++++++++++++++++++++
        frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame4.place(x=870, y=20)
        employeesResult = total_employees()
        employeesResult2 = employeesResult[0]
        frame4_label2 = customtkinter.CTkLabel(master=frame4,
                                               text="Total \nEmployees \n\n{}".format(employeesResult2[0]),
                                               font=labelfont)
        frame4_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # # +++++++++++++++++++++++++++++++++++Service Tab 1 Frame++++++++++++++++++++++++++++++++++++
        # tab2frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        # tab2frame1.place(x=30, y=20)
        #
        # def search_customers11():
        #     root = customtkinter.CTkToplevel()
        #     search_customers.SearchCustomer(root)
        #     root.mainloop()
        #
        # frame1_label1 = customtkinter.CTkButton(master=tab2frame1, text="Search \nCustomer", command=search_customers11,
        #                                         font=labelfont, fg_color='#2b2b2b', )
        # frame1_label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Service Tab 2 Frame++++++++++++++++++++++++++++++++++++
        # tab2frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        # tab2frame2.place(x=310, y=20)
        #
        # def search_drivers11():
        #     root = customtkinter.CTkToplevel()
        #     search_drivers.SearchDrivers(root)
        #     root.mainloop()
        #
        # frame2_label2 = customtkinter.CTkButton(master=tab2frame2, text="Search \nDrivers", command=search_drivers11,
        #                                         font=labelfont, fg_color='#2b2b2b', )
        # frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Service Tab 3 Frame++++++++++++++++++++++++++++++++++++
        # tab2frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        # tab2frame3.place(x=590, y=20)
        #
        # def search_employees11():
        #     root = customtkinter.CTkToplevel()
        #     search_employees.SearchEmployees(root)
        #     root.mainloop()
        #
        # frame3_label3 = customtkinter.CTkButton(master=tab2frame3, text="Search \nEmployees",
        #                                         command=search_employees11, font=labelfont, fg_color='#2b2b2b', )
        # frame3_label3.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Report Tab 1 Frame++++++++++++++++++++++++++++++++++++
        # tab3frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        # tab3frame1.place(x=30, y=20)
        #
        # def customer_report720():
        #     root = customtkinter.CTkToplevel()
        #     customer_report.CustomerReport(root)
        #     root.mainloop()
        #
        # tab3_label1 = customtkinter.CTkButton(master=tab3frame1, text="Customer \nReports", command=customer_report720,
        #                                       font=labelfont, fg_color='#2b2b2b', )
        # tab3_label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Report Tab 2 Frame++++++++++++++++++++++++++++++++++++
        # tab3frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        # tab3frame2.place(x=310, y=20)
        #
        # def driver_report720():
        #     root = customtkinter.CTkToplevel()
        #     driver_report.DriverReport(root)
        #     root.mainloop()
        #
        # tab3_label2 = customtkinter.CTkButton(master=tab3frame2, text="Driver \nReports", command=driver_report720,
        #                                       font=labelfont, fg_color='#2b2b2b', )
        # tab3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Report Tab 3 Frame++++++++++++++++++++++++++++++++++++
        # tab3frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        # tab3frame3.place(x=590, y=20)
        #
        # def booking_report720():
        #     root = customtkinter.CTkToplevel()
        #     booking_report.BookingReport(root)
        #     root.mainloop()
        #
        # tab3_label3 = customtkinter.CTkButton(master=tab3frame3, text="Booking \nReports", command=booking_report720,
        #                                       font=labelfont, fg_color='#2b2b2b', )
        # tab3_label3.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # # +++++++++++++++++++++++++++++++++++Report Tab 4 Frame++++++++++++++++++++++++++++++++++++
        # tab4frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        # tab4frame4.place(x=870, y=20)
        # tab4_label4 = customtkinter.CTkButton(master=tab4frame4, text="Billing \nReports", font=labelfont,
        #                                       fg_color='#2b2b2b', )
        # tab4_label4.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        treeView=ttk.Treeview(centerFrame)
        treeView.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        treeView['columns']=('bookingid','pickupaddress','date', 'time','dropoffaddress','name','bookingstatus')
        treeView.column('#0', width=0, stretch=0)
        treeView.column('bookingid', width=100, anchor=CENTER)
        treeView.column('pickupaddress', width=100, anchor=CENTER)
        treeView.column('date', width=100, anchor=CENTER)
        treeView.column('time', width=100, anchor=CENTER)
        treeView.column('dropoffaddress', width=100, anchor=CENTER)
        treeView.column('name', width=100, anchor=CENTER)
        treeView.column('bookingstatus', width=100, anchor=CENTER)

        treeView.heading('#0', text='', anchor=CENTER)
        treeView.heading('bookingid', text='Booking ID', anchor=CENTER)
        treeView.heading('pickupaddress', text='Pickup address', anchor=CENTER)
        treeView.heading('date', text='Date', anchor=CENTER)
        treeView.heading('time', text='Time', anchor=CENTER)
        treeView.heading('dropoffaddress', text='Dropoff address', anchor=CENTER)
        treeView.heading('name', text='Name', anchor=CENTER)
        treeView.heading('bookingstatus', text='Booking Status', anchor=CENTER)

        def show_booking():

            id=driverid.get()
            driverResult=driver_selectallbooking(id)
            i=0
            for x in driverResult:
                treeView.insert(parent='', index='end', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]) )
                i=i+1

        show_booking()





if __name__=='__main__':
    main=customtkinter.CTk()
    Driver_Dashboard(main)
    main.mainloop()
