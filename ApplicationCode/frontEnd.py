import tkinter as tk
from tkinter import ttk


def print_alert(msg, root, frame, row, colmn):
    label = ttk.Label(frame, text=msg,
                      font=("Helvetica", 30), anchor="center", foreground="red", background="white")
    label.grid(row=row, column=colmn, columnspan=4, padx=10, pady=10)

    def forget():
        label.grid_forget()

    root.after(4000, forget)


def addLabel(frame, text, row, colmn=1, size=40):
    ttk.Label(frame, text=text, font=("Helvetica", size)).grid(row=row, column=colmn)
