import tkinter
import customtkinter
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo


def open_video():
    vid_player.stop()
    global video_file
    video_file = tkinter.filedialog.askopenfilename(
        filetypes=[('Video', ['*.mp4', '*.avi', '*.mov', '*.mkv', '*gif']), ('All Files', '*.*')])
    if video_file:
        try:
            vid_player.load(video_file)
            vid_player.play()
            progress_slider.set(-1)
            play_pause_btn.configure(text="Pause ||")
        except:
            print("Unable to load the file")


def update_duration(event):
    try:
        duration = int(vid_player.video_info()["duration"])
        progress_slider.configure(from_=-1, to=duration, number_of_steps=duration)
    except:
        pass


def seek(value):
    if video_file:
        try:
            vid_player.seek(int(value))
            vid_player.play()
            vid_player.after(50, vid_player.pause)
            play_pause_btn.configure(text="Play ►")
        except:
            pass


def update_scale(event):
    try:
        progress_slider.set(int(vid_player.current_duration()))
    except:
        pass


def play_pause():
    if video_file:
        if vid_player.is_paused():
            vid_player.play()
            play_pause_btn.configure(text="Pause ||")

        else:
            vid_player.pause()
            play_pause_btn.configure(text="Play ►")


def video_ended(event):
    play_pause_btn.configure(text="Play ►")
    progress_slider.set(-1)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CustomTkinter x TkVideoPlayer.py")

video_file = ''
frame_1 = customtkinter.CTkFrame(master=app, corner_radius=15)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

button_1 = customtkinter.CTkButton(master=frame_1, text="Open Video", corner_radius=8, command=open_video)
button_1.pack(pady=10, padx=10)

vid_player = TkinterVideo(master=frame_1, scaled=True, keep_aspect=True, consistant_frame_rate=True, bg="black")
vid_player.set_resampling_method(1)
vid_player.pack(expand=True, fill="both", padx=10, pady=10)
vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended)

progress_slider = customtkinter.CTkSlider(master=frame_1, from_=-1, to=1, number_of_steps=1, command=seek)
progress_slider.set(-1)
progress_slider.pack(fill="both", padx=10, pady=10)

play_pause_btn = customtkinter.CTkButton(master=frame_1, text="Play ►", command=play_pause)
play_pause_btn.pack(pady=10)

app.mainloop()