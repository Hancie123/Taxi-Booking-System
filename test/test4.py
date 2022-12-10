import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

HEIGHT = 200
WIDTH = 300

app = customtkinter.CTk()
app.title("Dynamic Entry")
app.geometry((f"{WIDTH}x{HEIGHT}"))

label_1 = customtkinter.CTkLabel(master=app, text="Multiply 2 numbers")
label_1.pack(pady=10, padx=10)


def calculate(var, index, mode):
    if entry_1.get() != "" and entry_2.get() != "":
        label_2.configure(text="Total: " + str(int(entry_1.get()) * int(entry_2.get())))
    else:
        label_2.configure(text="Total: --")


def only_numbers(char):
    # Validate for numbers only
    if ((char.isdigit()) or (char == "")):
        return True
    else:
        return False


validation = app.register(only_numbers)

# Make two Interget variables
var1 = tkinter.StringVar()
var2 = tkinter.StringVar()

entry_1 = customtkinter.CTkEntry(master=app, textvariable=var1, validate='key', validatecommand=(validation, '%P'))
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=app, textvariable=var2, validate='key', validatecommand=(validation, '%P'))
entry_2.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=app, text="Total: 0")
label_2.pack(pady=10, padx=10)

# Trace the variables
var1.trace_add('write', calculate)
var2.trace_add('write', calculate)

app.mainloop()          