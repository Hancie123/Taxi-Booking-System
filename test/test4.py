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
        titlelbl.place(x=100,y=20)


        emaillbl=Label(self.main, text="Email: ", font=myfont)
        emaillbl.grid(row=1, column=0, pady=(50,0))


        emailfield=Entry(self.main, font=myfont)
        emailfield.grid(row=1,column=1)


        passwordlbl=Label(self.main, text="Password: ", font=myfont)


        passwordField=Entry(self.main, font=myfont, show='*')


        loginBT=Button(self.main, text="Login", font=myfont, bg="red", fg="white")


        registerBT=Button(self.main, text="Register", font=myfont , bg="red", fg="white")







if __name__=='__main__':
    main=Tk()
    Sweksha(main)
    main.mainloop()