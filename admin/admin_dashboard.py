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
from tkinter import messagebox
from sqlalchemy import create_engine
from tktimepicker import AnalogPicker, AnalogThemes,constants

from admin import booking_report
from billing import admin_payment
from customer import customer_management, login, customer_report, search_customers
from dbms.booking_backend import total_booking, select_all, update_booking
from dbms.customer_backend import total_customer
from dbms.driver_management import total_driver, available_driver, update_DriverStatus
from dbms.employees_backend import total_employees
from driver import driver_registration, driver_report, search_drivers
from employees import employees_management, search_employees
from libs import Global
from libs.booking_libs import BookingLibs
from libs.driver_libs import Driver_Libs


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


        #++++++++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++++++++++
        north_frame = customtkinter.CTkFrame(master=self.main, height=80, corner_radius=0)
        north_frame.pack(side=TOP, fill=BOTH)

        # +++++++++++++++++++++++++++++++++++Welcome Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        welcomelabel = customtkinter.CTkLabel(master=north_frame, text="Welcome {}".format(Global.currentAdmin[1]),
                                              font=('Times New Roman', 20, 'bold'), text_color="white",
                                              fg_color="#2b2b2b")
        welcomelabel.place(x=1290, y=25)

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

            title11lbl=customtkinter.CTkLabel(master=assignbookingFrame, text="ASSIGN DRIVERS", font=font720)
            title11lbl.place(x=110, y=20)

            pickup_address_lbl = customtkinter.CTkLabel(assignbookingFrame, text="Pick up: ",font=font720)
            pickup_address_lbl.place(x=30, y=100)

            picuptxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            picuptxt.place(x=140, y=100)

            date_lbl = customtkinter.CTkLabel(assignbookingFrame, text="Date: ", font=font720)
            date_lbl.place(x=30, y=150)

            date_txt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            date_txt.place(x=140, y=150)

            pickup_lbl = customtkinter.CTkLabel(assignbookingFrame, text="Time:", font=font720)
            pickup_lbl.place(x=30, y=200)

            def updateTime2(time):
                pickuptxt.delete(0, len(pickuptxt.get()))
                pickuptxt.insert(0, str("{}:{} {}".format(*time)))

            def time720():
                top = customtkinter.CTkToplevel(assignbookingFrame)
                top.title("Taxi Booking System")
                top.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
                top.resizable(0, 0)
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
                ok_btn = customtkinter.CTkButton(master=top, text="Ok", command=lambda: updateTime2(time_picker.time()))
                ok_btn.pack()


            pickuptxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            pickuptxt.place(x=140, y=200)

            time_img = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\time-five-regular-24.png"))
            pic_up_time_btn = customtkinter.CTkButton(assignbookingFrame, image=time_img, text="",fg_color="black", command=time720, font=font720, width=40)
            pic_up_time_btn.place(x=350, y=202)

            dropoff_lbl = customtkinter.CTkLabel(assignbookingFrame, text="Drop Off:", font=font720)
            dropoff_lbl.place(x=30, y=250)

            dropoff_txt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
            dropoff_txt.place(x=140, y=250)

            driveridlabel = customtkinter.CTkLabel(assignbookingFrame, text="Driver id:", font=font720)
            driveridlabel.place(x=30, y=300)


            driveridcombo = customtkinter.CTkEntry(assignbookingFrame,font=font720, width=200)
            driveridcombo.place(x=140, y=300)

            customerid=customtkinter.CTkEntry(assignbookingFrame)
            bookingid = customtkinter.CTkEntry(assignbookingFrame)


            def available_driver_gui():
                drivergui=customtkinter.CTkToplevel()
                drivergui.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
                drivergui.title("Taxi Booking System")
                drivergui.resizable(0, 0)
                frame_width = 400
                frame_height = 300
                screen_width = drivergui.winfo_screenwidth()
                screen_height = drivergui.winfo_screenheight()
                x_cordinate = int((screen_width / 2) - (frame_width / 2))
                y_cordinate = int((screen_height / 2) - (frame_height / 2))
                drivergui.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate+200, y_cordinate))

                availabledrivertable=ttk.Treeview(drivergui)
                availabledrivertable.pack(side=TOP, fill=BOTH, expand=TRUE)
                availabledrivertable['columns']=('id', 'name')
                availabledrivertable.column('#0', width=0, stretch=0)
                availabledrivertable.column('id', width=100, anchor=CENTER)
                availabledrivertable.column('name', width=100, anchor=CENTER)

                availabledrivertable.heading('#0', text='', anchor=CENTER)
                availabledrivertable.heading('id', text='Driver ID', anchor=CENTER)
                availabledrivertable.heading('name', text='Name', anchor=CENTER)

                def get_availabledriver():

                    availabledriver=available_driver()
                    i=0
                    for driver in availabledriver:
                        availabledrivertable.insert(parent='', index='end', values=(driver[0], driver[1]))

                get_availabledriver()

                def select_availabledriver(a):
                    driveridcombo.delete(0, END)
                    selectitem=availabledrivertable.selection()[0]
                    driveridcombo.insert(0, availabledrivertable.item(selectitem)['values'][0])



                availabledrivertable.bind("<<TreeviewSelect>>", select_availabledriver)


                root.mainloop()

            availabledriver_btn = customtkinter.CTkButton(assignbookingFrame,command=available_driver_gui, text="Available Driver", font=font720, width=150)
            availabledriver_btn.place(x=30, y=350)

            updatebookingresultlbl=customtkinter.CTkLabel(assignbookingFrame, text="", font=font720)
            updatebookingresultlbl.place(x=80, y=390)




            assinbookingframe2=customtkinter.CTkFrame(master=root, width=840)
            assinbookingframe2.pack(side=LEFT, fill=BOTH, padx=(0,10), pady=10)

            bookingTable = ttk.Treeview(assinbookingframe2)
            bookingTable['columns'] = ('bookingid', 'pickup', 'date', 'time', 'dropoff', 'status', 'customerid', 'driverid')
            bookingTable.column('#0', width=0, stretch=0)
            bookingTable.column('bookingid', width=50, anchor=CENTER)
            bookingTable.column('pickup', width=220, anchor=CENTER)
            bookingTable.column('date', width=120, anchor=CENTER)
            bookingTable.column('time', width=100, anchor=CENTER)
            bookingTable.column('dropoff', width=200, anchor=CENTER)
            bookingTable.column('status', width=180, anchor=CENTER)
            bookingTable.column('customerid', width=70, anchor=CENTER)
            bookingTable.column('driverid', width=80, anchor=CENTER)

            bookingTable.heading('#0', text='', anchor=CENTER)
            bookingTable.heading('bookingid', text="ID", anchor=CENTER)
            bookingTable.heading('pickup', text="Pickup", anchor=CENTER)
            bookingTable.heading('date', text="Date", anchor=CENTER)
            bookingTable.heading('time', text="Time", anchor=CENTER)
            bookingTable.heading('dropoff', text="Drop Off", anchor=CENTER)
            bookingTable.heading('status', text="Status", anchor=CENTER)
            bookingTable.heading('customerid', text="Cus ID", anchor=CENTER)
            bookingTable.heading('driverid', text="ID", anchor=CENTER)

            def bookingtable():
                Bookresult = select_all()
                i = 0
                for ro in Bookresult:
                    bookingTable.insert(parent='', index='end',
                                        values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
                    i = i + 1

            bookingTable.pack(padx=10, pady=10)


            def getDriverDetail(a):
                picuptxt.delete(0, END)
                date_txt.delete(0, END)
                pickuptxt.delete(0, END)
                dropoff_txt.delete(0, END)
                customerid.delete(0, END)
                bookingid.delete(0, END)

                selectitem2=bookingTable.selection()[0]

                picuptxt.insert(0, bookingTable.item(selectitem2)['values'][1])
                date_txt.insert(0, bookingTable.item(selectitem2)['values'][2])
                pickuptxt.insert(0, bookingTable.item(selectitem2)['values'][3])
                dropoff_txt.insert(0, bookingTable.item(selectitem2)['values'][4])
                customerid.insert(0, bookingTable.item(selectitem2)['values'][6])
                bookingid.insert(0, bookingTable.item(selectitem2)['values'][0])

            bookingTable.bind("<<TreeviewSelect>>",getDriverDetail )

            def update_customer_booking():
                picuptxt.get()
                date_txt.get()
                pickuptxt.get()
                dropoff_txt.get()
                customerid.get()
                driveridcombo.get()
                bookingid.get()

                updatebooking=BookingLibs(pickupaddress=picuptxt.get(),
                date=date_txt.get(),time=pickuptxt.get(), dropoffaddress=dropoff_txt.get(),
                cid=customerid.get(),bookingstatus='Booked', did= driveridcombo.get(), bookingid=bookingid.get())
                updatebookingResult=update_booking(updatebooking)

                driver=Driver_Libs(did=driveridcombo.get(), driverstatus='Booked')
                updateresult=update_DriverStatus(driver)
                if updatebookingResult==True:
                    updatebookingresultlbl.configure(text="Driver is assigned successfully")
                    bookingTable.delete(*bookingTable.get_children())
                    bookingtable()
                    bookingTable2.delete(*bookingTable2.get_children())
                    bookingTable11()


                else:
                    updatebookingresultlbl.configure(text="Error Occurred")

            assign_btn = customtkinter.CTkButton(assignbookingFrame,command=update_customer_booking, text="Assign Driver", font=font720, width=150)
            assign_btn.place(x=190, y=350)

            bookingtable()
            root.mainloop()



        assigndriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame,text="Assign Drivers   ",command=assign_driver, hover_color='black', font=sidemenufont, width=200,image=assigndriver_btn_image, fg_color='#2b2b2b')
        assigndriver_btn.place(x=40, y=200)

        def billing_gui():
            main=customtkinter.CTkToplevel()
            admin_payment.Admin_Payment(main)
            main.mainloop()

        payment_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\paypal-logo-24.png'))
        payment_btn = customtkinter.CTkButton(master=left_frame, text="Payment            ",command=billing_gui, hover_color='black', font=sidemenufont, width=200,image=payment_btn_image, fg_color='#2b2b2b')
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
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="Booking History", hover_color='black',font=sidemenufont, width=200,image=viewcustomer_btn_image, fg_color='#2b2b2b')
        viewcustomer_btn.place(x=40, y=450)

        viewdriver_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\trip-advisor-logo-24.png'))
        viewdriver_btn = customtkinter.CTkButton(master=left_frame, text="Billing History    ", hover_color='black',font=sidemenufont, width=200,image=viewdriver_btn_image, fg_color='#2b2b2b')
        viewdriver_btn.place(x=40, y=500)

        def logout():
            self.main.destroy()
            root=customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        logout_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame,command=logout, text="Logout              ", fg_color='#2b2b2b',hover_color='black',font=sidemenufont, width=200,image=logout_btn_image)
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
        frameCenter = customtkinter.CTkFrame(master=self.main, width=1200, height=650, corner_radius=20)
        frameCenter.place(x=320, y=100)

        parent_tab=customtkinter.CTkTabview(frameCenter, width=1170)
        parent_tab.place(x=15,y=10)

        parent_tab.add('Home')
        parent_tab.add('Search')
        parent_tab.add('Records')

        #+++++++++++++++++++++++++++++++++++Home Tab 1 Frame++++++++++++++++++++++++++++++++++++
        frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame1.place(x=30, y=20)
        result = total_customer()
        tmpResult = result[0]
        frame1_label2 = customtkinter.CTkLabel(master=frame1, text="Total \nCustomers \n\n{}".format(tmpResult[0]), font=labelfont)
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 2 Frame++++++++++++++++++++++++++++++++++++
        frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame2.place(x=310, y=20)
        bookingResult=total_booking()
        bookingresult2=bookingResult[0]
        frame2_label2 = customtkinter.CTkLabel(master=frame2, text="Total \nBookings \n\n{}".format(bookingresult2[0]),font=labelfont)
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 3 Frame++++++++++++++++++++++++++++++++++++
        frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame3.place(x=590, y=20)
        driverResult=total_driver()
        driveresult2=driverResult[0]
        frame3_label2 = customtkinter.CTkLabel(master=frame3, text="Total \nDrivers \n\n{}".format(driveresult2[0]),font=labelfont)
        frame3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 4 Frame++++++++++++++++++++++++++++++++++++
        frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame4.place(x=870, y=20)
        employeesResult=total_employees()
        employeesResult2=employeesResult[0]
        frame4_label2 = customtkinter.CTkLabel(master=frame4, text="Total \nEmployees \n\n{}".format(employeesResult2[0]),
                                               font=labelfont)
        frame4_label2.place(relx=0.5, rely=0.5, anchor=CENTER)




        # +++++++++++++++++++++++++++++++++++Service Tab 1 Frame++++++++++++++++++++++++++++++++++++
        tab2frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        tab2frame1.place(x=30, y=20)
        def search_customers11():
            root=customtkinter.CTkToplevel()
            search_customers.SearchCustomer(root)
            root.mainloop()

        frame1_label1 = customtkinter.CTkButton(master=tab2frame1,text="Search \nCustomer",command=search_customers11,font=labelfont,fg_color='#2b2b2b',)
        frame1_label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Service Tab 2 Frame++++++++++++++++++++++++++++++++++++
        tab2frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        tab2frame2.place(x=310, y=20)
        def search_drivers11():
            root=customtkinter.CTkToplevel()
            search_drivers.SearchDrivers(root)
            root.mainloop()
        frame2_label2 = customtkinter.CTkButton(master=tab2frame2, text="Search \nDrivers",command=search_drivers11, font=labelfont,fg_color='#2b2b2b', )
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Service Tab 3 Frame++++++++++++++++++++++++++++++++++++
        tab2frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Search'), width=250, height=150, corner_radius=20)
        tab2frame3.place(x=590, y=20)
        def search_employees11():
            root=customtkinter.CTkToplevel()
            search_employees.SearchEmployees(root)
            root.mainloop()
        frame3_label3 = customtkinter.CTkButton(master=tab2frame3, text="Search \nEmployees",command=search_employees11, font=labelfont,fg_color='#2b2b2b', )
        frame3_label3.place(relx=0.5, rely=0.5, anchor=CENTER)




        # +++++++++++++++++++++++++++++++++++Report Tab 1 Frame++++++++++++++++++++++++++++++++++++
        tab3frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        tab3frame1.place(x=30, y=20)
        def customer_report720():
            root=customtkinter.CTkToplevel()
            customer_report.CustomerReport(root)
            root.mainloop()
        tab3_label1 = customtkinter.CTkButton(master=tab3frame1, text="Customer \nReports",command=customer_report720, font=labelfont,fg_color='#2b2b2b', )
        tab3_label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 2 Frame++++++++++++++++++++++++++++++++++++
        tab3frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        tab3frame2.place(x=310, y=20)
        def driver_report720():
            root=customtkinter.CTkToplevel()
            driver_report.DriverReport(root)
            root.mainloop()
        tab3_label2 = customtkinter.CTkButton(master=tab3frame2, text="Driver \nReports",command=driver_report720, font=labelfont,fg_color='#2b2b2b', )
        tab3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 3 Frame++++++++++++++++++++++++++++++++++++
        tab3frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        tab3frame3.place(x=590, y=20)
        def booking_report720():
            root=customtkinter.CTkToplevel()
            booking_report.BookingReport(root)
            root.mainloop()
        tab3_label3 = customtkinter.CTkButton(master=tab3frame3, text="Booking \nReports",command=booking_report720, font=labelfont,fg_color='#2b2b2b', )
        tab3_label3.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 4 Frame++++++++++++++++++++++++++++++++++++
        tab4frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Records'), width=250, height=150, corner_radius=20)
        tab4frame4.place(x=870, y=20)
        tab4_label4 = customtkinter.CTkButton(master=tab4frame4, text="Billing \nReports", font=labelfont,
                                              fg_color='#2b2b2b', )
        tab4_label4.place(relx=0.5, rely=0.5, anchor=CENTER)




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

        bookingTable2=ttk.Treeview(frameCenter)
        bookingTable2['columns']=('bookingid', 'pickup', 'date','time','dropoff','status', 'customerid', 'driverid')
        bookingTable2.column('#0', width=0, stretch=0)
        bookingTable2.column('bookingid', width=180, anchor=CENTER)
        bookingTable2.column('pickup', width=240, anchor=CENTER)
        bookingTable2.column('date', width=150, anchor=CENTER)
        bookingTable2.column('time', width=150, anchor=CENTER)
        bookingTable2.column('dropoff', width=220, anchor=CENTER)
        bookingTable2.column('status', width=220, anchor=CENTER)
        bookingTable2.column('customerid', width=150, anchor=CENTER)
        bookingTable2.column('driverid', width=150, anchor=CENTER)

        bookingTable2.heading('#0', text='', anchor=CENTER)
        bookingTable2.heading('bookingid', text="Booking ID", anchor=CENTER)
        bookingTable2.heading('pickup', text="Pickup", anchor=CENTER)
        bookingTable2.heading('date', text="Date", anchor=CENTER)
        bookingTable2.heading('time', text="Time", anchor=CENTER)
        bookingTable2.heading('dropoff', text="Drop Off", anchor=CENTER)
        bookingTable2.heading('status', text="Status", anchor=CENTER)
        bookingTable2.heading('customerid', text="Customer ID", anchor=CENTER)
        bookingTable2.heading('driverid', text="Driver ID", anchor=CENTER)

        def bookingTable11():
            Bookresult = select_all()
            i = 0
            for ro in Bookresult:
                bookingTable2.insert(parent='', index='end',
                                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
                i = i + 1

        bookingTable11()
        bookingTable2.place(x=15, y=360)



if __name__=='__main__':
    main=customtkinter.CTk()
    Admin_Dashboard(main)
    main.mainloop()




