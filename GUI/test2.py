from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview, Style



class Table:
    def __init__(self, main):
        self.main=main
        self.main.title("Hancie Phago Table")
        self.main.geometry("800x500")

        TreeViewFrame=Frame(self.main, bg="green", height=400, width=400)
        TreeViewFrame.pack(side=RIGHT, fill=BOTH)

        scroll_y=Scrollbar(TreeViewFrame, orient=VERTICAL)
        scroll_y.pack(side="right", fill=Y)

        scroll_x=Scrollbar(TreeViewFrame, orient=HORIZONTAL)
        scroll_x.pack(side="bottom", fill=X)

        tree=Treeview(TreeViewFrame,height=20, columns=('ID','Name','Address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        tree.column('#0', width=0, stretch=NO)
        tree.column('ID',anchor=CENTER, width=220)
        tree.column('Name', anchor=CENTER, width=220)
        tree.column('Address', anchor=CENTER, width=220)

        scroll_x.config(command=tree.xview())
        scroll_y.config(command=tree.yview())

        tree.heading('#0', text='')
        tree.heading('ID', text='Person ID')
        tree.heading('Name', text='Name')
        tree.heading('Address', text='Address')

        tree.pack(side=RIGHT, fill=BOTH)

if __name__=='__main__':
    main=Tk()
    Table(main)
    main.mainloop()