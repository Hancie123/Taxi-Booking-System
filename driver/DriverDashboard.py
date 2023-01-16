from tkinter import *
import customtkinter
import pandas
from PIL import ImageTk, Image
from matplotlib import axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from time import strftime
from tkinter import ttk, messagebox

from tktimepicker import AnalogThemes, AnalogPicker, constants

from customer import login
from dbms.booking_backend import total_booking, select_all, driver_update_booking
from dbms.customer_backend import total_customer
from dbms.driver_backend import driver_riding_total, driver_total_booked, driver_ridecompleted, driver_ridecancelled
from dbms.driver_management import update_DriverStatus, driver_select_all, total_driver, driver_selectallbooking, \
    driver_password_change
from dbms.employees_backend import total_employees
from driver import drivertriphistory, driverprofile
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

        #+++++++++++++++++++++++++++++++++++Welcome Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        welcomelabel = customtkinter.CTkLabel(master=self.main, text="Welcome {}".format(Global.currentDriver[1]),font=('Times New Roman', 20, 'bold'), text_color="white", fg_color="#2b2b2b")
        welcomelabel.place(x=1290, y=25)

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
                    driver_ridecancelled(driverid.get())
                    driver_ridecompleted(driverid.get())
                    driver_total_booked(driverid.get())
                    driver_riding_total(driverid.get())
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

        def trip_history_gui():
            root=customtkinter.CTkToplevel()
            drivertriphistory.DriverHistory(root)
            root.mainloop()

        trip_image = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-regular-24.png'))
        trip_btn = customtkinter.CTkButton(master=leftFrame, text="Trips History        ", command=trip_history_gui,hover_color='black', font=sidemenufont, width=200,image=trip_image, fg_color='#2b2b2b')
        trip_btn.place(x=40, y=300)

        def myprofile():
            root=customtkinter.CTkToplevel()
            driverprofile.DriverProfile(root)
            root.mainloop()

        profile_image = customtkinter.CTkImage(light_image=Image.open('E:\\College Assignments\\Second Semester\Python\\Taxi Booking System\\Images\\user-account-solid-24.png'))
        profile_btn = customtkinter.CTkButton(master=leftFrame, text="My Profile          ", command=myprofile,hover_color='black', font=sidemenufont, width=200, image=profile_image,fg_color='#2b2b2b')
        profile_btn.place(x=40, y=350)

        def change_password_gui():
            password=customtkinter.CTkToplevel()
            password.title("Taxi Booking System | Change {} Password".format(Global.currentDriver[1]))
            password.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
            frame_width = 530
            frame_height = 400
            password.resizable(0, 0)
            screen_width = password.winfo_screenwidth()
            screen_height = password.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            password.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate + 70, y_cordinate - 70))


            frame = customtkinter.CTkFrame(password)
            frame.pack(fill=BOTH, expand=TRUE)

            font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

            img = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-72.png"))
            image_label = Label(password, image=img, bg="#2b2b2b")
            image_label.image = img
            image_label.place(x=150, y=40)

            title_lbl = customtkinter.CTkLabel(master=password,text="Changing password for\n{}".format(Global.currentDriver[1]),font=font720, bg_color="#2b2b2b")
            title_lbl.place(x=200, y=40)

            currentpw_lbl = customtkinter.CTkLabel(master=password, text="New Password: ", font=font720,
                                                   bg_color="#2b2b2b")
            currentpw_lbl.place(x=60, y=150)

            currentpw_txt = customtkinter.CTkEntry(master=password, font=font720, show='*', width=200)
            currentpw_txt.place(x=240, y=150)

            confirmpw_lbl = customtkinter.CTkLabel(master=password, text="Confirm Password: ", font=font720,
                                                   bg_color="#2b2b2b")
            confirmpw_lbl.place(x=60, y=220)

            conformpw_txt = customtkinter.CTkEntry(master=password, show='*', font=font720, width=200)
            conformpw_txt.place(x=240, y=220)

            def show_password():
                if i.get() == 1:
                    conformpw_txt.configure(show='')
                    currentpw_txt.configure(show='')
                else:
                    conformpw_txt.configure(show='*')
                    currentpw_txt.configure(show='*')

            i = customtkinter.IntVar()

            password_show = customtkinter.CTkCheckBox(password, text="Show password", variable=i,command=show_password, bg_color="#2b2b2b")
            password_show.place(x=240, y=260)

            idtxt = Entry(password)
            idtxt.insert(0, "{}".format(Global.currentDriver[0]))

            def change_password():
                id = idtxt.get()
                password1 = currentpw_txt.get()
                newpassword = conformpw_txt.get()

                if password1 == newpassword:
                    password720 = Driver_Libs(did=id, password=newpassword)
                    changepasswordresult = driver_password_change(password720)

                    if changepasswordresult == True:
                        messagebox.showinfo("Taxi Booking System", "The password is changed successfully!")
                        self.main.destroy()
                        root=customtkinter.CTk()
                        login.Login(root)
                        root.mainloop()
                    else:
                        messagebox.showerror("Taxi Booking System", "Error occurred!")

                else:
                    messagebox.showerror("Taxi Booking System", "The password does not match. Please try again!")
                    password.destroy()

            confirm_btn = customtkinter.CTkButton(master=password,command=change_password,  text="Change Password!",font=font720)
            confirm_btn.place(x=230, y=310)


        changepasswordimage = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\key-solid-24.png'))
        passwordchangebtn = customtkinter.CTkButton(master=leftFrame, text="Change Password",command=change_password_gui, hover_color='black',font=sidemenufont, width=200,image=changepasswordimage, fg_color='#2b2b2b')
        passwordchangebtn.place(x=40, y=400)

        def logout():
            self.main.destroy()
            root=customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        logout_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=leftFrame,command=logout, text="Logout               ", fg_color='#2b2b2b',hover_color='black',font=sidemenufont, width=200,image=logout_btn_image)
        logout_btn.place(x=40, y=450)

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
                style1.configure("Treeview",
                                 background="#dbdbdb",
                                 fieldbackground="#dbdbdb",
                                 foreground="black")
                welcomelabel.configure(fg_color="#dbdbdb")
                welcomelabel.configure(text_color="#2b2b2b")
                welcomelbl.configure(fg_color="#dbdbdb")
            if choice=='dark':
                Cover_Image_label['bg'] = "#2b2b2b"
                toggleButton['bg'] = "#2b2b2b"
                welcomelabel.configure(fg_color="#2b2b2b")
                welcomelabel.configure(text_color="white")
                style1.configure("Treeview",
                                 background="#2b2b2b",
                                 fieldbackground="#2b2b2b",
                                 foreground="white")
                welcomelbl.configure(fg_color="#2b2b2b")



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

        # +++++++++++++++++++++++++++++++++++Home Tab 1 Frame++++++++++++++++++++++++++++++++++++
        frame1 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame1.place(x=30, y=20)
        driveridd=driverid.get()
        result = driver_riding_total(driveridd)
        tmpResult = result[0]
        frame1_label2 = customtkinter.CTkLabel(master=frame1, text="Total \nRiding \n\n{}".format(tmpResult[0]),
                                               font=labelfont)
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 2 Frame++++++++++++++++++++++++++++++++++++
        frame2 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame2.place(x=310, y=20)
        bookingResult = driver_total_booked(driverid.get())
        bookingresult2 = bookingResult[0]
        frame2_label2 = customtkinter.CTkLabel(master=frame2, text="Total \nBooked \n\n{}".format(bookingresult2[0]),
                                               font=labelfont)
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 3 Frame++++++++++++++++++++++++++++++++++++
        frame3 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame3.place(x=590, y=20)
        driverResult = driver_ridecompleted(driverid.get())
        driveresult2 = driverResult[0]
        frame3_label2 = customtkinter.CTkLabel(master=frame3, text="Rides \nCompleted \n\n{}".format(driveresult2[0]),
                                               font=labelfont)
        frame3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 4 Frame++++++++++++++++++++++++++++++++++++
        frame4 = customtkinter.CTkFrame(master=parent_tab.tab('Home'), width=250, height=150, corner_radius=20)
        frame4.place(x=870, y=20)
        employeesResult = driver_ridecancelled(driverid.get())
        employeesResult2 = employeesResult[0]
        frame4_label2 = customtkinter.CTkLabel(master=frame4,
                                               text="Ride \nCancelled \n\n{}".format(employeesResult2[0]),
                                               font=labelfont)
        frame4_label2.place(relx=0.5, rely=0.5, anchor=CENTER)





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
