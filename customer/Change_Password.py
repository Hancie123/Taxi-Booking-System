from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from tkinter import messagebox
from dbms.passwordchange_backend import passwordChange
from libs import Global
from libs.customer_libs import Customer_Libs



class Password_Change(customtkinter.CTk):
    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.root.title("Taxi Booking System | Change Customer Password")
        self.root.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")
        frame_width=530
        frame_height=400
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x_cordinate=int((screen_width/2)-(frame_width/2))
        y_cordinate=int((screen_height/2)-(frame_height/2))
        self.root.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate+70,y_cordinate-70))
        self.root.resizable(0,0)

        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill=BOTH, expand=TRUE)

        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        img=ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-72.png"))
        image_label=Label(self.root, image=img, bg="#2b2b2b")
        image_label.image=img
        image_label.place(x=150, y=40)


        title_lbl=customtkinter.CTkLabel(master=self.root, text="Changing password for\n{}".format(Global.currentUser[1]), font=font720, bg_color="#2b2b2b")
        title_lbl.place(x=200, y=40)

        currentpw_lbl=customtkinter.CTkLabel(master=self.root, text="New Password: ", font=font720, bg_color="#2b2b2b")
        currentpw_lbl.place(x=60, y=150)

        currentpw_txt=customtkinter.CTkEntry(master=self.root, font=font720,show='*', width=200)
        currentpw_txt.place(x=240, y=150)

        confirmpw_lbl = customtkinter.CTkLabel(master=self.root, text="Confirm Password: ", font=font720, bg_color="#2b2b2b")
        confirmpw_lbl.place(x=60, y=220)

        conformpw_txt = customtkinter.CTkEntry(master=self.root, show='*', font=font720, width=200)
        conformpw_txt.place(x=240, y=220)



        def show_password():
            if i.get() == 1:
                conformpw_txt.configure(show='')
                currentpw_txt.configure(show='')
            else:
                conformpw_txt.configure(show='*')
                currentpw_txt.configure(show='*')

        i = customtkinter.IntVar()

        password_show = customtkinter.CTkCheckBox(self.root, text="Show password", variable=i, command=show_password, bg_color="#2b2b2b")
        password_show.place(x=240, y=260)

        idtxt=Entry(self.root)
        idtxt.insert(0,"{}".format(Global.currentUser[0]))


        def change_password():
            customerid=idtxt.get()
            password1=currentpw_txt.get()
            newpassword=conformpw_txt.get()

            if password1 == newpassword:
                password720 = Customer_Libs(cid=customerid, password=newpassword)
                result = passwordChange(password720)
                if result == True:
                    messagebox.showinfo("Taxi Booking System", "The password is changed successfully!")
                    self.root.destroy()
                else:
                    messagebox.showerror("Taxi Booking System", "Error occurred!")

            else:
                messagebox.showerror("Taxi Booking System","The password does not match. Please try again!")





        confirm_btn = customtkinter.CTkButton(master=self.root,command=change_password, text="Change Password!", font=font720)
        confirm_btn.place(x=230, y=310)


if __name__=='__main__':
    root=customtkinter.CTk()
    Password_Change(root)
    root.mainloop()
