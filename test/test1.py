
import tkinter
import customtkinter

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    frames = {"frame1": None, "frame2": None}

    def frame1_selector(self):
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame2_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def __init__(self):
        super().__init__()
        # self.state('withdraw')
        self.title("Change Frames")

        self.geometry("800x600")

        # contains everything
        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        # buttons to select the frames
        bt_frame1 = customtkinter.CTkButton(left_side_panel, padx=10, pady=10, text="Frame 1", command=self.frame1_selector)
        bt_frame1.grid(row=0, column=0)

        bt_frame2 = customtkinter.CTkButton(left_side_panel, padx=10, pady=10, text="Frame 2", command=self.frame2_selector)
        bt_frame2.grid(row=1, column=0)

        # right side panel -> to show the frame1 or frame 2
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel)
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        App.frames['frame1'] = customtkinter.CTkFrame(fg_color="red")
        bt_from_frame1 = customtkinter.CTkButton(App.frames['frame1'], text="Test 1", command=lambda:print("test 1") )
        bt_from_frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        App.frames['frame2'] = customtkinter.CTkFrame(fg_color="blue")
        bt_from_frame2 = customtkinter.CTkButton(App.frames['frame2'], text="Test 2", command=lambda:print("test 2") )
        bt_from_frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

a = App()
a.mainloop()
