from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from libs import Global


class CustomerProfile():
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("{} Profile".format(Global.currentUser[1]))
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        width = 700
        height = 400
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate, yCordinate - 50))
        self.main.maxsize(800, 400)

        font720 = ('Times New Roman', 14, 'normal')


        centerFrame = customtkinter.CTkFrame(master=self.main, width=660, height=320)
        centerFrame.place(x=20, y=60)

        namelbl = Label(centerFrame, text="Name: ", font=font720, bg="#2a2d2e", fg="white")
        namelbl.place(x=50, y=150)

        namelbl1=Label(centerFrame, text="{}".format(Global.currentUser[1]), font=font720, bg="#2a2d2e", fg="white")
        namelbl1.place(x=150, y=150)

        dob = Label(centerFrame, text="DOB: ", font=font720, bg="#2a2d2e", fg="white")
        dob.place(x=50, y=200)

        dob1 = Label(centerFrame, text="{}".format(Global.currentUser[2]), font=font720, bg="#2a2d2e", fg="white")
        dob1.place(x=150, y=200)

        gender = Label(centerFrame, text="Gender: ", font=font720, bg="#2a2d2e", fg="white")
        gender.place(x=50, y=250)

        gender1 = Label(centerFrame, text="{}".format(Global.currentUser[3]), font=font720, bg="#2a2d2e", fg="white")
        gender1.place(x=150, y=250)

        mobile = Label(centerFrame, text="Mobile: ", font=font720, bg="#2a2d2e", fg="white")
        mobile.place(x=50, y=300)

        mobile1 = Label(centerFrame, text="{}".format(Global.currentUser[4]), font=font720, bg="#2a2d2e", fg="white")
        mobile1.place(x=150, y=300)

        email = Label(centerFrame, text="Email: ", font=font720, bg="#2a2d2e", fg="white")
        email.place(x=450, y=150)

        email1 = Label(centerFrame, text="{}".format(Global.currentUser[5]), font=font720, bg="#2a2d2e", fg="white")
        email1.place(x=550, y=150)

        address = Label(centerFrame, text="Address: ", font=font720, bg="#2a2d2e", fg="white")
        address.place(x=440, y=200)

        address1 = Label(centerFrame, text="{}".format(Global.currentUser[6]), font=font720, bg="#2a2d2e", fg="white")
        address1.place(x=550, y=200)

        password = Label(centerFrame, text="Password: ", font=font720, bg="#2a2d2e", fg="white")
        password.place(x=440, y=250)

        password1 = Label(centerFrame, text="{}".format(Global.currentUser[7]), font=font720, bg="#2a2d2e", fg="white")
        password1.place(x=550, y=250)

        credit = Label(centerFrame, text="Credit No: ", font=font720, bg="#2a2d2e", fg="white")
        credit.place(x=440, y=300)

        credit1 = Label(centerFrame, text="{}".format(Global.currentUser[8]), font=font720, bg="#2a2d2e", fg="white")
        credit1.place(x=550, y=300)



        user_image = ImageTk.PhotoImage(Image.open(
            "E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label = Label(self.main, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=350, y=20)


if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerProfile(main)
    main.mainloop()