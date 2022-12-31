from tkinter import *


class test():
    def __init__(self, root):
        self.root=root
        self.root.state('zoomed')

        index = 0
        txt = [' ', '|', ' ', '|', ' ', '|', 'W|', 'WE|', 'WEL|', 'WELC|', 'WELCO|', 'WELCOM|', 'WELCOME|', 'WELCOME |',
               'WELCOME U|', 'WELCOME US|'
            , 'WELCOME USE|', 'WELCOME USER|']

        def start_animation():
            index = 0


            if not index + 1 > len(txt):
                text_animation_lbl.config(text=txt[index])
                index += 1
                self.after(250, start_animation)

            else:
                index = 0
                text_animation_lbl.config(text='|')
                self.after(250, start_animation)

        text_animation_lbl = Label(self.root, text="|", font=("verdana", 24, "bold"))
        text_animation_lbl.grid(row=0, column=0)

        self.root.after(250, start_animation)




if __name__=='__main__':
    root=Tk()
    test(root)
    root.mainloop()