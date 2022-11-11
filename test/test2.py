from tkinter import *

class Sweksha:
    def __init__(self, main):
        self.main=main
        self.main.title("Sweksha Basnet")
        # self.main.state('zoomed')
        self.main.resizable(FALSE,FALSE)

        #Center window in screen
        width=700
        height=400
        frameWidth=self.main.winfo_screenwidth()
        frameHeight=self.main.winfo_screenheight()
        xCordinate=int((frameWidth/2)-(width/2))
        yCordinate=int((frameHeight/2)-(height/2))
        self.main.geometry('{}x{}+{}+{}'.format(width,height,xCordinate,yCordinate-60))


        myfont=('Helvetica', '16','bold')

        titlelbl=Label(self.main, text="TAXI BOOKING LOGIN", font=('Helvetica',20,'bold'))
        titlelbl.pack(side=TOP, fill=BOTH)


        emaillbl=Label(self.main, text="Email: ", font=myfont)
        emaillbl.place(x=180,y=100)

        emailfield=Entry(self.main, font=myfont)
        emailfield.place(x=300, y=100)

        passwordlbl=Label(self.main, text="Password: ", font=myfont)
        passwordlbl.place(x=180, y=160)

        passwordField=Entry(self.main, font=myfont, show='*')
        passwordField.place(x=300, y=160)

        loginBT=Button(self.main, text="Login", font=myfont, bg="red", fg="white")
        loginBT.place(x=300, y=250)

        registerBT=Button(self.main, text="Register", font=myfont , bg="red", fg="white")
        registerBT.place(x=400, y=250)


        



if __name__=='__main__':
    main=Tk()
    Sweksha(main)
    main.mainloop()








