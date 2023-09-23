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
    btn = ttk.Button(frame, text=text, command=action)  # create the btn
    style = ttk.Style()  # create its style var
    style.configure('customised.TButton', font=('Helvetica', size), padding=5, anchor= "e")  # customize the style
    btn.configure(style='customised.TButton')  # Apply the custom style to btn
    btn.grid(row=row, column=colmn)  # appear the btn
def addEntry(frame,row,colmn=1,size=40):
    entry = ttk.Entry(frame, font=("Helvetica", size))
    entry.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return entry

def addPswdEntry(frame,row,colmn=1,size=40,show='*'):
    psw = ttk.Entry(frame, font=("Helvetica", size), show=show)
    psw.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return psw
def LogOut(root,frame,initFrame):
    def initialFrame():
        frame.pack_forget()
        initFrame.pack()
    btn = ttk.Button(frame, text="خروج ", command=initialFrame)  # create the btn
    style = ttk.Style()  # create its style var
    style.configure('btn.TButton', font=('Helvetica', 16), padding=5)  # customize the style
    btn.configure(style='btn.TButton')  # Apply the custom style to btn
    btn.grid(row=0,column=0, padx=0, pady=5)
    btn.grid(sticky="sw")  # appear the btn

