"""Simple program with GUI that download a video from youtube"""
from tkinter import *
from pytube import YouTube

app = Tk()
app.geometry("500x300")
app.resizable(0, 0)
app.title("Youtube video downloader")

Label(app, text="Youtube Video Downloader", font="arial 20 bold").pack()
link = StringVar()
Label(app, text="Paste Link Here:", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(app, width=70, textvariable=link).place(x=32, y=90)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(app, text="DOWNLOADED", font="arial 15").place(x=180, y=210)


Button(app, text="DOWNLOAD", font="arial 15 bold", bg="pale violet red",
       padx=2, command=Downloader).place(x=180, y=150)

if __name__ == '__main__':
	app.mainloop()


