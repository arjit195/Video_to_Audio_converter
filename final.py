from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import moviepy.editor as me
from tkinter import messagebox

filename = ''

def convert():
    global filename
    if filename:
        filetypes = (("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("OGG files", "*.ogg"), ("All files", "*.*"))
        video = me.VideoFileClip(filename)
        audio = video.audio
        file = asksaveasfilename(defaultextension=format.get(), filetypes=filetypes)
        if file:
            audio.write_audiofile(file)
            messagebox.showinfo("Success", "Audio conversion completed successfully!")
            label5.config(text="Done", foreground="green")
        else:
            messagebox.showwarning("Cancelled", "File save operation was cancelled.")
    else:
        messagebox.showerror("Error", "Please select a video file first.")

def select():
    global filename
    filetypes = (
        ('Video files', '*.mp4 *.avi *.mov *.wmv *.flv *.mkv'),
        ('All files', '*.*')
    )
    filename = askopenfilename(filetypes=filetypes)
    if filename:
        label3.config(text="File Selected", foreground="green")
        label4.pack(pady=5)  # Show label4
        menu.pack(pady=5)    # Show format menu
        button3.pack(pady=10) # Show Export button
    else:
        label3.config(text="No file selected", foreground="red")

root = Tk()
root.geometry("600x400")
root.minsize(600, 400)
root.maxsize(600, 400)
root.title("Video to Audio Converter")

# Background frame
frame = Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame.pack(expand=True, fill=BOTH)

label1 = Label(frame, text="Video to Audio Converter", font=("Arial", 24, "bold"), bg="#f0f0f0")
label1.pack(pady=10)

label2 = Label(frame, text="Select Video file to Convert", bg="#f0f0f0", font=("Arial", 14))
label2.pack(pady=5)

button1 = Button(frame, text="Select Video", command=select, font=("Arial", 10), padx=8, pady=4)
button1.pack(pady=5)

label3 = Label(frame, text="", font=("Arial", 12), bg="#f0f0f0")
label3.pack(pady=5)

label4 = Label(frame, text="Select Audio format:", bg="#f0f0f0", font=("Arial", 14))

format = StringVar(value=".mp3")
options = [".mp3", ".wav", ".ogg"]
menu = OptionMenu(frame, format, *options)

button3 = Button(frame, text="Export", command=convert, font=("Arial", 10), padx=8, pady=4)

label5 = Label(frame, text="", font=("Arial", 14), bg="#f0f0f0")

# Adjust layout
label4.pack(pady=5)
menu.pack(pady=5)
button3.pack(pady=10)
label5.pack(pady=10)

root.mainloop()
