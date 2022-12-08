from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import ImageTk, Image
from dbms.driver_management import insert_record, search_record, delete_record, update_record
from libs.driver_libs import Driver_Libs
from tkinter import messagebox


#++++++++++++++++++++++++++++++++++++++++++++GUI+++++++++++++++++++++++++++++++++++++++++++


class DriverRegistration():

    def __init__(self, driver):
        self.driver=driver
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.driver.title("Driver Registration")
        myWidth=900
        myHeight=500
        screenWidth=self.driver.winfo_screenwidth()
        screenHeight=self.driver.winfo_screenheight()
        xCordinate=int((screenWidth/2)-(myWidth/2))
        yCordinate=int((screenHeight/2)-(myHeight/2))
        #+++++++++++++++++++++++++Center Window in to screen++++++++++++++++++++++++++++++
        self.driver.geometry('{}x{}+{}+{}'.format(myWidth, myHeight, xCordinate+200, yCordinate))
        #+++++++++++++++++++++++++++++++Set Icon in window++++++++++++++++++++++++++++++++++++
        self.driver.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")


        #font
        font720=customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        #All the variables
        self.idtxt=StringVar()
        self.nametxt=StringVar()
        self.mobiletxt=StringVar()
        self.emailtxt=StringVar()
        self.licensetxt=StringVar()
        self.passwordtxt=StringVar()


        #+++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        topFrame=customtkinter.CTkFrame(master=self.driver, height=70)
        topFrame.pack(side=TOP, fill=BOTH, padx=20, pady=(10,20))

        #+++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        titleLabel=customtkinter.CTkLabel(master=topFrame, text="DRIVER MANAGEMENT SYSTEM",font=('Times New Roman', 25, 'bold'))
        titleLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        #++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame=customtkinter.CTkFrame(master=self.driver, width=855, height=380)
        centerFrame.pack(anchor=CENTER)

        def searchdriver():
            driverid=int(idtxt.get())

            searchResult=search_record(driverid)

            if idtxt.get()=='':
                messagebox.showerror("Taxi Booking System", "The user not found")

            else:

                if searchResult == None:
                    messagebox.showerror("Taxi Booking System", "The user not found")

                else:
                    nametxt.delete(0, len(nametxt.get()))
                    nametxt.insert(0, searchResult[1])

                    mobiletxt.delete(0, len(mobiletxt.get()))
                    mobiletxt.insert(0, searchResult[2])

                    emailtxt.delete(0, len(emailtxt.get()))
                    emailtxt.insert(0, searchResult[3])

                    licensetxt.delete(0, len(licensetxt.get()))
                    licensetxt.insert(0, searchResult[4])

                    passwordtxt.delete(0, len(passwordtxt.get()))
                    passwordtxt.insert(0, searchResult[5])




        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        idlbl = customtkinter.CTkLabel(master=centerFrame, text="Search: ", font=font720)
        idlbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        idtxt = customtkinter.CTkEntry(master=centerFrame,textvariable=self.idtxt,  placeholder_text="Enter Driver ID", font=font720,width=200)
        idtxt.place(x=140, y=15)

        search_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\search-alt-2-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=centerFrame, image=search_image, text="Search",
                                           command=searchdriver, font=font720, width=180)
        deletebtn.place(x=350, y=15)

        centerFrame2=customtkinter.CTkFrame(master=centerFrame, height=300, width=540)
        centerFrame2.place(x=20, y=65)

        #++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++
        namelbl=customtkinter.CTkLabel(master=centerFrame2, text="Name: ", font=font720)
        namelbl.place(x=40,y=30)

        #++++++++++++++++++++++++++++++TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        nametxt=customtkinter.CTkEntry(master=centerFrame2,textvariable=self.nametxt,  font=font720, width=250)
        nametxt.place(x=200,y=30)

        #+++++++++++++++++++++++++++++Mobile Label++++++++++++++++++++++++++++
        mobilelbl = customtkinter.CTkLabel(master=centerFrame2, text="Mobile: ", font=font720)
        mobilelbl.place(x=40, y=80)

        # ++++++++++++++++++++++++++++++Mobile TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        mobiletxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.mobiletxt, font=font720, width=250)
        mobiletxt.place(x=200, y=80)

        # +++++++++++++++++++++++++++++Email Label++++++++++++++++++++++++++++
        emaillbl = customtkinter.CTkLabel(master=centerFrame2, text="Email: ", font=font720)
        emaillbl.place(x=40, y=130)

        # ++++++++++++++++++++++++++++++Email TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        emailtxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.emailtxt,   font=font720, width=250)
        emailtxt.place(x=200, y=130)

        # +++++++++++++++++++++++++++++License Label++++++++++++++++++++++++++++
        licenselbl = customtkinter.CTkLabel(master=centerFrame2, text="License no: ", font=font720)
        licenselbl.place(x=40, y=180)

        # ++++++++++++++++++++++++++++++License TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        licensetxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.licensetxt,   font=font720,width=250)
        licensetxt.place(x=200, y=180)

        # +++++++++++++++++++++++++++++Password Label++++++++++++++++++++++++++++
        passwordlbl = customtkinter.CTkLabel(master=centerFrame2, text="Password: ", font=font720)
        passwordlbl.place(x=40, y=230)

        # ++++++++++++++++++++++++++++++Password TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        passwordtxt = customtkinter.CTkEntry(master=centerFrame2,textvariable=self.passwordtxt, font=font720, width=250)
        passwordtxt.place(x=200, y=230)



        innerFrame=customtkinter.CTkFrame(master=centerFrame, width=250, height=340)
        innerFrame.place(x=580, y=20)

        def save_record():

            if nametxt.get()=='' or mobiletxt.get()=='' or emailtxt.get()=='' or licensetxt.get()=='' or passwordtxt.get()=='':
                messagebox.showwarning("Taxi Booking System", "Please fill all the fields")

            else:
                driver = Driver_Libs(name=nametxt.get(), mobile=mobiletxt.get(), email=emailtxt.get(),license=licensetxt.get(), password=passwordtxt.get(), status='Driver',driverstatus='')
                result = insert_record(driver)
                if result == True:
                    msg1 = messagebox.showinfo("Taxi Booking System", "Driver is registered successfully!")
                else:
                    msg2 = messagebox.showerror("Taxi Booking System", "Driver register is unsuccessfull!")






        save_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\check-square-regular-24.png"))
        savebtn=customtkinter.CTkButton(master=innerFrame,command=save_record, image=save_image, text="Save Record", font=font720,width=180, hover_color="black")
        savebtn.place(x=30,y=80)

        def update():
            driver = Driver_Libs(name=nametxt.get(), mobile=mobiletxt.get(), email=emailtxt.get(),
                                 license=licensetxt.get(), password=passwordtxt.get(), did=idtxt.get())
            updateresult=update_record(driver)

            if updateresult==True:
                messagebox.showinfo("Taxi Booking System","The record is updated")

            else:
                messagebox.showerror("Taxi Booking System","Error occurred!")


        update_image=customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png"))
        updatebtn = customtkinter.CTkButton(master=innerFrame,command=update, text="Update Record",image=update_image, font=font720, width=180, hover_color="black")
        updatebtn.place(x=30, y=140)

        def delete():
            id=idtxt.get()
            result=delete_record(id)
            if result==True:
                messagebox.showinfo("Taxi Booking System","The user is deleted successfully!")

            else:
                messagebox.showerror("Taxi Booking System", "Error occurred!")


        delete_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=innerFrame,image=delete_image,command=delete, text="Delete Record", font=font720, width=180, hover_color="black")
        deletebtn.place(x=30, y=200)

        def clear():
            self.idtxt.set('')
            self.nametxt.set('')
            self.emailtxt.set('')
            self.mobiletxt.set('')
            self.licensetxt.set('')
            self.passwordtxt.set('')

        clear_image = customtkinter.CTkImage(light_image=Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        clearbtn = customtkinter.CTkButton(master=innerFrame, image=clear_image, text="Clear Record",
                                         command=clear,   font=font720, width=180, hover_color="black")
        clearbtn.place(x=30, y=260)



if __name__=='__main__':
    driver=customtkinter.CTk()
    DriverRegistration(driver)
    driver.mainloop()
