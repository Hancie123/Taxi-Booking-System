from datetime import date, datetime
from tkinter import messagebox, ttk
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from admin import admin_dashboard
from customer import Customer_Register, customer_dashboard
from customer.customer_dashboard import Customer_Dashboard
from dbms.customer_management import insert_record
from dbms.myactivity_backend import activity_insert
from driver import DriverDashboard, driverhistory
from driver.driverhistory import DriverHistory
from libs import Global
from libs.customer_libs import Customer_Libs
from dbms.login_management import login, driverlogin, adminLogin
import platform

from libs.myactivity_libs import MyActivity


class Login(customtkinter.CTk):
    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.root.screen_width=root.winfo_screenwidth()
        self.root.screen_height=root.winfo_screenheight()
        self.root.minsize(self.root.screen_width, self.root.screen_height)
        self.root.state('zoomed')
        self.root.title("Taxi Booking System Login")
        self.root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        self.root.bind('<Escape>', lambda e: root.destroy())

        font1 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        north_frame = customtkinter.CTkFrame(master=root, height=100)
        north_frame.pack(side=TOP, fill=BOTH)

        title_label = customtkinter.CTkLabel(master=north_frame, text="TAXI BOOKING SYSTEM", font=('Times New Roman', 35, 'bold'))
        title_label.place(x=650, y=40)

        frame1 = customtkinter.CTkFrame(master=root, width=400, height=400, corner_radius=20)
        frame1.pack(side=LEFT, padx=20)

        canvas = Canvas(frame1, width=900, height=900, bg="#212325", borderwidth=0, bd=0, highlightthickness=0)
        image=ImageTk.PhotoImage(Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Tablet login-rafiki.png"))
        canvas.create_image(120, 120, image=image)
        canvas.pack()

        Cover_Image = Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\Tablet login-rafiki.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(frame1, image=photo1, bg="#212325")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=10, y=0)

        # frame2 = customtkinter.CTkFrame(master=root, width=750, height=600, corner_radius=20)
        # frame2.pack(side=RIGHT, padx=30)

        parent_tab=customtkinter.CTkTabview(self.root, width=750, height=600)
        parent_tab.pack(side=RIGHT, padx=30)

        parent_tab.add('Sign In')


        sign_in_image = Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(master=parent_tab.tab('Sign In'), image=photo, bg="#2b2b2b")
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=380, y=40)

        signin_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Sign In", font=font1)
        signin_lbl.place(x=330, y=150)

        email_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Email: ", font=font1)
        email_lbl.place(x=200, y=205)

        email_txt1 = customtkinter.CTkEntry(master=parent_tab.tab('Sign In'), corner_radius=10, font=font1, width=200)
        email_txt1.insert(0, 'neuve@gmail.com')
        email_txt1.place(x=330, y=200)

        password_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Password: ", font=font1)
        password_lbl.place(x=200, y=255)

        def show_password():
            if i.get()==1:
                password_txt1.configure(show='')
            else:
                password_txt1.configure(show='*')

        i=customtkinter.IntVar()

        password_txt1 = customtkinter.CTkEntry(master=parent_tab.tab('Sign In'), show="*", corner_radius=10, font=font1, width=200)
        password_txt1.insert(0,'0720')
        password_txt1.place(x=330, y=250)

        password_show = customtkinter.CTkCheckBox(master=parent_tab.tab('Sign In'), text="Show password", variable=i, command=show_password)
        password_show.place(x=330, y=290)

        def login_customer():
            login720=Customer_Libs(email=email_txt1.get(), password=password_txt1.get())
            user=login(login720)
            driverresult=driverlogin(login720)
            adminresult=adminLogin(login720)

            if email_txt1.get()=="" or password_txt1.get()=='':
                messagebox.showerror("Taxi Booking System","Please enter email and password!")

            else:
                if user != None:
                    if user[9] == 'Customer':
                        Global.currentUser = user

                        # myid = user[0]
                        # my_system = platform.uname()
                        # system11 = (f"{my_system.system}")
                        # model11 = (f"{my_system.node}")
                        # machine11 = (f"{my_system.machine}")
                        # processor11 = (f"{my_system.processor}")
                        #
                        # date11 = date.today()
                        # now = datetime.now()
                        # current_time = now.strftime("%I:%M:%S")
                        #
                        # LoginActivity = MyActivity('', system=system11, model=model11, machine=machine11,
                        #                            processor=processor11, date=date11, date2=current_time, cid=myid)
                        # activityResult = activity_insert(LoginActivity)


                        self.root.destroy()
                        root = customtkinter.CTk()
                        obj2 = customer_dashboard.Customer_Dashboard(root)
                        root.mainloop()

                elif driverresult != None:
                    Global.currentDriver=driverresult
                    self.root.destroy()
                    root = customtkinter.CTk()
                    DriverDashboard.Driver_Dashboard(root)
                    root.mainloop()

                elif adminresult != None:
                    Global.currentAdmin = adminresult
                    self.root.destroy()
                    root = customtkinter.CTk()
                    obj2 = admin_dashboard.Admin_Dashboard(root)
                    root.mainloop()


                else:
                    msg = messagebox.showerror("Taxi Booking System", "Incorrect email and password!")


        # Use CTkButton instead of tkinter Button
        add_login_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\login.png").resize((50, 50)))
        button = customtkinter.CTkButton(master=parent_tab.tab('Sign In'),command=login_customer, text="Login", image=add_login_image,
                                         corner_radius=10,
                                         text_color="white", font=('',18, 'bold'), hover_color="black")
        button.place(x=340, y=350)

        signup_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="No account yet")
        signup_lbl.place(x=320, y=420)


        def signup():
            self.root.destroy()
            root=customtkinter.CTk()
            obj=Customer_Register.Register(root)
            root.mainloop()

        signup_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign In'), text="SIGN UP NOW", width=50, height=20,
                                             hover_color="black", command=signup)


        signup_btn.place(x=410, y=420)

        parent_tab.add('Sign Up')

        signupframe=customtkinter.CTkFrame(master=parent_tab.tab('Sign Up'), height=70,)
        signupframe.pack(side=TOP, fill=BOTH, pady=(20,0))

        signuptitle=customtkinter.CTkLabel(master=signupframe, text="CUSTOMER REGISTRATION FORM", font=('Times New Roman',20, 'bold'))
        signuptitle.place(x=200, y=20)

        # ===========================All Variables===========
        self.name_txt = StringVar()
        self.mobile_txt = StringVar()
        self.gender_txt = StringVar()
        self.email_txt = StringVar()
        self.address_txt = StringVar()
        self.password_txt = StringVar()
        self.credit_txt = StringVar()

        name_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Name: ",font=font1)
        name_lbl.place(x=20, y=150)

        name_txt = customtkinter.CTkEntry(parent_tab.tab('Sign Up'), font=font1,width=200)
        name_txt.configure(textvariable=self.name_txt)
        name_txt.place(x=110, y=150)

        dob_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="DOB: ", font=font1)
        dob_lbl.place(x=20, y=200)

        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='black',
                        arrowcolor='red')
        dob_txt = DateEntry(parent_tab.tab('Sign Up'), font=('Times New Roman',18), selectmode='day', style='my.DateEntry', background="green",bordercolor="red",selectbackground="green", width=17, date_pattern='yyyy-mm-dd')
        dob_txt.place(x=135, y=255)

        gender_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Gender: ", font=font1)
        gender_lbl.place(x=20, y=250)

        gender_txt = customtkinter.CTkOptionMenu(master=parent_tab.tab('Sign Up'),  variable=self.gender_txt,values=['Male', 'Female', 'Others'], font=font1, width=200)
        gender_txt.set('Male')
        gender_txt.place(x=110, y=250)

        password_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Password: ",font=font1)
        password_lbl.place(x=20, y=300)

        password_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1, width=200)
        password_txt.configure(textvariable=self.password_txt)
        password_txt.place(x=110, y=300)

        mobile_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Mobile: ", font=font1)
        mobile_lbl.place(x=400, y=150)

        mobile_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1,width=200)
        mobile_txt.configure(textvariable=self.mobile_txt)
        mobile_txt.place(x=480, y=150)

        address_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Address: ",font=font1)
        address_lbl.place(x=400, y=200)

        address_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1, width=200)
        address_txt.configure(textvariable=self.address_txt)
        address_txt.place(x=480, y=200)

        email_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Email: ",font=font1)
        email_lbl.place(x=400, y=250)

        email_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'),font=font1,width=200)
        email_txt.configure(textvariable=self.email_txt)
        email_txt.place(x=480, y=250)

        credit_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Credit: ", font=font1)
        credit_lbl.place(x=400, y=300)

        credit_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1,width=200)
        credit_txt.configure(textvariable=self.credit_txt)
        credit_txt.place(x=480, y=300)

        def save_customer_info():

            if (name_txt.get() == '') or (dob_txt.get() == '') or (gender_txt.get() == '') or (mobile_txt.get() == '') \
                    or (email_txt.get() == '') or (address_txt.get() == '') or (password_txt.get() == '') or (
                    credit_txt.get() == 0):
                warning = messagebox.showwarning("Taxi Booking System", "Please enter all the field!")

            else:
                customer_info = Customer_Libs('', name_txt.get(), dob_txt.get(), gender_txt.get(),
                                              mobile_txt.get(), email_txt.get(), address_txt.get(),
                                              password_txt.get(), credit_txt.get(), status="Customer")
                result = insert_record(customer_info)
                if result == True:
                    promt = messagebox.showinfo('Taxi Booking System', "Customer is registered successfully")
                else:
                    promt1 = messagebox.showerror("Error!", "Registration of customer info is unsuccessful!")

        register_btn_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit.png"))
        register_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign Up'),command=save_customer_info, text="Register",image=register_btn_image,hover_color='black', font=('Tahoma', 20, 'bold'))
        register_btn.place(x=150, y=400)

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

        clear_btn_image = customtkinter.CTkImage(light_image=Image.open("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\cleaning.png"))
        clear_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign Up'),command=clear,  text="Clear", image=clear_btn_image,hover_color='black', font=('Tahoma', 20, 'bold'))
        clear_btn.place(x=300, y=400)



if __name__ == '__main__':
    root = customtkinter.CTk()
    Login(root)
    root.mainloop()
















