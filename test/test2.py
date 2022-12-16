from tkinter import *
from PIL import ImageTk, Image

class Hancie():
    def __init__(self, root):
        self.root=root

        image = Image.open('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.jpg')
        image = image.resize((400, 400))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(self.root, image=image)
        Image_Label.image = image
        Image_Label.place(x=20, y=20)


if __name__=='__main__':
    root=Tk()
    Hancie(root)
    root.mainloop()
