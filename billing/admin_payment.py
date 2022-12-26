from datetime import date
from time import strftime
from tkinter import *
import customtkinter
from tkinter import ttk, filedialog
from tkinter import messagebox

from reportlab.lib.units import inch

from dbms.billing_backend import billing_table, insert_billing
from dbms.booking_backend import driver_update_booking
from libs.billing_libs import BillingLibs
from libs.booking_libs import BookingLibs
from reportlab.lib import units
from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import letter,A4
import random


class Admin_Payment():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("Taxi Booking System | Customer Billing System")
        self.main.resizable(0, 0)
        width = 1250
        height = 450
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate + 100, yCordinate))
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        titlefont = customtkinter.CTkFont(family='Times New Roman', size=35, weight='normal')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        font = customtkinter.CTkFont(family='Times New Roman', size=20, weight='bold')
        labelfont = customtkinter.CTkFont(family='Times New Roman', size=25, weight='normal')
        sidemenufont = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        num = random.randint(1000, 100000)

        def only_numbers(char):
            # Validate for numbers only
            if ((char.isdigit()) or (char == "")):
                return True
            else:
                return False

        validation = self.main.register(only_numbers)

        self.kmtxt = StringVar()
        self.unittxt = StringVar()

        def calculate(var, index, mode):
            if kmtxt.get() != "" and unittxt.get() != "":
                totaltxt.delete(0, END)
                totaltxt.insert(0, str(int(kmtxt.get()) * int(unittxt.get())))
            else:
                totaltxt.delete(0, END)

        assignbookingFrame = customtkinter.CTkFrame(self.main, width=400, corner_radius=20)
        assignbookingFrame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        title11lbl = customtkinter.CTkLabel(master=assignbookingFrame, text="CUSTOMER BILLING SYSTEM", font=font)
        title11lbl.place(x=50, y=20)

        namelnl = customtkinter.CTkLabel(assignbookingFrame, text="Name: ", font=font720)
        namelnl.place(x=30, y=100)

        nametxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
        nametxt.bind("<Button-1>", lambda e: "break")
        nametxt.bind("<Key>", lambda e: "break")
        nametxt.place(x=140, y=100)

        creditlbl = customtkinter.CTkLabel(assignbookingFrame, text="Credit No: ", font=font720)
        creditlbl.place(x=30, y=150)

        credittxt = customtkinter.CTkEntry(assignbookingFrame, font=font720, width=200)
        credittxt.bind("<Button-1>", lambda e: "break")
        credittxt.bind("<Key>", lambda e: "break")
        credittxt.place(x=140, y=150)

        kmlbl = customtkinter.CTkLabel(assignbookingFrame, text="Kilometer: ", font=font720)
        kmlbl.place(x=30, y=200)

        kmtxt = customtkinter.CTkEntry(assignbookingFrame,textvariable=self.kmtxt, validate='key', validatecommand=(validation, '%P'), font=font720, width=200)
        kmtxt.place(x=140, y=200)

        unitlbl = customtkinter.CTkLabel(assignbookingFrame, text="Unit:", font=font720)
        unitlbl.place(x=30, y=250)

        unittxt = customtkinter.CTkEntry(assignbookingFrame,textvariable=self.unittxt, validate='key', validatecommand=(validation, '%P'), font=font720, width=200)
        unittxt.insert(0, '100')
        unittxt.bind("<Button-1>", lambda e: "break")
        unittxt.bind("<Key>", lambda e: "break")
        unittxt.place(x=140, y=250)

        totallbl = customtkinter.CTkLabel(assignbookingFrame, text="Grand Total:", font=font720)
        totallbl.place(x=30, y=300)


        totaltxt = customtkinter.CTkEntry(assignbookingFrame,font=font720, width=200)
        totaltxt.bind("<Button-1>", lambda e: "break")
        totaltxt.bind("<Key>", lambda e: "break")
        totaltxt.place(x=140, y=300)

        # Trace the variables
        self.unittxt.trace_add('write', calculate)
        self.kmtxt.trace_add('write', calculate)

        bookingid=Entry(self.main)

        pickupaddresstxt=Entry(self.main)
        dropoffaddresstxt=Entry(self.main)
        datetxt=Entry(self.main)
        timetxt=Entry(self.main)


        def generate_bill():
            name=nametxt.get()
            km=kmtxt.get()
            unit=unittxt.get()
            total=totaltxt.get()
            bookingid1=bookingid.get()

            todatedate=date.today()

            billing=BillingLibs(billingid='',name=name, km=km, unit=unit, total=total, bookingid=bookingid1, date=todatedate)
            result=insert_billing(billing)

            booking=BookingLibs(bookingstatus='Billing Completed',bookingid=bookingid1)
            updatebookingResult=driver_update_booking(booking)
            if result==True:
                updatebookingresultlbl.configure(text="The bill is generated successfully")
                bookingTable.delete(*bookingTable.get_children())
                billing_tabel()

                mypath = "C:\\Users\\Hanci\Desktop\\Taxi Booking Bill\\{}.pdf".format(num)
                c = canvas.Canvas(mypath, pagesize=letter)
                c.setFont('Helvetica', 20)
                c.translate(inch, inch)
                c.setStrokeColorRGB(1, 0, 0)
                c.setLineWidth(2)
                c.line(0, 8 * inch, 7 * inch, 8 * inch)
                c.drawString(1 * inch, 9.1 * inch, "Taxi Booking System")
                c.setFont('Helvetica', 14)
                c.drawString(1 * inch, 8.8 * inch, 'Kathmandu, Nepal')


                c.drawString(5.8 * inch, 9.1 * inch, 'Bill No: {}'.format(num))

                # Taxi Receipt Label
                # txt1=txt.get()
                c.setFont('Times-Bold', 18)
                c.drawString(2.8 * inch, 8.1 * inch, 'TAXI RECEIPT')

                c.drawImage('E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo2.jpg',
                            -0.8 * inch, 8.4 * inch)

                c.setFont('Helvetica', 14)
                # Date label
                todaydate = date.today()
                c.drawString(0.5 * inch, 7.5 * inch, 'Date:   {}'.format(todaydate))

                # Time label
                currenttime = strftime("%I:%M:%S")
                c.drawString(5 * inch, 7.5 * inch, 'Time:   {}'.format(currenttime))

                # Customer Name
                c.drawString(0.5 * inch, 7 * inch, 'Name: {}'.format(nametxt.get()))

                # Pickup address
                c.drawString(0.5 * inch, 6.7 * inch, 'Pickup address: {}'.format(pickupaddresstxt.get()))

                # Dropoff address
                c.drawString(0.5 * inch, 6.4 * inch, 'Dropoff address: {}'.format(dropoffaddresstxt.get()))

                # Date
                c.drawString(0.5 * inch, 6.1 * inch, 'Date: {}'.format(datetxt.get()))

                # Time
                c.drawString(0.5 * inch, 5.8 * inch, 'Time: {}'.format(timetxt.get()))

                c.setStrokeColorRGB(1, 0, 0)
                c.setLineWidth(1)

                # Open line
                c.line(0, 5.5 * inch, 7 * inch, 5.5 * inch)
                # Close line
                c.line(0, 5 * inch, 7 * inch, 5 * inch)

                # Description
                c.drawString(0.5 * inch, 5.2 * inch, 'Description')

                # Kilometer label
                c.drawString(2.5 * inch, 5.2 * inch, 'Kilometer')

                # Unit label
                c.drawString(4.5 * inch, 5.2 * inch, 'Unit')

                # Total Label
                c.drawString(6 * inch, 5.2 * inch, 'Total')

                # ++++++++++++++++++++++++++++++++++++++Table Data+++++++++++++++++++++++++++++++
                # Description data
                c.drawString(0.5 * inch, 4.7 * inch, 'From {}'.format(pickupaddresstxt.get()))

                # Description data
                c.drawString(0.5 * inch, 4.4 * inch, 'To {}'.format(dropoffaddresstxt.get()))

                # Kilometer Data
                c.drawString(2.5 * inch, 4.7 * inch, '{} KM'.format(kmtxt.get()))

                # Unit Data
                c.drawString(4.5 * inch, 4.7 * inch, '100')

                # Total Data
                c.drawString(5.9 * inch, 4.7 * inch, 'Rs. {}'.format(totaltxt.get()))

                # Signature data
                c.drawString(0.5 * inch, 1.7 * inch, 'Signature')

                c.drawImage(
                    'E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\hancieSignature.jpg',
                    0.5 * inch,
                    0.3 * inch)

                c.showPage()
                c.save()



            else:
                messagebox.showerror("Taxi Booking System","Error Occurred")





        availabledriver_btn = customtkinter.CTkButton(assignbookingFrame,text="Generate Bill",command=generate_bill, font=font720, width=150)
        availabledriver_btn.place(x=150, y=350)

        updatebookingresultlbl = customtkinter.CTkLabel(assignbookingFrame, text="", font=font720)
        updatebookingresultlbl.place(x=80, y=390)

        tableFrame = customtkinter.CTkFrame(master=self.main, width=840)
        tableFrame.pack(side=LEFT, fill=BOTH,expand=True, padx=(0, 10), pady=10)

        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#2b2b2b",
                         foreground="white",
                         rowheight=25,
                         fieldbackground="#2b2b2b",
                         bordercolor="#343638",
                         borderwidth=0,
                         font=('Times New Roman', 16))
        style1.map('Treeview', background=[('selected', '#22559b')])

        style1.configure("Treeview.Heading",
                         background="#565b5e",
                         foreground="white",
                         relief="flat",
                         font=('Times New Roman', 17))
        style1.map("Treeview.Heading",
                   background=[('active', '#3484F0')], )

        bookingTable = ttk.Treeview(tableFrame)
        bookingTable.pack(side=TOP, fill=BOTH,expand=True, padx=5, pady=5)
        bookingTable['columns'] = ('cid', 'bookingid', 'did', 'name','credit', 'date', 'time', 'pickupaddress', 'dropoffaddress','drivername')
        bookingTable.column('#0', width=0, stretch=0)
        bookingTable.column('cid', width=0, stretch=0)
        bookingTable.column('bookingid', width=0, stretch=0)
        bookingTable.column('did', width=0, stretch=0)
        bookingTable.column('name', width=200, anchor=CENTER)
        bookingTable.column('credit', width=0, stretch=0)
        bookingTable.column('date', width=120, anchor=CENTER)
        bookingTable.column('time', width=100, anchor=CENTER)
        bookingTable.column('pickupaddress', width=200, anchor=CENTER)
        bookingTable.column('dropoffaddress', width=200, anchor=CENTER)
        bookingTable.column('drivername', width=200, anchor=CENTER)

        bookingTable.heading('#0', text='', anchor=CENTER)
        bookingTable.heading('cid', text="", anchor=CENTER)
        bookingTable.heading('bookingid', text="", anchor=CENTER)
        bookingTable.heading('did', text="", anchor=CENTER)
        bookingTable.heading('name', text="Customer Name", anchor=CENTER)
        bookingTable.heading('credit', text="", anchor=CENTER)
        bookingTable.heading('date', text="Date", anchor=CENTER)
        bookingTable.heading('time', text="Time", anchor=CENTER)
        bookingTable.heading('pickupaddress', text="Pickup Address", anchor=CENTER)
        bookingTable.heading('dropoffaddress', text="Dropoff Address", anchor=CENTER)
        bookingTable.heading('drivername', text="Driver Name", anchor=CENTER)



        def get_selectitem(a):
            nametxt.delete(0, END)
            credittxt.delete(0, END)
            bookingid.delete(0, END)
            pickupaddresstxt.delete(0, END)
            dropoffaddresstxt.delete(0, END)
            datetxt.delete(0, END)
            timetxt.delete(0, END)


            selectitem=bookingTable.selection()[0]
            nametxt.insert(0, bookingTable.item(selectitem)['values'][3])
            credittxt.insert(0, bookingTable.item(selectitem)['values'][4])
            bookingid.insert(0, bookingTable.item(selectitem)['values'][1])

            pickupaddresstxt.insert(0, bookingTable.item(selectitem)['values'][7])
            dropoffaddresstxt.insert(0, bookingTable.item(selectitem)['values'][8])
            datetxt.insert(0, bookingTable.item(selectitem)['values'][5])
            timetxt.insert(0, bookingTable.item(selectitem)['values'][6])

        bookingTable.bind('<<TreeviewSelect>>', get_selectitem)

        def billing_tabel():

            bill720=billing_table()

            for b in bill720:
                bookingTable.insert(parent='', index='end', values=(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9]))

        billing_tabel()

if __name__=='__main__':
    main=customtkinter.CTk()
    Admin_Payment(main)
    main.mainloop()