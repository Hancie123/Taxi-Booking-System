from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import inch
import random
from tkinter.filedialog import asksaveasfile
app=Tk()
app.geometry("500x300")

mypath="C:\\Users\\Hanci\Desktop\\g.pdf"

txt=Entry(app)
txt.pack()

def pdf():
    c = canvas.Canvas(mypath, pagesize=letter)
    c.setFont('Helvetica', 20)
    c.translate(inch, inch)
    c.setStrokeColorRGB(1, 0, 0)
    c.setLineWidth(2)
    c.line(0, 8 * inch, 7 * inch, 8 * inch)
    c.drawString(1 * inch, 9.1 * inch, "Taxi Booking System")
    c.setFont('Helvetica', 14)
    c.drawString(1 * inch, 8.8 * inch, 'Kathmandu, Nepal')

    num = random.randint(1000, 100000)
    c.drawString(5.8 * inch, 9.1 * inch, 'Bill No: {}'.format(num))

    txt1=txt.get()
    c.drawString(5.8 * inch, 5.1 * inch,'{}'.format(txt1))

    c.drawImage('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo2.jpg', -0.8 * inch,
                8.4 * inch)

    c.setFont("Helvetica", 140)
    c.rotate(-45)  # restore the rotation
    c.setFillColorRGB(0, 0, 0)  # font colour
    # font style and size
    c.drawString(2 * inch, 1 * inch, "SAMPLE")  # String written

    c.showPage()
    c.save()

btn=Button(app,text="Export",command=pdf)
btn.pack()







app.mainloop()




