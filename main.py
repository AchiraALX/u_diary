#!/usr/bin/env python3

import tkinter as tk
from tkinter.font import Font
from tkinter import (
    filedialog,
    ttk
)
from query import main
from plyer import notification
from funcs import *
import time

users = main('users')
entries = main('entries')
comments = main('comments')
fg_colors = {
    'kombu': '#354230',
    'title': '#29AB87'
}

bg_colors = {
    'honeydew': '#F0FFF0',
    'tea': '#D0F0C0'
}

def reload_data():
    global users
    global entries
    global comments

    users = main('users')
    entries = main('entries')
    comments = main('comments')

def available_users() -> list:
    global users

    available_users = []
    for user in users['users']:
        available_users.append(user['username'])

    return available_users

# List the entries in the center_frame
default_user = available_users()[0]
def list_entries(user: str = default_user ):
    global entries
    global fg_colors
    global bg_colors

    destroy_children(center_frame)

    for entry in entries['entries']:
        if entry['user'] == user:
            entry_frame = tk.Frame(
                center_frame,
                bg='#F0FFF0',
                highlightbackground=bg_colors['tea'],
                highlightthickness=3
            )

            entry_title = tk.Label(
                entry_frame,
                text=entry['title'],
                font=Font(family='Arial', size=14, weight='bold'),
                bg='#F0FFF0',
                fg='#29AB87',
                justify='left',
                anchor='w'
            )

            entry_body = tk.Label(
                entry_frame,
                text=entry['content'],
                font=('Montserrat', 12),
                fg=fg_colors['kombu'],
                bg=bg_colors['honeydew'],
                wraplength=500,
                justify='left',
                anchor='w'
            )

            entry_title.grid(
                row=0,
                column=0,
                sticky='nsew'
            )
            entry_body.grid(
                row=1,
                column=0,
                sticky='nsew'
            )
            entry_frame.pack(
                fill=tk.X,
                ipadx=105,
                ipady=5
            )

    # Add a button to add an  entry
    add_entry_button = tk.Button(
        center_frame,
        text="Add entry",
        font=('Montserrat', 12),
        bg=bg_colors['honeydew'],
        fg=fg_colors['kombu'],
        relief='flat',
        command=lambda: user_add_entry(user, center_frame)
    )
    add_entry_button.pack(
        fill=tk.X,
        ipadx=105,
        ipady=5
    )

def on_user_select(event):
    selected_user = user_button.get()
    list_entries(selected_user)

def show_add_user():
    add_user()
    available_users()

def home():
    reload_data()
    list_entries(user_button.get())

def add_entry_and_reload():
    if op.get_stack() == {}:
        print("Empty stack")
        op.push("add_entry_status", False)

    status = op.get("add_entry_status")
    user = user_button.get()
    while not status:
        user_add_entry(user, center_frame)
        status = op.get("add_entry_status")

    home()

window = tk.Tk()

window.title("Diary")
# minimum size 800 x 600
width = 1000
height = 600

window.minsize(width, height)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

window.geometry(f"{width}x{height}+{x}+{y}")

# Combobox style
style = ttk.Style()
style.configure(
    "TCombobox",
    relief="solid",
    boderwidth=1
)

# Create three frames: top, middle, bottom
# Top frame
top_frame = tk.Frame(
    window,
    bg='cyan',
    height=80
)
top_frame.columnconfigure(1, weight=1)

# Middle frame
middle_frame = tk.Frame(
    window,
    bg='gray',
)

# Bottom Frame
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
center_frame.columnconfigure(0, weight=1)

right_frame = tk.Frame(
    middle_frame,
    bg='light gray',
    width=250,
)

# Pack the frames
left_frame.pack(side=tk.LEFT, fill=tk.Y)
center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_frame.pack(side=tk.LEFT, fill=tk.Y)

top_frame.pack(
    fill=tk.X
)
middle_frame.pack(fill=tk.BOTH, expand=True)
bottom_frame.pack(fill=tk.X)

# List the entries by default user
list_entries()

# A combo box to select and change user
user_list = available_users()
user_button = ttk.Combobox(
    top_frame,
    values=user_list,
)
user_button.grid(
    row=0,
    column=1,
    pady=5
)
user_button.bind("<<ComboboxSelected>>", on_user_select)
user_button.current(0)

# Button to add user
add_user_button = tk.Button(
    top_frame,
    text="Add user",
    command=show_add_user
)
add_user_button.grid(
    row=0,
    column=2,
    padx=5,
)

# Home button
home_button = tk.Button(
    top_frame,
    text="Home",
    command=home
)
home_button.grid(
    row=0,
    column=0,
    padx=5,
)

window.mainloop()
