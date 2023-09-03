import tkinter as tk
from tkinter import ttk
def addingNewUser(add_user, home, root):

    #function to handle the return the home page
    def return_to_home():
        add_user.pack_forget()
        home.pack()

    # creating user and password labels and entries
    for i in range(2):
        ttk.Label(add_user, text="\n", font=("Helvetica", 30)).grid(row=i, column=3)

    ttk.Label(add_user, text=": الإسم  ", font=("Helvetica", 30)).grid(row=5, column=3)
    name = ttk.Entry(add_user, font=("Helvetica", 30))
    name.grid(row=5, column=2, padx=20, pady=30, sticky="e")

    ttk.Label(add_user, text=": الرمز السرِّي   ", font=("Helvetica", 30)).grid(row=6, column=3)
    psw = ttk.Entry(add_user, font=("Helvetica", 30), show='*')
    psw.grid(row=6, column=2, padx=20, pady=30, sticky="e")

    ttk.Label(add_user, text=": التأكد من الرمز السرِّي   ", font=("Helvetica", 30)).grid(row=6, column=3)
    psw = ttk.Entry(add_user, font=("Helvetica", 30), show='*')

    ttk.Label(add_user, text="\n", font=("Helvetica", 30)).grid(row=7, column=3)

    # creating a btn to return to home page
    submit_button = ttk.Button(add_user, text="  الرجوع إلى الصفحة الرئيسية  ", command=return_to_home)
    submit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    # creating a btn to return to home page
    submit_button = ttk.Button(add_user, text="  إضافة الحساب   ", command=return_to_home)
    submit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)
    add_user.pack()