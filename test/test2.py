from tkinter import *

import pandas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

mydict={'Food':['Momo','Pizza','Burger'], 'Price':[200,100,300]}
df=pandas.DataFrame(data=mydict)
fig=df.plot.line(title="Food Menu", y='Price', figsize=(4,4)).get_figure()

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x400")
plot=FigureCanvasTkAgg(fig, app)
plot.get_tk_widget().place(x=20,y=20)


app.mainloop()