import pandas
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import mysql.connector
from tkinter import *

sql_engine=create_engine('mysql+pymysql://root:@localhost/hancie')
db_connection=sql_engine.connect()

my_colors=[(.9,.4,.6),(.1,.3,.8)]
query='SELECT * FROM daily_expenses'
df=pandas.read_sql(query, db_connection, index_col='category')
fig=df.plot.bar(title="Hancie Phago", y='amount', figsize=(6,6), color=my_colors, legend=True, grid=False).get_figure()

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")
plot=FigureCanvasTkAgg(fig, app)
plot.get_tk_widget().place(x=5, y=5)


app.mainloop()