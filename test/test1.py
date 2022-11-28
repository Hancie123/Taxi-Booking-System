from tkinter import *
from PIL import ImageTk, Image
import customtkinter

class test720():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        self.main.title("Hancie Phago")
        self.main.geometry("500x400")

        self.photo = ImageTk.PhotoImage(Image.open("E:\\College Assignments\\Second Semester\\Python\\Taxi Booking System\\Images\\user-solid-72.png"))
        label = Label(self.main, image=self.photo)
        label.image = self.photo
        label.pack()

