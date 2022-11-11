from tkinter import *
from test import test2


class App720:
    def __init__(self, main):
        self.main=main
        self.main.title("Hancie e-Learning Studio")
        self.main.geometry("500x300")

        def switch_frame():
            self.main.destroy()
            root=Tk()
            sw=test2.App123(root)
            root.mainloop()



        tc_btn=Button(self.main, text="Button", font=('Helvetica',16), command=switch_frame)
        tc_btn.pack(pady=20)

main=Tk()
App720(main)
main.mainloop()