from tkinter import *
from tkinter import ttk
from sqlalchemy import create_engine

window=Tk()
window.title("Table in Tkinter")
window.geometry("500x400")
window.resizable(width=0, height=0)

my_conn = create_engine('mysql+pymysql://root:@localhost/taxi_booking_system')

tableFrame=Frame(window)
tableFrame.pack()

tblPerson=ttk.Treeview(tableFrame)
tblPerson['columns']=('cid', 'name','dob','email','password')
tblPerson.column('#0', width=0, stretch=NO)
tblPerson.column('cid', width=50, anchor=CENTER)
tblPerson.column('name', width=100, anchor=CENTER)
tblPerson.column('dob', width=50, anchor=CENTER)
tblPerson.column('email', width=100, anchor=CENTER)
tblPerson.column('password', width=100, anchor=CENTER)

tblPerson.heading('#0', text='', anchor=CENTER)
tblPerson.heading('cid', text='CID', anchor=CENTER)
tblPerson.heading('name', text='Name', anchor=CENTER)
tblPerson.heading('dob', text='DOB', anchor=CENTER)
tblPerson.heading('email', text='Email', anchor=CENTER)
tblPerson.heading('password', text='Password', anchor=CENTER)

r_set=my_conn.execute('''SELECT * from booking''')
for dt in r_set:
    tblPerson.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4]))

tblPerson.pack()
window.mainloop()