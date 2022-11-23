from tkinter import *
import customtkinter
import pandas
from matplotlib import axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


#++++++++++++++++++++++++++++++++GUI DESIGNING++++++++++++++++++++++++++++++++
class Driver_Dashboard():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        self.main.title("Hancie e-Learning Studio")
        self.main.state('zoomed')

#++++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++
        leftFrame=customtkinter.CTkFrame(self.main, width=300)
        leftFrame.pack(side=LEFT, fill=BOTH)

#+++++++++++++++++++++++++++Top Label++++++++++++++++++++++++++=
        welcomelbl=customtkinter.CTkLabel(master=self.main, text="Welcome Neuve Limbu", text_font=('', 14))
        welcomelbl.place(x=350, y=20)

        logoutbtn=customtkinter.CTkButton(master=self.main, text="Logout", text_font=('', 14),
                                          text_color="white", fg_color="black", hover_color="red")
        logoutbtn.place(x=1350, y=20)

#++++++++++++++++++++++++++++Top Frame++++++++++++++++++++++++++++++++++++++++++++++
        topFrame=customtkinter.CTkFrame(self.main, height=220)
        topFrame.pack(side=TOP, fill=BOTH, pady=(60,10), padx=10)

        totalCustomer=customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalCustomer.place(x=40, y=10)

        totalbooked = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalbooked.place(x=330, y=10)

        totalactive = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalactive.place(x=620, y=10)

        totalpaid = customtkinter.CTkFrame(master=topFrame, width=260, corner_radius=20)
        totalpaid.place(x=910, y=10)

#++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        centerFrame=customtkinter.CTkFrame(self.main)
        centerFrame.pack(side=TOP, fill=BOTH, expand=True, pady=(0,10), padx=10)

        sql_engine = create_engine('mysql+pymysql://root:@localhost/hancie')
        db_connection = sql_engine.connect()
        layout1 = dict(plot_bgcolor='green', paper_bgcolor='green')
        my_colors = [(.9, .4, .6), (.1, .3, .8)]
        query = 'SELECT * FROM daily_expenses limit 6'
        df = pandas.read_sql(query, db_connection, index_col='category')
        fig = df.plot.bar(title="Hancie Phago", y='amount', figsize=(3, 3),use_index = True, color=my_colors, legend=True
                          ,facecolor="red",layout=layout1, grid=False).get_figure()
        fig.set_facecolor('#2a2d2e')










        plot = FigureCanvasTkAgg(fig, centerFrame)
        plot.get_tk_widget().place(x=5, y=5)


        query = "SELECT *  FROM daily_expenses"
        df = pandas.read_sql(query, db_connection, index_col='date')
        fig2 = df.plot.line(title="Loan Amount", y='amount',  figsize=(3,3)).get_figure();

        plot2 = FigureCanvasTkAgg(fig2, centerFrame)
        plot2.get_tk_widget().place(x=800, y=5)


if __name__=='__main__':
    main=customtkinter.CTk()
    Driver_Dashboard(main)
    main.mainloop()
