from tkinter import *




window=Tk()
window.title("Basic Window")
window.geometry("500x300")

idlabel=Label(window, text="ID")
idlabel.pack()



idtxt=Entry(window)
idtxt.pack()

def isNumeric(str1):
    if str1.isnumeric():
        return True
    else:
        return False

def strToint(str1):
    return int(str1)

def checkRange(num1, num2, num3):
    if num1>=num2 and num1<=num3:
        return True
    else:
        return False


def save():
    id=idtxt.get()
    result1=isNumeric(id)
    if result1==True:
        numID=strToint(id)
        result3=checkRange(numID, 1,100)
        if result3==True:
            print("valid id")

        else:
            print("Out of range")
    else:
        print("Invalid")

btnsave=Button(window,command=save, text="Save")
btnsave.pack()





window.mainloop()