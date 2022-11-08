import pandas
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import mysql.connector
from tkinter import *
from scipy.stats import gaussian_kde

sql_engine=create_engine('mysql+pymysql://root:@localhost/hancie')
db_connection=sql_engine.connect()


query='SELECT Note_ID from notes'
df=pandas.read_sql(query, db_connection)
fig=df.plot.density(title="Hancie Phago", y='Note_ID', figsize=(5,5)).get_figure()

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")
plot=FigureCanvasTkAgg(fig, app)
plot.get_tk_widget().place(x=5, y=5)


app.mainloop()