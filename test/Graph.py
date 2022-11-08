from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import pandas
import mysql.connector

sqlEngine = create_engine('mysql+pymysql://root:@localhost/hancie')
dbConnection = sqlEngine.connect()

query = "SELECT  Receiver_Name, SUM(Amount) as Amount1 FROM loan"
df = pandas.read_sql(query, dbConnection, index_col='Receiver_Name')
fig2 = df.plot.line(title="Loan Amount", y='Amount1', figsize=(5, 4)).get_figure();

import tkinter  as tk
my_w = tk.Tk()
my_w.geometry("600x600")  # Size of the window
my_w.title('Hancie e-Learning Studio')
plot2 = FigureCanvasTkAgg(fig2,my_w)
plot2.get_tk_widget().place(x=20, y=50)
my_w.mainloop()  # Keep the window open