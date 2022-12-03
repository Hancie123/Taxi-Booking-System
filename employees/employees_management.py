from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter

from dbms.customer_management import insert_record, search_customer, update_record, delete_record
from libs.customer_libs import Customer_Libs


class CustomerManagement(customtkinter.CTk):
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Customer Management System")
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        width = 1050
        height = 450
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate, yCordinate - 50))
        self.main.maxsize(1050, 450)

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
        self.passwordtxt = StringVar()
        self.credittxt=StringVar()

        # +++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        topFrame = customtkinter.CTkFrame(master=self.main, height=70)
        topFrame.pack(side=TOP, fill=BOTH, padx=20, pady=(10, 20))

        # +++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        titleLabel = customtkinter.CTkLabel(master=topFrame, text="CUSTOMER MANAGEMENT SYSTEM", font=('Times New Roman', 25, 'bold'))
        titleLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame = customtkinter.CTkFrame(master=self.main, width=1000, height=340)
        centerFrame.pack(anchor=CENTER)

        def searchCustomer():

            customerid=idtxt.get()
            customerResult=search_customer(customerid)
            if customerResult==None:
                messagebox.showwarning("Taxi Booking System", "The Customer ID {} is not found".format(customerid))

            else:
                nametxt.delete(0, len(nametxt.get()))
                nametxt.insert(0, customerResult[1])

                dobtxt.delete(0, len(dobtxt.get()))
                dobtxt.insert(0, customerResult[2])

                gendertxt.delete(0, len(gendertxt.get()))
                gendertxt.insert(0, customerResult[3])

                mobiletxt.delete(0, len(mobiletxt.get()))
                mobiletxt.insert(0, customerResult[4])

                emailtxt.delete(0, len(emailtxt.get()))
                emailtxt.insert(0, customerResult[5])

                addresstxt.delete(0, len(addresstxt.get()))
                addresstxt.insert(0, customerResult[6])

                passwordtxt.delete(0, len(passwordtxt.get()))
                passwordtxt.insert(0, customerResult[7])

                credittxt.delete(0, len(credittxt.get()))
                credittxt.insert(0, customerResult[8])


        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        idlbl = customtkinter.CTkLabel(master=centerFrame, text="Search: ", font=font720)
        idlbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        idtxt = customtkinter.CTkEntry(master=centerFrame,textvariable=self.idtxt, placeholder_text="Enter Driver ID", font=font720, width=200)
        idtxt.place(x=100, y=15)

        search_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\search-alt-2-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=centerFrame, image=search_image, text="Search",command=searchCustomer, font=font720, width=180)
        deletebtn.place(x=320, y=15)


        #++++++++++++++++++++++++Center Frame 2+++++++++++++++++++++++++++++++++++
        centerFrame2 = customtkinter.CTkFrame(master=centerFrame, height=255, width=690)
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

        # ++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++
        creditlbl = customtkinter.CTkLabel(master=centerFrame2, text="Credit: ", font=font720)
        creditlbl.place(x=380, y=180)

        # ++++++++++++++++++++++++++++++Credit TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        credittxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.credittxt, font=font720, width=200)
        credittxt.place(x=470, y=180)

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

        # +++++++++++++++++++++++++++++Password Label++++++++++++++++++++++++++++
        passwordlbl = customtkinter.CTkLabel(master=centerFrame2, text="Password: ", font=font720)
        passwordlbl.place(x=40, y=180)

        # ++++++++++++++++++++++++++++++Password TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        passwordtxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.passwordtxt,  font=font720,width=200)
        passwordtxt.place(x=150, y=180)


        sideFrame = customtkinter.CTkFrame(master=centerFrame, width=250, height=300)
        sideFrame.place(x=730, y=20)

        def save_customer_info():

            if (nametxt.get() == '') or (dobtxt.get() == '') or (gendertxt.get() == '') or (mobiletxt.get() == '') \
                    or (emailtxt.get() == '') or (addresstxt.get() == '') or (passwordtxt.get() == '') or (
                    credittxt.get() == 0):
                warning = messagebox.showwarning("Taxi Booking System", "Please enter all the field!")

            else:
                customer_info = Customer_Libs('', nametxt.get(), dobtxt.get(), gendertxt.get(),
                                              mobiletxt.get(), emailtxt.get(), addresstxt.get(),
                                              passwordtxt.get(), credittxt.get(), status="Customer")
                result = insert_record(customer_info)
                if result == True:
                    promt = messagebox.showinfo('Taxi Booking System', "Customer is registered successfully")
                else:
                    promt1 = messagebox.showerror("Error!", "Registration of customer info is unsuccessful!")



        save_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\check-square-regular-24.png"))
        savebtn = customtkinter.CTkButton(master=sideFrame, command=save_customer_info, image=save_image, text="Save Record",font=font720, width=180, hover_color="black")
        savebtn.place(x=35, y=50)

        def update():
            customer_info = Customer_Libs(cid=idtxt.get(), name=nametxt.get(), dob=dobtxt.get(), gender=gendertxt.get(),
                                          mobile=mobiletxt.get(), email=emailtxt.get(), address=addresstxt.get(),
                                          password=passwordtxt.get(), credit=credittxt.get(), status="Customer")
            updateResult=update_record(customer_info)
            if updateResult==True:
                messagebox.showinfo("Taxi Booking System","The record is updated")

            else:
                messagebox.showwarning("Taxi Booking System","The record is not updated")



        update_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png"))
        updatebtn = customtkinter.CTkButton(master=sideFrame, command=update, text="Update Record", image=update_image,font=font720, width=180, hover_color="black")
        updatebtn.place(x=35, y=100)

        def delete():

            customerid=idtxt.get()
            deleteResult=delete_record(customerid)
            if deleteResult==True:
                messagebox.showinfo("Taxi Booking System","The customer ID {} is deleted successfully".format(customerid))

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
            self.passwordtxt.set('')
            self.dobtxt.set('')
            self.gendertxt.set('')
            self.credittxt.set('')

        clear_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        clearbtn = customtkinter.CTkButton(master=sideFrame, image=clear_image, text="Clear Record",command=clear, font=font720, width=180, hover_color="black")
        clearbtn.place(x=35, y=200)


if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerManagement(main)
    main.mainloop()
