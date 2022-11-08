from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import mysql.connector
import pandas
from tkinter import *

sqlEngine=create_engine('mysql+pymysql://root:@localhost/hancie')
db_connection=sqlEngine.connect()


query='SELECT * FROM daily_expenses limit 6'
df=pandas.read_sql(query, db_connection, index_col="category")
fig=df.plot.pie(title="Hancie Phago",y="amount",figsize=(8,5),legend=False, autopct='%1.0f%%').get_figure()


app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x400")
plot=FigureCanvasTkAgg(fig, app)
plot.get_tk_widget().place(x=10, y=10)


app.mainloop()



