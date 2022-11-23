from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import ImageTk, Image
from dbms.driver_management import insert_record
from libs.driver_libs import Driver_Libs
from tkinter import messagebox

#++++++++++++++++++++++++++++++++++++++++++++GUI+++++++++++++++++++++++++++++++++++++++++++


class DriverRegistration():

    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Driver Registration")
        myWidth=900
        myHeight=500
        screenWidth=self.main.winfo_screenwidth()
        screenHeight=self.main.winfo_screenheight()
        xCordinate=int((screenWidth/2)-(myWidth/2))
        yCordinate=int((screenHeight/2)-(myHeight/2))
        #+++++++++++++++++++++++++Center Window in to screen++++++++++++++++++++++++++++++
        self.main.geometry('{}x{}+{}+{}'.format(myWidth, myHeight, xCordinate-30, yCordinate-70))
        #+++++++++++++++++++++++++++++++Set Icon in window++++++++++++++++++++++++++++++++++++
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        self.main.resizable(0,0)

        #font
        font720=('',16,'normal')

        #+++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        topFrame=customtkinter.CTkFrame(master=self.main, height=70)
        topFrame.pack(side=TOP, fill=BOTH, padx=20, pady=(10,20))

        #+++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        titleLabel=customtkinter.CTkLabel(master=topFrame, text="Driver Registration Form",text_font=('',20,'bold'))
        titleLabel.place(x=300,y=20)

        #++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame=customtkinter.CTkFrame(master=self.main, width=855, height=380)
        centerFrame.pack(anchor=CENTER)

        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        idlbl = customtkinter.CTkLabel(master=centerFrame, text="Search: ", text_font=font720)
        idlbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        idtxt = customtkinter.CTkEntry(master=centerFrame, placeholder_text="Enter Driver ID", text_font=font720,width=200)
        idtxt.place(x=140, y=15)

        search_image = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\search-alt-2-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=centerFrame, image=search_image, text="Search",
                                            text_font=font720, width=180)
        deletebtn.place(x=350, y=15)

        centerFrame2=customtkinter.CTkFrame(master=centerFrame, height=300, width=540)
        centerFrame2.place(x=20, y=65)

        #++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++
        namelbl=customtkinter.CTkLabel(master=centerFrame2, text="Name: ", text_font=font720)
        namelbl.place(x=40,y=30)

        #++++++++++++++++++++++++++++++TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        nametxt=customtkinter.CTkEntry(master=centerFrame2, text_font=font720, width=250)
        nametxt.place(x=200,y=30)

        #+++++++++++++++++++++++++++++Mobile Label++++++++++++++++++++++++++++
        mobilelbl = customtkinter.CTkLabel(master=centerFrame2, text="Mobile: ", text_font=font720)
        mobilelbl.place(x=40, y=80)

        # ++++++++++++++++++++++++++++++Mobile TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        mobiletxt = customtkinter.CTkEntry(master=centerFrame2, text_font=font720, width=250)
        mobiletxt.place(x=200, y=80)

        # +++++++++++++++++++++++++++++Email Label++++++++++++++++++++++++++++
        emaillbl = customtkinter.CTkLabel(master=centerFrame2, text="Email: ", text_font=font720)
        emaillbl.place(x=40, y=130)

        # ++++++++++++++++++++++++++++++Email TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        emailtxt = customtkinter.CTkEntry(master=centerFrame2,  text_font=font720, width=250)
        emailtxt.place(x=200, y=130)

        # +++++++++++++++++++++++++++++License Label++++++++++++++++++++++++++++
        licenselbl = customtkinter.CTkLabel(master=centerFrame2, text="License no: ", text_font=font720)
        licenselbl.place(x=40, y=180)

        # ++++++++++++++++++++++++++++++License TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        licensetxt = customtkinter.CTkEntry(master=centerFrame2,  text_font=font720,width=250)
        licensetxt.place(x=200, y=180)

        # +++++++++++++++++++++++++++++Password Label++++++++++++++++++++++++++++
        passwordlbl = customtkinter.CTkLabel(master=centerFrame2, text="Password: ", text_font=font720)
        passwordlbl.place(x=40, y=230)

        # ++++++++++++++++++++++++++++++Password TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        passwordtxt = customtkinter.CTkEntry(master=centerFrame2, text_font=font720, width=250)
        passwordtxt.place(x=200, y=230)



        innerFrame=customtkinter.CTkFrame(master=centerFrame, width=250, height=340)
        innerFrame.place(x=580, y=20)

        def save_record():
            driver=Driver_Libs(name=nametxt.get(), mobile=mobiletxt.get(), email=emailtxt.get(),license= licensetxt.get(), password=passwordtxt.get(), status='Driver')
            result=insert_record(driver)
            if result==True:
                msg1=messagebox.showinfo("Taxi Booking System","Driver is registered successfully!")
            else:
                msg2=messagebox.showerror("Taxi Booking System","Driver register is unsuccessfull!")

        save_image = ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\check-square-regular-24.png"))
        savebtn=customtkinter.CTkButton(master=innerFrame,command=save_record, image=save_image, text="Save Record", text_font=font720,width=180, hover_color="black")
        savebtn.place(x=35,y=80)

        update_image=ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png"))
        updatebtn = customtkinter.CTkButton(master=innerFrame, text="Update Record",image=update_image, text_font=font720, width=180, hover_color="black")
        updatebtn.place(x=25, y=140)

        delete_image = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-x-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=innerFrame,image=delete_image, text="Delete Record", text_font=font720, width=180)
        deletebtn.place(x=30, y=200)



if __name__=='__main__':
    main=customtkinter.CTk()
    DriverRegistration(main)
    main.mainloop()
