import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")

tk.Label(root, text="Enter YouTube Video URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

root.mainloop()
