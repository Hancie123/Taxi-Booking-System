from tkinter import *
import customtkinter

class DriverHistory:
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Driver History")
        self.main.resizable(0, 0)
        frame_width = 900
        frame_height = 600
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate-50, y_cordinate-90))
        self.main.bind("<Escape>", lambda e:self.main.destroy())
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")







if __name__=='__main__':
    main=customtkinter.CTk()
    DriverHistory(main)
    main.mainloop()