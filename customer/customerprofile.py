from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from libs import Global

#+++++++++++++++++++++++++++++++++Main Class++++++++++++++++++++++++++++++
class CustomerProfile():
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        # self.main.title("{} Profile".format(Global.currentUser[1]))
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        width = 750
        height = 400
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate, yCordinate - 50))
        self.main.maxsize(950, 400)

        #++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 =customtkinter.CTkFont(family='Times New Roman', size=19, weight='normal')

        #++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++
        centerFrame = customtkinter.CTkFrame(master=self.main, width=710, height=320)
        centerFrame.place(x=20, y=60)

        #++++++++++++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++++
        namelbl = customtkinter.CTkLabel(centerFrame, text="Name: ", font=font720)
        namelbl.place(x=50, y=100)

        #+++++++++++++++++++++++++++++++++++++Global Name Label+++++++++++++++++++++++++++++++++++++
        namelbl1=customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[1]), font=font720)
        namelbl1.place(x=150, y=100)

        #++++++++++++++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        dob = customtkinter.CTkLabel(centerFrame, text="DOB: ", font=font720)
        dob.place(x=50, y=150)

        #+++++++++++++++++++++++++++++++++++++Global DOB Label+++++++++++++++++++++++++++++++++++++++
        # .format(Global.currentUser[2])
        dob1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[2]), font=font720)
        dob1.place(x=150, y=150)

        # +++++++++++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++++
        gender = customtkinter.CTkLabel(centerFrame, text="Gender: ", font=font720)
        gender.place(x=50, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Gender Label+++++++++++++++++++++++++++++++++++++++
        gender1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[3]), font=font720)
        gender1.place(x=150, y=200)

        # +++++++++++++++++++++++++++++++++++++Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile = customtkinter.CTkLabel(centerFrame, text="Mobile: ", font=font720)
        mobile.place(x=50, y=250)

        # +++++++++++++++++++++++++++++++++++++Global Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[4]), font=font720)
        mobile1.place(x=150, y=250)

        # +++++++++++++++++++++++++++++++++++++Email Label+++++++++++++++++++++++++++++++++++++++
        email = customtkinter.CTkLabel(centerFrame, text="Email: ", font=font720)
        email.place(x=410, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Email Label+++++++++++++++++++++++++++++++++++++++
        email1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[5]), font=font720)
        email1.place(x=510, y=100)

        # +++++++++++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++++
        address = customtkinter.CTkLabel(centerFrame, text="Address: ", font=font720)
        address.place(x=410, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Address Label+++++++++++++++++++++++++++++++++++++++
        address1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[6]), font=font720)
        address1.place(x=510, y=150)

        # +++++++++++++++++++++++++++++++++++++Password Label+++++++++++++++++++++++++++++++++++++++
        password = customtkinter.CTkLabel(centerFrame, text="Password: ", font=font720)
        password.place(x=410, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Password Label+++++++++++++++++++++++++++++++++++++++
        password1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[7]), font=font720)
        password1.place(x=510, y=200)

        # +++++++++++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++++
        credit = customtkinter.CTkLabel(centerFrame, text="Credit No: ", font=font720)
        credit.place(x=410, y=250)

        # +++++++++++++++++++++++++++++++++++++Global Credit Label+++++++++++++++++++++++++++++++++++++++
        credit1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentUser[8]), font=font720)
        credit1.place(x=510, y=250)

        # +++++++++++++++++++++++++++++++++++++Image Label+++++++++++++++++++++++++++++++++++++++
        user_image = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label = Label(self.main, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=400, y=20)


if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerProfile(main)
    main.mainloop()