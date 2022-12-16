from tkinter import *
from tkinter import ttk 


root = Tk()
root.title("Hancie e-Learning Studio")


data = [
        [1,"Hancie","Phago","hanciephago@mail.com",20],
        [3,"Nitesh","Hamal","nitesh0hamal@mail.com",20],
        [4,"Naindra","Phago","naindraraj@mail.com",47],
        [7,"Padam","Kumari","padam@mail.com",46],
        [8,"Bina","Phago","pq@mail.com",43],
        [9,"Sunita","Phago","rs@mail.com",35],
       ]


treeView = ttk.Treeview(root)
treeView['columns']=(1,2,3,4,5)
treeView.column('#0', width=0, stretch=0)
treeView.column(1, anchor='center', width=50)
treeView.column(2, anchor='center', width=100)
treeView.column(3, anchor='center', width=100)
treeView.column(4, anchor='center', width=100)
treeView.column(5, anchor='center', width=100)

treeView.heading('#0', text='')
treeView.heading(1, text='ID')
treeView.heading(2, text='First Name')
treeView.heading(3, text='Last Name')
treeView.heading(4, text='Email')
treeView.heading(5, text='Age')

# create a function to display data in treeview
def displayData():
    for row in data:
        treeView.insert('',END, values=row)


displayData()


treeView.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()