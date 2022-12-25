from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from tkinter import messagebox
from dbms.customer_management import update_customer_record
from libs import Global
from libs.customer_libs import Customer_Libs


#+++++++++++++++++++++++++++++++++Main Class++++++++++++++++++++++++++++++
class UpdateCustomerProfile():
    def __init__(self, updateprofile):
        self.updateprofile = updateprofile
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.updateprofile.resizable(0,0)
        self.updateprofile.title("{} Profile".format(Global.currentUser[1]))
        self.updateprofile.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        width = 750
        height = 440
        myscreenwidth = self.updateprofile.winfo_screenwidth()
        myscreenheight = self.updateprofile.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.updateprofile.geometry('{}x{}+{}+{}'.format(width, height, xCordinate, yCordinate - 50))
        self.updateprofile.maxsize(750, 440)

        id=Entry(self.updateprofile)
        id.insert(0, Global.currentUser[0])

        #++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 =customtkinter.CTkFont(family='Times New Roman', size=19, weight='normal')

        #++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++
        centerFrame = customtkinter.CTkFrame(master=self.updateprofile, width=710, height=360)
        centerFrame.place(x=20, y=60)

        #++++++++++++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++++
        namelbl = customtkinter.CTkLabel(centerFrame, text="Name: ", font=font720)
        namelbl.place(x=50, y=100)

        #+++++++++++++++++++++++++++++++++++++Global Name Label+++++++++++++++++++++++++++++++++++++
        namelbl1=customtkinter.CTkEntry(centerFrame,width=180,font=font720)
        namelbl1.insert(0,Global.currentUser[1])
        namelbl1.place(x=150, y=100)

        #++++++++++++++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        dob = customtkinter.CTkLabel(centerFrame, text="DOB: ", font=font720)
        dob.place(x=50, y=150)

        #+++++++++++++++++++++++++++++++++++++Global DOB Label+++++++++++++++++++++++++++++++++++++++
        # .format(Global.currentUser[2])
        dob1 = customtkinter.CTkEntry(centerFrame,width=180, font=font720)
        dob1.insert(0,Global.currentUser[2])
        dob1.place(x=150, y=150)

        # +++++++++++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++++
        gender = customtkinter.CTkLabel(centerFrame, text="Gender: ", font=font720)
        gender.place(x=50, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Gender Label+++++++++++++++++++++++++++++++++++++++
        gender1 = customtkinter.CTkEntry(centerFrame,width=180, font=font720)
        gender1.insert(0,Global.currentUser[3])
        gender1.place(x=150, y=200)

        # +++++++++++++++++++++++++++++++++++++Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile = customtkinter.CTkLabel(centerFrame, text="Mobile: ", font=font720)
        mobile.place(x=50, y=250)

        # +++++++++++++++++++++++++++++++++++++Global Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile1 = customtkinter.CTkEntry(centerFrame,width=180, font=font720)
        mobile1.insert(0, Global.currentUser[4])
        mobile1.place(x=150, y=250)

        # +++++++++++++++++++++++++++++++++++++Email Label+++++++++++++++++++++++++++++++++++++++
        email = customtkinter.CTkLabel(centerFrame, text="Email: ", font=font720)
        email.place(x=410, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Email Label+++++++++++++++++++++++++++++++++++++++
        email1 = customtkinter.CTkEntry(centerFrame,width=180,  font=font720)
        email1.insert(0,Global.currentUser[5])
        email1.place(x=510, y=100)

        # +++++++++++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++++
        address = customtkinter.CTkLabel(centerFrame, text="Address: ", font=font720)
        address.place(x=410, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Address Label+++++++++++++++++++++++++++++++++++++++
        address1 = customtkinter.CTkEntry(centerFrame,width=180, font=font720)
        address1.insert(0,Global.currentUser[6] )
        address1.place(x=510, y=150)


        # +++++++++++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++++
        credit = customtkinter.CTkLabel(centerFrame, text="Credit No: ", font=font720)
        credit.place(x=410, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Credit Label+++++++++++++++++++++++++++++++++++++++
        credit1 = customtkinter.CTkEntry(centerFrame,width=180, font=font720)
        credit1.insert(0, Global.currentUser[8])
        credit1.place(x=510, y=200)

        def updatecustomer():
            customer=Customer_Libs(cid=id.get(), name=namelbl1.get(),dob=dob1.get(),gender=gender1.get(), mobile=mobile1.get(), email=email1.get(), address=address1.get(), credit=credit1.get())
            updateResult=update_customer_record(customer)
            if updateResult==True:
                messagebox.showinfo("Taxi Booking System","The {} details is updated successfully!".format(Global.currentUser[1]))
                self.updateprofile.destroy()

            else:
                messagebox.showerror("Taxi Booking System","Error")

        update_btn_image = customtkinter.CTkImage(light_image=Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\edit-alt-regular-24.png'))
        update_btn = customtkinter.CTkButton(master=centerFrame,command=updatecustomer, text="Update Details",font=font720,image=update_btn_image)
        update_btn.place(x=300, y=320)

        # +++++++++++++++++++++++++++++++++++++Image Label+++++++++++++++++++++++++++++++++++++++
        user_image = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-120.png"))
        user_image_label = Label(self.updateprofile, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=400, y=20)


if __name__=='__main__':
    updateprofile=customtkinter.CTk()
    UpdateCustomerProfile(updateprofile)
    updateprofile.mainloop()