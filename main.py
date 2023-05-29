#!/usr/bin/env python3

import tkinter as tk
import sqlalchemy
import time
import imghdr
from PIL import Image, ImageTk
from tkinter import filedialog

def select_image():
    file = filedialog.askopenfilename(
        title='Select image',
        filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    )

    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(center_frame, image=photo)
    label.image = photo
    label.pack()

window = tk.Tk()

window.title("Diary")
# minimum size 800 x 600
window.minsize(1000, 600)

# Create three frames: top, middle, bottom
top_frame = tk.Frame(
    window,
    bg='cyan',
    height=50
)

middle_frame = tk.Frame(
    window,
    bg='gray',
)

bottom_frame = tk.Frame(
    window,
    bg='dark green',
    height=50
)

# Create three vertical frame in the middle frame
left_frame = tk.Frame(
    middle_frame,
    bg='red',
    width=150,
)

center_frame = tk.Frame(
    middle_frame
)

right_frame = tk.Frame(
    middle_frame,
    bg='light gray',
    width=250,
)

button = tk.Button(left_frame, text="Go", command=select_image)

button.pack(fill=tk.X)

# Pack the frames
left_frame.pack(side=tk.LEFT, fill=tk.Y)
center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_frame.pack(side=tk.LEFT, fill=tk.Y)

top_frame.pack(fill=tk.X)
middle_frame.pack(fill=tk.BOTH, expand=True)
bottom_frame.pack(fill=tk.X)

window.mainloop()