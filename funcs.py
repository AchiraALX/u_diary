#!/usr/bin/env python3
"""A script to hold the major functions
"""

import tkinter as tk
from tkinter import messagebox
from plyer import notification
from add import Add

add = Add()

class Operations:
    """A stack class
    """

    def __init__(self):
        self.stack = {}

    def push(self, key, value):
        """Add to the stack
        """
        self.stack[key] = value

    def pop(self, key):
        """Remove from the stack
        """
        return self.stack.pop(key)

    def get(self, key):
        """Get a value from the stack
        """
        return self.stack.get(key)

    def get_stack(self):
        """Get the stack
        """
        return self.stack

op = Operations()

# Add user
def add_user():
    """Add a user to the database
    """
    def submit_form():
        """Submit the form
        """
        name = entry_name.get().capitalize()
        username = entry_username.get()

        details = {
            "name": name,
            "username": username
        }
        if add.add_user(**details):
            notification.notify(
                title="Success",
                message=f"{username} added successfully",
            )
            form_dialog.destroy()
            op.push("add_user_status", True)

        else:
            messagebox.showerror(
                title="Error",
                message="Something went wrong"
            )

            op.push("add_user_status", False)



    form_dialog = tk.Toplevel()
    form_dialog.title("Add user")
    # Resize the dialog
    form_dialog.geometry("400x250")

    # Name field
    label_name = tk.Label(
        form_dialog,
        text="Name: ",
        relief="flat"
    )
    label_name.grid(
        row=0,
        column=0,
        pady=5,
    )
    entry_name = tk.Entry(
        form_dialog,
        relief="flat"
    )
    entry_name.grid(
        row=0,
        column=1,
        pady=5,
    )

    # Username field
    label_username = tk.Label(
        form_dialog,
        text="Username: ",
        relief="flat"
    )
    label_username.grid(
        row=1,
        column=0,
        sticky="ew",
        pady=5,
    )
    entry_username = tk.Entry(
        form_dialog,
        relief="flat"
    )
    entry_username.grid(
        row=1,
        column=1,
        sticky="ew",
        pady=5,
    )

    # Add a submit button
    submit_button = tk.Button(
        form_dialog,
        text="Submit",
        command=submit_form,

    )

    submit_button.grid(
        row=3,
        column=0,
        columnspan=2,
        sticky="ew",
    )


# Add an entry
def user_add_entry(username: str, frame: tk.Frame):
    """Add an entry

    Args:
        username (str): username for the currently logged in user
    """

    def submit_form(username: str):
        """Submit the form
        """
        title = entry_title.get()
        body = entry_body.get("1.0", "end-1c")

        details = {
            "title": title,
            "content": body,
            "author_info": username
        }

        obj = add.add_entry(**details)
        if obj:
            notification.notify(
                title="Success",
                message=f"{title} added successfully",
            )

            op.push("add_entry_status", True)
        else:
            messagebox.showerror(
                title="Error",
                message=f"Something went wrong"
            )
            op.push("add_entry_status", False)

    destroy_children(frame)

    # Title field
    label_title = tk.Label(
        frame,
        text="Title: ",
        relief="flat",
        justify='left',
        anchor="w"
    )
    label_title.grid(
        row=0,
        column=0,
        pady=5,
    )

    entry_title = tk.Entry(
        frame,
        relief="flat"
    )
    entry_title.grid(
        row=1,
        column=0,
        pady=5,
        sticky="ew",
    )
    # Body field
    label_body = tk.Label(
        frame,
        text="Body: ",
        relief="flat"
    )
    label_body.grid(
        row=2,
        column=0,
        pady=5,
    )
    entry_body = tk.Text(
        frame,
        relief="flat",
        height=20,
    )

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=lambda: submit_form(username),
    )

    entry_body.grid(
        row=3,
        column=0,
        pady=5,
        sticky="ew",
    )
    submit_button.grid(
        row=4,
        column=0,
        columnspan=4,
        sticky="ew",
    )

# Destroy widgets children
def destroy_children(frame: tk.Frame) -> None:
    """Destroy widgets children

    Args:
        frame (tk.Frame): frame to be used
    """
    for widget in frame.winfo_children():
        widget.destroy()