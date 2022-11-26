from tkinter import *

ws = Tk()
Frm = Frame(ws)
Label(Frm, text='Enter Word to Find:').pack(side=LEFT)
modify = Entry(Frm)

modify.pack(side=LEFT, fill=BOTH, expand=1)

modify.focus_set()

buttn = Button(Frm, text='Find')
buttn.pack(side=RIGHT)
Frm.pack(side=TOP)

txt = Text(ws)

txt.insert('1.0', '''Enter here...''')
txt.pack(side=BOTTOM)


def find():
    txt.tag_remove('found', '1.0', END)
    ser = modify.get()
    if ser:
        idx = '1.0'
        while 1:
            idx = txt.search(ser, idx, nocase=1,
                             stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(ser))

            txt.tag_add('found', idx, lastidx)
            idx = lastidx
        txt.tag_config('found', foreground='blue')
    modify.focus_set()


buttn.config(command=find)

ws.mainloop()