from customer.Customer_Register import Register
from customer.Login import Login
from tkinter import *
import customtkinter


if __name__ == '__main__':
    root = customtkinter.CTk()
    Login(root)
    root.mainloop()

