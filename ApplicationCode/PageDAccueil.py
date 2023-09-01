import tkinter as tk
from tkinter import ttk

def HomePage(root):
    # creating home page frame
    home = ttk.Frame(root)

    # creating the command to the buttoms
    def AddAFarmer():
        # to make sure that everything is okkey
        print("Button to add a subscriber is clicked !")
        # creating the form page
        form = ttk.Frame(root)
        # hiding the home page which is the current page
        home.pack_forget()
        # calling the function FormPage from the file formPage
        import formPage as fp
        fp.Form_Page(form, root, home)

    def ViewSubscriberList():
        # to make sure that everything is okkey
        print("Button to view subscriber list is clicked !")
        # creating the subscriber list page
        view = ttk.Frame(root)
        # hiding the home page which is the current page
        home.pack_forget()
        # calling the function ViewSubscriberPage from the file viewSubscriberPage
        import viewSubscribrPage as vp
        vp.SubscriberPage(view,home)

    def deleteASubscriber():
        # to make sure that everything is okkey
        print("Button to delete a subscriber is clicked !")
        # creating the subscriber deletion page
        delete = ttk.Frame(root)
        # hiding the home page which is the current page
        home.pack_forget()
        # calling the function ViewSubscriberPage from the file viewSubscriberPage
        import SubscriberDeletionPage as sp
        sp.SubscriberDeletion(delete, home,root)
    # Create buttons
    AddingInscriptionButton = ttk.Button(home, text="إضافة مشترك جديد ", command=AddAFarmer)
    ViewSubscribersButton = ttk.Button(home, text="عرض قائمة المشتركين", command=ViewSubscriberList)
    deleteASubscriberButton = ttk.Button(home, text="حذف مشترك ", command=deleteASubscriber)

    # Place buttons in the home page
    for i in range(7):
        ttk.Label(home, text="\n").grid(row=i)
    AddingInscriptionButton.grid(row=8, padx=10, pady=10)
    ttk.Label(home, text="\n").grid(row=9)
    ViewSubscribersButton.grid(row=10, padx=10, pady=10)
    ttk.Label(home, text="\n").grid(row=11)
    deleteASubscriberButton.grid(row=12, padx=10, pady=10)

    # showing the home page
    home.pack()

    # Increase the button size
    ttk.Style().configure("TButton", font=("Helvetica", 30), padding=5, anchor="e")


