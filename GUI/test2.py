
import customtkinter
import awesometkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

HEIGHT = 250
WIDTH = 370

app = customtkinter.CTk()
app.title("Circular Progress Bar")
app.geometry((f"{WIDTH}x{HEIGHT}"))

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)


def button_function():
    if button_1.text == "Start":
        bar1.start()
        bar2.start()
        button_1.configure(text="Stop")
    else:
        bar1.stop()
        bar2.stop()
        button_1.configure(text="Start")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(padx=10, pady=10)

bar1 = awesometkinter.RadialProgressbar3d(frame_1, fg='green', parent_bg="#2a2d2e", size=(130, 130))
bar1.grid(row=0, column=0, pady=10, padx=20)

bar2 = awesometkinter.RadialProgressbar(frame_1, fg='red', parent_bg="#2a2d2e", size=(120, 120))
bar2.grid(row=0, column=1, pady=10, padx=20)

button_1 = customtkinter.CTkButton(frame_1, width=200, text="Start", command=button_function)
button_1.grid(row=1, columnspan=2, pady=20, padx=20)

app.mainloop()             