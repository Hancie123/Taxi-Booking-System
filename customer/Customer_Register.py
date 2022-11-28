from libs.customer_libs import Customer_Libs
from dbms.customer_management import insert_record
from tkinter import *
import customtkinter
from tkcalendar import *
from PIL import ImageTk, Image
from datetime import date
from customer import login
from tkinter import messagebox, ttk


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

        # ===========================All Variables===========
        self.name_txt = StringVar()
        self.mobile_txt = StringVar()
        self.gender_txt=StringVar()
        self.email_txt = StringVar()
        self.address_txt = StringVar()
        self.password_txt = StringVar()
        self.credit_txt = StringVar()

        def signin():
            self.root.destroy()
            root=customtkinter.CTk()
            obj1=login.Login(root)
            root.mainloop()



        font = ('Bodoni',15,'bold')
        font1 = ('Bodoni',16,'normal')

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
        name_lbl.place(x=630, y=240)

        name_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white',  text_color='black', text_font=font1,
                                          width=250)
        name_txt.configure(textvariable=self.name_txt)
        name_txt.place(x=650, y=200)

        dob_lbl = Label(root, text="DOB: ",bg="#212325", fg="white", font=font)
        dob_lbl.place(x=630, y=310)

        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='black',
                        arrowcolor='red')
        dob_txt = DateEntry(root, font=font1, selectmode='day',style='my.DateEntry', background="green", bordercolor="red",
                                 selectbackground="green", width=17,  date_pattern='yyyy-mm-dd')

        dob_txt.place(x=820, y=320)

        gender_lbl = Label(root, text="Gender: ",bg="#212325", fg="white", font=font)
        gender_lbl.place(x=1350, y=240)

        gender_txt = customtkinter.CTkOptionMenu(master=root, fg_color='white',variable=self.gender_txt, text_color='black',
                                                 values=['Male', 'Female', 'Others'], text_font=font1, width=250)
        gender_txt.set('Male')
        gender_txt.place(x=1240, y=200)

        mobile_lbl = Label(root, text="Mobile: ",bg="#212325", fg="white", font=font)
        mobile_lbl.place(x=1350, y=310)

        mobile_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                            width=250)
        mobile_txt.configure(textvariable=self.mobile_txt)
        mobile_txt.place(x=1240, y=250)

        address_lbl = Label(root, text="Address: ",bg="#212325", fg="white", font=font)
        address_lbl.place(x=630, y=385)

        address_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black',
                                             text_font=font1, width=250)
        address_txt.configure(textvariable=self.address_txt)
        address_txt.place(x=650, y=310)

        email_lbl = Label(root, text="Email: ", bg="#212325", fg="white", font=font)
        email_lbl.place(x=1350, y=380)

        email_txt = customtkinter.CTkEntry(master=root, text="", fg_color='white', text_color='black', text_font=font1,
                                           width=250)
        email_txt.configure(textvariable=self.email_txt)
        email_txt.place(x=1240, y=305)

        password_lbl = Label(root, text="Password: ", bg="#212325", fg="white",font=font)
        password_lbl.place(x=630, y=455)

        password_txt = customtkinter.CTkEntry(master=root, text="",  fg_color='white', text_color='black',
                                              text_font=font1, width=250)
        password_txt.configure(textvariable=self.password_txt)
        password_txt.place(x=650, y=365)

        credit_lbl = Label(root, text="Credit No: ",bg="#212325", fg="white", font=font)
        credit_lbl.place(x=1350, y=450)

        credit_txt = customtkinter.CTkEntry(master=root, text="",  fg_color='white', text_color='black', text_font=font1,
                                            width=250)
        credit_txt.configure(textvariable=self.credit_txt)
        credit_txt.place(x=1240, y=360)


        def save_customer_info():

            if (name_txt.get()=='') or (dob_txt.get()=='') or (gender_txt.get()=='') or (mobile_txt.get()=='') \
                        or (email_txt.get()=='') or (address_txt.get()=='') or (password_txt.get()=='') or (credit_txt.get()==0):
                warning=messagebox.showwarning("Taxi Booking System","Please enter all the field!")

            else:
                customer_info = Customer_Libs('', name_txt.get(), dob_txt.get(), gender_txt.get(),
                                              mobile_txt.get(), email_txt.get(), address_txt.get(),
                                              password_txt.get(), credit_txt.get())
                result = insert_record(customer_info)
                if result == True:
                    promt = messagebox.showinfo('Taxi Booking System', "Customer is registered successfully")
                else:
                    promt1 = messagebox.showerror("Error!", "Registration of customer info is unsuccessful!")





        register_btn_image = ImageTk.PhotoImage(
            Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit.png"))

        register_btn = customtkinter.CTkButton(master=root,command=save_customer_info,  text="Register", image=register_btn_image,
                                               hover_color='black', text_font=('Tahoma', 20, 'bold'))
        register_btn.place(x=900, y=500)

        def clear():
            self.name_txt.set('')
            self.mobile_txt.set('')
            self.credit_txt.set('')
            self.gender_txt.set('')
            self.address_txt.set('')
            self.password_txt.set('')
            self.email_txt.set('')

            if (name_txt.get()=='') or (mobile_txt.get()=='') or (credit_txt.get()=='') or \
               (address_txt.get()=='') or (password_txt.get()=='') or \
                (email_txt.get()==''):
                msg1=messagebox.showinfo("Taxi Booking System","All fields are cleared!")

            else:
                msg2=messagebox.showerror("Error!","Error ocurred!")








        #Clear btn image and button
        clear_btn_image = ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\cleaning.png"))
        clear_btn = customtkinter.CTkButton(master=root, command=clear, text="Clear",image=clear_btn_image,hover_color='black', text_font=('Tahoma', 20, 'bold'))
        clear_btn.place(x=1080, y=500)

        #Back button and label widget
        back_lbl = customtkinter.CTkLabel(master=root, text="Already have an account",
                                          text_font=('', 14, 'normal'),
                                          text_color='white')
        back_lbl.place(x=920, y=550)

        back_btn = customtkinter.CTkButton(master=root, text="SIGN IN", width=100, text_font=('Tahoma', 14, 'bold'),
                                           hover_color='black', command=signin)
        back_btn.place(x=1130, y=550)


if __name__ == '__main__':
    root = customtkinter.CTk()
    Register(root)
    root.mainloop()







