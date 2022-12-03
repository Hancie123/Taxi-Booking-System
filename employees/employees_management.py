from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
from dbms.employees_backend import insert_record, search_employees, update_record, delete_record
from libs.employees_libs import EmployeesLibs


class EmployeesManagement(customtkinter.CTk):
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Employees Management System")
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        width = 1050
        height = 400
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate+200, yCordinate))
        self.main.maxsize(1050, 400)

        # font
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        # All the variables
        self.idtxt = StringVar()
        self.nametxt = StringVar()
        self.gendertxt=StringVar()
        self.mobiletxt = StringVar()
        self.emailtxt = StringVar()
        self.addresstxt=StringVar()
        self.dobtxt = StringVar()

        # +++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        topFrame = customtkinter.CTkFrame(master=self.main, height=70)
        topFrame.pack(side=TOP, fill=BOTH, padx=20, pady=(10, 20))

        # +++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        titleLabel = customtkinter.CTkLabel(master=topFrame, text="EMPLOYEES MANAGEMENT SYSTEM", font=('Times New Roman', 25, 'bold'))
        titleLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame = customtkinter.CTkFrame(master=self.main, width=1000, height=290)
        centerFrame.pack(anchor=CENTER)

        def searchEmployees():

            employeesid=idtxt.get()
            employeesResult=search_employees(employeesid)
            if employeesResult==None:
                messagebox.showwarning("Taxi Booking System", "The Employees ID {} is not found".format(employeesid))

            else:
                nametxt.delete(0, len(nametxt.get()))
                nametxt.insert(0, employeesResult[1])

                dobtxt.delete(0, len(dobtxt.get()))
                dobtxt.insert(0, employeesResult[2])

                gendertxt.delete(0, len(gendertxt.get()))
                gendertxt.insert(0, employeesResult[3])

                mobiletxt.delete(0, len(mobiletxt.get()))
                mobiletxt.insert(0, employeesResult[4])

                emailtxt.delete(0, len(emailtxt.get()))
                emailtxt.insert(0, employeesResult[5])

                addresstxt.delete(0, len(addresstxt.get()))
                addresstxt.insert(0, employeesResult[6])




        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        idlbl = customtkinter.CTkLabel(master=centerFrame, text="Search: ", font=font720)
        idlbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        idtxt = customtkinter.CTkEntry(master=centerFrame,textvariable=self.idtxt, placeholder_text="Enter Driver ID", font=font720, width=200)
        idtxt.place(x=100, y=15)

        search_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\search-alt-2-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=centerFrame, image=search_image, text="Search",command=searchEmployees, font=font720, width=180)
        deletebtn.place(x=320, y=15)


        #++++++++++++++++++++++++Center Frame 2+++++++++++++++++++++++++++++++++++
        centerFrame2 = customtkinter.CTkFrame(master=centerFrame, height=200, width=690)
        centerFrame2.place(x=20, y=65)

        # ++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++
        namelbl = customtkinter.CTkLabel(master=centerFrame2, text="Name: ", font=font720)
        namelbl.place(x=40, y=30)

        # ++++++++++++++++++++++++++++++TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        nametxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.nametxt, font=font720, width=200)
        nametxt.place(x=150, y=30)

        # ++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        doblbl = customtkinter.CTkLabel(master=centerFrame2, text="DOB: ", font=font720)
        doblbl.place(x=380, y=30)

        # ++++++++++++++++++++++++++++++DOB TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        dobtxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.dobtxt, font=font720, width=200)
        dobtxt.place(x=470, y=30)

        # ++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++
        genderlbl = customtkinter.CTkLabel(master=centerFrame2, text="Gender: ", font=font720)
        genderlbl.place(x=380, y=80)

        # ++++++++++++++++++++++++++++++Gender TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        gendertxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.gendertxt,  font=font720, width=200)
        gendertxt.place(x=470, y=80)

        # ++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++
        addresslbl = customtkinter.CTkLabel(master=centerFrame2, text="Address: ", font=font720)
        addresslbl.place(x=380, y=130)

        # ++++++++++++++++++++++++++++++Address TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        addresstxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.addresstxt, font=font720, width=200)
        addresstxt.place(x=470, y=130)

        # +++++++++++++++++++++++++++++Mobile Label++++++++++++++++++++++++++++
        mobilelbl = customtkinter.CTkLabel(master=centerFrame2, text="Mobile: ", font=font720)
        mobilelbl.place(x=40, y=80)

        # ++++++++++++++++++++++++++++++Mobile TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        mobiletxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.mobiletxt, font=font720, width=200)
        mobiletxt.place(x=150, y=80)

        # +++++++++++++++++++++++++++++Email Label++++++++++++++++++++++++++++
        emaillbl = customtkinter.CTkLabel(master=centerFrame2, text="Email: ", font=font720)
        emaillbl.place(x=40, y=130)

        # ++++++++++++++++++++++++++++++Email TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        emailtxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.emailtxt, font=font720, width=200)
        emailtxt.place(x=150, y=130)


        sideFrame = customtkinter.CTkFrame(master=centerFrame, width=250, height=250)
        sideFrame.place(x=730, y=20)

        def save_employees_info():

            if (nametxt.get() == '') or (dobtxt.get() == '') or (gendertxt.get() == '') or (mobiletxt.get() == '') \
                    or (emailtxt.get() == '') or (addresstxt.get() == ''):
                warning = messagebox.showwarning("Taxi Booking System", "Please enter all the field!")

            else:
                customer_info = EmployeesLibs('', nametxt.get(), dobtxt.get(), gendertxt.get(),
                                              mobiletxt.get(), emailtxt.get(), addresstxt.get())
                result = insert_record(customer_info)
                if result == True:
                    promt = messagebox.showinfo('Taxi Booking System', "Employees detail is registered successfully")
                else:
                    promt1 = messagebox.showerror("Error!", "Registration of employees info is unsuccessful!")



        save_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\check-square-regular-24.png"))
        savebtn = customtkinter.CTkButton(master=sideFrame, command=save_employees_info, image=save_image, text="Save Record",font=font720, width=180, hover_color="black")
        savebtn.place(x=35, y=50)

        def update():
            employees_info = EmployeesLibs(emid=idtxt.get(), name=nametxt.get(), dob=dobtxt.get(), gender=gendertxt.get(),
                                          mobile=mobiletxt.get(), email=emailtxt.get(), address=addresstxt.get())
            updateResult=update_record(employees_info)
            if updateResult==True:
                messagebox.showinfo("Taxi Booking System","The record is updated")

            else:
                messagebox.showwarning("Taxi Booking System","The record is not updated")



        update_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png"))
        updatebtn = customtkinter.CTkButton(master=sideFrame, command=update, text="Update Record", image=update_image,font=font720, width=180, hover_color="black")
        updatebtn.place(x=35, y=100)

        def delete():

            employeesid=idtxt.get()
            deleteResult=delete_record(employeesid)
            if deleteResult==True:
                messagebox.showinfo("Taxi Booking System","The employees ID {} is deleted successfully".format(employeesid))

            else:
                messagebox.showerror("Taxi Booking System","Error occurred!")



        delete_image = customtkinter.CTkImage(light_image=Image.open(
            "E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=sideFrame, image=delete_image, command=delete, text="Delete Record",
                                            font=font720, width=180, hover_color="black")
        deletebtn.place(x=35, y=150)

        def clear():
            self.idtxt.set('')
            self.nametxt.set('')
            self.emailtxt.set('')
            self.mobiletxt.set('')
            self.addresstxt.set('')
            self.dobtxt.set('')
            self.gendertxt.set('')

        clear_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        clearbtn = customtkinter.CTkButton(master=sideFrame, image=clear_image, text="Clear Record",command=clear, font=font720, width=180, hover_color="black")
        clearbtn.place(x=35, y=200)


if __name__=='__main__':
    main=customtkinter.CTk()
    EmployeesManagement(main)
    main.mainloop()
