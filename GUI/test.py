from tkinter import *
from tkinter.ttk import Treeview, Style


class Registration:

    def __init__(self, register):
        self.register=register
        self.register.geometry("500x500")

        self.TreeviewFrame = Frame(self.register, width=850, height=500, bg='skyblue')
        self.TreeviewFrame.place(x=200, y=220, width=1200, height=550)

        # ********************************************    table and its elements   ******************************************
        # creating scroll bar
        scroll_y = Scrollbar(self.TreeviewFrame, orient=VERTICAL)
        scroll_y.pack(side='right', fill=Y)
        scroll_x = Scrollbar(self.TreeviewFrame, orient=HORIZONTAL)
        scroll_x.pack(side='bottom', fill=X)

        # adding some styles to treeview method

        # Add Some Style
        style = Style()
        # Pick A Theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#D3D3D3")

        # table frame defining columns
        self.tree = Treeview(self.TreeviewFrame, height=20,
                             columns=('bookingID', 'customerName', 'pdate', 'ptime', 'paddress', 'daddress', 'bstatus'),
                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, selectmode='extended')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('bookingID', anchor=CENTER, width=50, minwidth=30)
        self.tree.column('customerName', anchor=CENTER, width=140)
        self.tree.column('pdate', anchor=CENTER, width=140)
        self.tree.column('ptime', anchor=CENTER, width=140)
        self.tree.column('paddress', anchor=CENTER, width=140)
        self.tree.column('daddress', anchor=CENTER, width=140)
        self.tree.column('bstatus', anchor=CENTER, width=140)

        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

        # heading of the columns
        self.tree.heading('#0', text='')
        self.tree.heading('bookingID', text='Booking ID', anchor=CENTER)
        self.tree.heading('customerName', text='Customer Name', anchor=CENTER)
        self.tree.heading('pdate', text='Date of booking', anchor=CENTER)
        self.tree.heading('ptime', text='Pick up time', anchor=CENTER)
        self.tree.heading('paddress', text='Pick up Address', anchor=CENTER)
        self.tree.heading('daddress', text='Drop off Address', anchor=CENTER)
        self.tree.heading('bstatus', text='Booking Status', anchor=CENTER)

        self.tree.pack()





if __name__=='__main__':
    register=Tk()
    Registration(register)
    register.mainloop()