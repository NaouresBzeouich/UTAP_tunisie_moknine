import tkinter as tk
from tkinter import ttk

def HomePage(root, user_name, admin_name):
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

    def addNewUser():
        print("Button to add a new user is clicked !")
        add_user = ttk.Frame(root)
        home.pack_forget()
        import AddUserPage as addUser
        addUser.addingNewUser(add_user, home, root)

    # Create buttons
    adding_inscription_button = ttk.Button(home, text="إضافة مشترك جديد ", command=AddAFarmer)
    view_subscribers_button = ttk.Button(home, text="عرض قائمة المشتركين", command=ViewSubscriberList)

    # Place buttons in the home page
    if user_name == admin_name:         # adding the deletion function for only admin user
        for i in range(5):
            ttk.Label(home, text="\n").grid(row=i)
        adding_inscription_button.grid(row=6, padx=10, pady=10)
        ttk.Label(home, text="\n").grid(row=7)
        view_subscribers_button.grid(row=8, padx=10, pady=10)
        ttk.Label(home, text="\n").grid(row=9)

        delete_a_subscriber_button = ttk.Button(home, text="حذف مشترك ", command=deleteASubscriber)
        delete_a_subscriber_button.grid(row=10, padx=10, pady=10)
        ttk.Label(home, text="\n").grid(row=11)

        add_new_user_button = ttk.Button(home, text=" إضافة حساب جديد ", command=addNewUser)
        add_new_user_button.grid(row=12, padx=10, pady=10)
    else:
        for i in range(7):
            ttk.Label(home, text="\n").grid(row=i)
        adding_inscription_button.grid(row=8, padx=10, pady=10)
        ttk.Label(home, text="\n").grid(row=9)
        view_subscribers_button.grid(row=10, padx=10, pady=10)
        ttk.Label(home, text="\n").grid(row=11)

    # showing the home page
    home.pack()

    # Increase the button size
    ttk.Style().configure("TButton", font=("Helvetica", 30), padding=5, anchor="e")


