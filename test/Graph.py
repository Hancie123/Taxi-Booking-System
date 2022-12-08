from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import pandas



sqlEngine = create_engine('mysql+pymysql://root:@localhost/hancie')
dbConnection = sqlEngine.connect()

query = "SELECT *  FROM daily_expenses"

df = pandas.read_sql(query, dbConnection, index_col='date')



fig2 = df.plot.line(title="Loan Amount", y='amount',color="blue", figsize=(5, 4)).get_figure();
fig2.savefig("output.pdf", facecolor=fig2.get_facecolor(), transparent=True)

import tkinter  as tk
my_w = tk.Tk()
my_w.geometry("600x600")  # Size of the window
my_w.title('Hancie e-Learning Studio')
plot2 = FigureCanvasTkAgg(fig2,my_w)
plot2.get_tk_widget().place(x=20, y=50)


my_w.mainloop()  # Keep the window open