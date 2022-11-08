from tkinter import *
import customtkinter
from tkcalendar import *
from PIL import ImageTk, Image
from datetime import date
from GUI import Login


class Register(customtkinter.CTk):
    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.root.title("Customer Register")
        self.root.screen_width = root.winfo_screenwidth()
        self.root.screen_height = root.winfo_screenheight()
        self.root.state('zoomed')
        self.root.minsize(self.root.screen_width, self.root.screen_height)
        self.root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        def signin():
            self.root.destroy()
            root=customtkinter.CTk()
            obj1=Login.Login(root)
            root.mainloop()

        font = ('Tahoma', 18, 'bold')
        font1 = ('Tahoma', 18, 'normal')

        North_Frame = customtkinter.CTkFrame(master=root, height=100, corner_radius=0)
        North_Frame.pack(side=TOP, fill=BOTH)

        title_lbl = customtkinter.CTkLabel(master=North_Frame, text="CUSTOMER REGISTRATION FORM",
                                           text_font=('Cambria', 26, 'bold'))
        title_lbl.place(x=500, y=25)

        back_image = Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\\back.png')
        photo = ImageTk.PhotoImage(back_image)
        back_image_label = Label(North_Frame, image=photo, bg="#2a2d2e")
        back_image_label.image = photo
        back_image_label.place(x=20, y=25)

        Right_frame = customtkinter.CTkFrame(master=root)
        Right_frame.pack(side=LEFT, fill=BOTH)

        canva = Canvas(Right_frame, width=900, height=900, bd=0, highlightthickness=0)
        canva.pack()

        Cover_Image = Image.open(
            'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Taxi.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(Right_frame, image=photo1, bg="#212325")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=0, y=0)

        name_lbl = Label(root, text="Name: ",bg="#212325", fg="white",font=font)
        name_lbl.place(x=630, y=200)

        name_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                          width=250)
        name_txt.place(x=650, y=160)

        dob_lbl = Label(root, text="DOB: ",bg="#212325", fg="white", font=font)
        dob_lbl.place(x=630, y=270)

        dt = date.today()
        dob_txt = DateEntry(root, font=font1, selectmode='day', width=17, mindate=dt)

        dob_txt.place(x=820, y=270)

        gender_lbl = Label(root, text="Gender: ",bg="#212325", fg="white", font=font)
        gender_lbl.place(x=1350, y=200)

        gender_txt = customtkinter.CTkOptionMenu(master=root, fg_color='white', text_color='black',
                                                 values=['Male', 'Female', 'Others'], text_font=font1, width=250)
        gender_txt.set('Male')
        gender_txt.place(x=1240, y=160)

        mobile_lbl = Label(root, text="Mobile: ",bg="#212325", fg="white", font=font)
        mobile_lbl.place(x=1350, y=270)

        mobile_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                            width=250)
        mobile_txt.place(x=1240, y=210)

        address_lbl = Label(root, text="Address: ",bg="#212325", fg="white", font=font)
        address_lbl.place(x=630, y=340)

        address_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black',
                                             text_font=font1,
                                             width=250)
        address_txt.place(x=650, y=270)

        email_lbl = Label(root, text="Email: ", bg="#212325", fg="white", font=font)
        email_lbl.place(x=1350, y=340)

        email_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                           width=250)
        email_txt.place(x=1240, y=265)

        password_lbl = Label(root, text="Password: ", bg="#212325", fg="white",font=font)
        password_lbl.place(x=630, y=410)

        password_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black',
                                              text_font=font1, width=250)
        password_txt.place(x=650, y=325)

        credit_lbl = Label(root, text="Credit No: ",bg="#212325", fg="white", font=font)
        credit_lbl.place(x=1350, y=410)

        credit_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                            width=250)
        credit_txt.place(x=1240, y=320)

        register_btn_image = ImageTk.PhotoImage(
            Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit.png"))
        register_btn = customtkinter.CTkButton(master=root, text="Register", image=register_btn_image,
                                               hover_color='black', text_font=('Tahoma', 20, 'bold'))
        register_btn.place(x=1000, y=530)

        back_lbl = customtkinter.CTkLabel(master=root, text="Already have an account",
                                          text_font=('Tahoma', 14, 'normal'),
                                          text_color='white')
        back_lbl.place(x=950, y=590)

        back_btn = customtkinter.CTkButton(master=root, text="SIGN IN", width=100, text_font=('Tahoma', 14, 'bold'),
                                           hover_color='black', command=signin)
        back_btn.place(x=1170, y=590)










