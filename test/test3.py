from sqlalchemy import create_engine
import customtkinter
my_conn = create_engine("mysql+pymysql://root:@localhost/taxi_booking_system")

query = "SELECT DISTINCT(bookingid) as class FROM booking"

my_data = my_conn.execute(query)  # SQLAlchem engine result
my_list = [r for r, in my_data]  # create a  list

import tkinter as tk
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

cb1 = customtkinter.CTkComboBox(my_w, values=my_list, width=15)
cb1.grid(row=1, column=1, padx=30, pady=30)
my_w.mainloop()  # Keep the window open