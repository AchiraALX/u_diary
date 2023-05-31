#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog


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

# Pack the frames
left_frame.pack(side=tk.LEFT, fill=tk.Y)
center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_frame.pack(side=tk.LEFT, fill=tk.Y)

top_frame.pack(fill=tk.X)
middle_frame.pack(fill=tk.BOTH, expand=True)
bottom_frame.pack(fill=tk.X)

window.mainloop()
