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

def addBttn(frame,action,text,row,colmn=1,size=40):
    # creating a btn to go to home page
    submit_button = ttk.Button(frame, text=text, command=action)
    submit_button.grid(row=row, column=colmn, columnspan=2, padx=10, pady=10)
    # Increase the button size
    ttk.Style().configure("TButton", font=("Helvetica", size), padding=5, anchor="e")

def addEntry(frame,row,colmn=1,size=40):
    entry = ttk.Entry(frame, font=("Helvetica", size))
    entry.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return entry

def addPswdEntry(frame,row,colmn=1,size=40,show='*'):
    psw = ttk.Entry(frame, font=("Helvetica", size), show=show)
    psw.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return psw
