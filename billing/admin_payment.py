from tkinter import *
import customtkinter
from tkinter import ttk

from dbms.billing_backend import billing_table


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
        nametxt.place(x=140, y=100)

        kmlbl = customtkinter.CTkLabel(assignbookingFrame, text="Kilometer: ", font=font720)
        kmlbl.place(x=30, y=150)

        kmtxt = customtkinter.CTkEntry(assignbookingFrame,textvariable=self.kmtxt, validate='key', validatecommand=(validation, '%P'), font=font720, width=200)
        kmtxt.place(x=140, y=150)

        unitlbl = customtkinter.CTkLabel(assignbookingFrame, text="Unit:", font=font720)
        unitlbl.place(x=30, y=200)

        unittxt = customtkinter.CTkEntry(assignbookingFrame,textvariable=self.unittxt, validate='key', validatecommand=(validation, '%P'), font=font720, width=200)
        unittxt.insert(0, '100')
        unittxt.configure(state=DISABLED)
        unittxt.place(x=140, y=200)

        totallbl = customtkinter.CTkLabel(assignbookingFrame, text="Grand Total:", font=font720)
        totallbl.place(x=30, y=250)


        totaltxt = customtkinter.CTkEntry(assignbookingFrame,font=font720, width=200)
        totaltxt.bind("<Key>", lambda e: "break")
        totaltxt.place(x=140, y=250)

        # Trace the variables
        self.unittxt.trace_add('write', calculate)
        self.kmtxt.trace_add('write', calculate)

        availabledriver_btn = customtkinter.CTkButton(assignbookingFrame,text="Generate Bill", font=font720, width=150)
        availabledriver_btn.place(x=150, y=320)

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
        bookingTable['columns'] = ('cid', 'bookingid', 'did', 'name', 'date', 'time', 'pickupaddress', 'dropoffaddress','drivername')
        bookingTable.column('#0', width=0, stretch=0)
        bookingTable.column('cid', width=0, stretch=0)
        bookingTable.column('bookingid', width=0, stretch=0)
        bookingTable.column('did', width=0, stretch=0)
        bookingTable.column('name', width=200, anchor=CENTER)
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
        bookingTable.heading('date', text="Date", anchor=CENTER)
        bookingTable.heading('time', text="Time", anchor=CENTER)
        bookingTable.heading('pickupaddress', text="Pickup Address", anchor=CENTER)
        bookingTable.heading('dropoffaddress', text="Dropoff Address", anchor=CENTER)
        bookingTable.heading('drivername', text="Driver Name", anchor=CENTER)

        def billing_tabel():

            bill720=billing_table()

            for b in bill720:
                bookingTable.insert(parent='', index='end', values=(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]))

        billing_tabel()

        def get_selectitem(a):
            nametxt.delete(0, END)

            selectitem=bookingTable.selection()[0]
            nametxt.insert(0, bookingTable.item(selectitem)['values'][3])

        bookingTable.bind('<<TreeviewSelect>>', get_selectitem)

if __name__=='__main__':
    main=customtkinter.CTk()
    Admin_Payment(main)
    main.mainloop()