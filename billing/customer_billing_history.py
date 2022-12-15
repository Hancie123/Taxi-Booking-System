from tkinter import *
import customtkinter
from tkinter import ttk

from dbms.billing_backend import billing_history12, customer_billing_history
from dbms.driver_history_backend import customer_driver_history
from libs import Global


class CustomerBillingHistory():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("{} Billing History".format(Global.currentUser[1]))
        self.main.resizable(0, 0)
        frame_width = 1050
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate+50, y_cordinate+50))
        self.main.bind("<Escape>", lambda e:self.main.destroy())
        self.main.iconbitmap("E:\College Assignments\Second Semester\Python\Taxi Booking System\Images\logo.ico")

        font1 = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')

        topFrame = customtkinter.CTkFrame(self.main, height=80)
        topFrame.pack(side=TOP, fill=BOTH)

        titlelabel = customtkinter.CTkLabel(topFrame, text='{} Billing History'.format(Global.currentUser[1]), font=font1)
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        treeView=ttk.Treeview(self.main)
        treeView.pack(side=BOTTOM, fill=BOTH, expand=True)
        treeView['columns']=('pickupaddress', 'dropoffaddress','date', 'time','km','unit','total')
        treeView.column('#0', width=0, stretch=0)
        treeView.column('pickupaddress', width=100, anchor=CENTER)
        treeView.column('dropoffaddress', width=200, anchor=CENTER)
        treeView.column('date', width=200, anchor=CENTER)
        treeView.column('time', width=200, anchor=CENTER)
        treeView.column('km', width=100, anchor=CENTER)
        treeView.column('unit', width=100, anchor=CENTER)
        treeView.column('total', width=100, anchor=CENTER)


        treeView.heading('#0', text='', anchor=CENTER)
        treeView.heading('pickupaddress',text='Pickup Address', anchor=CENTER)
        treeView.heading('dropoffaddress', text='Dropoff Address', anchor=CENTER)
        treeView.heading('date', text='Date', anchor=CENTER)
        treeView.heading('time', text='Time', anchor=CENTER)
        treeView.heading('km', text='KM', anchor=CENTER)
        treeView.heading('unit', text='Unit', anchor=CENTER)
        treeView.heading('total', text='Total', anchor=CENTER)

        customerid=Entry(self.main)
        customerid.insert(0, Global.currentUser[0])


        def billingtable():
            id=customerid.get()
            billingHistory=customer_billing_history(id)

            for ro in billingHistory:
                treeView.insert(parent='', index='end', values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))


        billingtable()

        def getSum(item=""):
            val = 0
            for row in treeView.get_children(item):
                # print(trv.item(row)["values"][3])# print price
                val = val + treeView.item(row)["values"][6]
            print(val)
            treeView.insert(parent='', index='end', values=('','','','','','',"Total: {}".format(val)))

        getSum()







if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerBillingHistory(main)
    main.mainloop()