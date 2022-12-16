from tkinter import ttk
import tkinter as tk
from sqlalchemy import create_engine

my_conn = create_engine('mysql+pymysql://root:@localhost/taxi_booking_system')

###### end of connection ####
r_set = my_conn.execute("SELECT count(*) as no from customers")
data_row = r_set.fetchone()
no_rec = data_row[0]  # Total number of rows in table
limit = 5;  # No of records to be shown per page.
##### tkinter window ######
from tkinter import ttk
import tkinter as tk

my_w = tk.Tk()
my_w.geometry("400x400")
my_str = tk.StringVar()  # to display query at end


def my_display(offset):
    ###
    trv = ttk.Treeview(my_w, selectmode='browse')

    trv.grid(row=1, column=2, padx=20, pady=20, columnspan=3)
    # number of columns
    trv["columns"] = ("1", "2", "3", "4", "5")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns and alignment
    trv.column("1", width=30, anchor='c')
    trv.column("2", width=80, anchor='w')
    trv.column("3", width=80, anchor='c')
    trv.column("4", width=80, anchor='c')
    trv.column("5", width=80, anchor='c')

    # Headings
    # respective columns
    trv.heading("1", text="id")
    trv.heading("2", text="Name")
    trv.heading("3", text="Class")
    trv.heading("4", text="Mark")
    trv.heading("5", text="Gender")
    ###
    q = "SELECT * from customers LIMIT " + str(offset) + "," + str(limit)
    r_set = my_conn.execute(q);

    for dt in r_set:
        trv.insert("", 'end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

    # Show buttons
    back = offset - limit  # This value is used by Previous button
    next = offset + limit  # This value is used by Next button
    b1 = tk.Button(my_w, text='< Prev', command=lambda: my_display(back))
    b1.grid(row=2, column=2, sticky='E')
    b2 = tk.Button(my_w, text='Next >', command=lambda: my_display(next))
    b2.grid(row=2, column=3)

    if (no_rec <= next):
        b2["state"] = "disabled"  # disable next button
    else:
        b2["state"] = "active"  # enable next button

    if (back >= 0):
        b1["state"] = "active"  # enable Prev button
    else:
        b1["state"] = "disabled"  # disable Prev button
    # for your understanding of how the offset value changes
    # query is displayed here, it is not part of the script
    my_str.set(q + '\n' + "next: " + str(next) + "\n back:" + str(back))
    l1 = tk.Label(my_w, textvariable=my_str)
    l1.grid(row=3, column=1, columnspan=3)


my_display(0)
my_w.mainloop()