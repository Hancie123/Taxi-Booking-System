from datetime import date
from time import strftime
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

    #Taxi Receipt Label
    # txt1=txt.get()
    c.setFont('Times-Bold', 18)
    c.drawString(2.8 * inch, 8.1 * inch,'TAXI RECEIPT')

    c.drawImage('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo2.jpg', -0.8 * inch,8.4 * inch)

    c.setFont('Helvetica', 14)
    #Date label
    todaydate=date.today()
    c.drawString(0.5*inch, 7.5*inch,'Date:   {}'.format(todaydate))

    # Time label
    currenttime = strftime("%I:%M:%S")
    c.drawString(5 * inch, 7.5 * inch, 'Time:   {}'.format(currenttime))

    # Customer Name
    c.drawString(0.5 * inch, 7 * inch, 'Name: Hancie Phago')

    # Pickup address
    c.drawString(0.5 * inch, 6.7 * inch, 'Pickup address: Kathmandu')

    #Dropoff address
    c.drawString(0.5 * inch, 6.4* inch, 'Dropoff address: Lalitpur')

    # Date
    c.drawString(0.5 * inch, 6.1 * inch, 'Date: 2022-12-12')

    # Time
    c.drawString(0.5 * inch, 5.8 * inch, 'Time: 2022-12-12')

    c.setStrokeColorRGB(1,0,0)
    c.setLineWidth(1)

    #Open line
    c.line(0,5.5*inch, 7*inch,5.5*inch)
    #Close line
    c.line(0,5*inch,7*inch,5*inch )

    # Description
    c.drawString(0.5 * inch, 5.2 * inch, 'Description')

    # Kilometer label
    c.drawString(2.5 * inch, 5.2 * inch, 'Kilometer')

    # Unit label
    c.drawString(4.5 * inch, 5.2 * inch, 'Unit')

    # Total Label
    c.drawString(6 * inch, 5.2 * inch, 'Total')

    #++++++++++++++++++++++++++++++++++++++Table Data+++++++++++++++++++++++++++++++
    # Description data
    c.drawString(0.5 * inch, 4.7 * inch, 'From Kathmandu')

    # Description data
    c.drawString(0.5 * inch, 4.4 * inch, 'To Godawari')

    # Kilometer Data
    c.drawString(2.5 * inch, 4.7 * inch, '20 Km')

    # Unit Data
    c.drawString(4.5 * inch, 4.7 * inch, '100')

    # Total Data
    c.drawString(5.9 * inch, 4.7 * inch, 'Rs. 1200')

    # Signature data
    c.drawString(0.5 * inch, 1.7 * inch, 'Signature')

    c.drawImage('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\hancieSignature.jpg', 0.5 * inch,
                0.3*inch)









    c.showPage()
    c.save()

btn=Button(app,text="Export",command=pdf)
btn.pack()



pdf()







