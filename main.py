from pytube import YouTube
from tkinter import *
from tkinter import ttk
import os

window = Tk()
window.title("YoutubeDownloader")
window.geometry("400x300+500+200")
window.resizable(0, 0)

def download():
    filename = fval.get()
    video = YouTube(val.get())

    Label(window, text="DOWNLOADED", fg="green", font=("Helvetica", 10)).place(x=160, y=245)
    if drop.get() == "Highest" and drop1.get() == "Mp4":
        video = video.streams.get_highest_resolution()
        video.download("C:\\Users\\Dell\\Downloads", filename=filename)
    elif drop.get() == "Highest" and drop1.get() == "Mp3":
        video = video.streams.get_audio_only()
        video.download("C:\\Users\\Dell\\Downloads",filename=filename)
        os.rename(f'C:\\Users\\Dell\\Downloads\\{filename}.mp4', f'C:\\Users\\Dell\\Downloads\\{filename}.mp3')
    elif drop.get() == "Lowest" and drop1.get() == "Mp3":
        video = video.streams.get_audio_only()
        video.download("C:\\Users\\Dell\\Downloads",filename=filename)
        os.rename(f'C:\\Users\\Dell\\Downloads\\{filename}.mp4', f'C:\\Users\\Dell\\Downloads\\{filename}.mp3')
    else:
        video = video.streams.get_lowest_resolution()
        video.download("C:\\Users\\Dell\\Downloads")

#title
title = Label(window,
              text="YoutubeVideoDownloader",
              font=("Helvetica", 20, "bold"),
              fg="red",
              width=400,
              anchor=CENTER).pack()

#text
text1 = Label(window, text="----------------------------------------------------------------",
              font=("Helvetica", 18), fg="gray").place(x=0, y=30)
text2 = Label(window, text="Video Url:", font=("Helvetica", 12, "bold"), fg="red").place(x=43, y=70)
text3 = Label(window, text="Resolution:", font=("Helvetica", 12, "bold"), fg="red").place(x=43, y=100)
text4 = Label(window, text="Format:", font=("Helvetica", 12, "bold"), fg="red").place(x=43, y=128)
text5 = Label(window, text="Filename:", font=("Helvetica", 12, "bold"), fg="red").place(x=43, y=158)
text6 = Label(window, text="note: same named file will be overwritten.",
              font=("Helvetica", 10,), fg="red").place(x=43, y=180)

#entry
val = StringVar()
url = Entry(window,textvariable=val, font=("Helvetica", 10), fg="black", width=35, bd=2).place(x=137, y=71)
fval = StringVar()
fname = Entry(window,textvariable=fval, font=("Helvetica", 10), fg="black", width=25, bd=2).place(x=137, y=160)

#combobox
drop = StringVar()
value = drop.get()
combobox = ttk.Combobox(window,textvariable=drop,state= "readonly")
combobox['values'] = ('Lowest','Highest')
combobox.current(1)
combobox.place(x=137, y=102)

#combobox2
drop1 = StringVar()
value1 = drop1.get()
combobox1 = ttk.Combobox(window,textvariable=drop1,state= "readonly")
combobox1['values'] = ('Mp3','Mp4')
combobox1.current(1)
combobox1.place(x=137, y=130)

#btn
downloadbtn = Button(window, text="Download",font=("Helvetica", 13, "bold"),bd=4, fg="green",
                     command=download).place(x=150, y=200)

window.mainloop()