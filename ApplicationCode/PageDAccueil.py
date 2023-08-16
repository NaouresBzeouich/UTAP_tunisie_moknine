import tkinter as tk
from tkinter import ttk

def HomePage():
    # Create the main window
    root = tk.Tk()
    # Adding a title to the main window
    root.title("UTAO tunisie moknine ")
    # Setting dimensions (width x height)
    root.geometry("800x600")
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
        vp.SubscriberPage(view)

    # Create buttons
    AddingInscriptionButton = ttk.Button(home, text="إضافة مشترك جديد ", command=AddAFarmer)
    ViewSubscribersButton = ttk.Button(home, text="عرض قائمة المشتركين", command=ViewSubscriberList)

    # Place buttons in the home page
    AddingInscriptionButton.pack(pady=20)
    ViewSubscribersButton.pack()
    # showing the home page
    home.pack()
    # Start the GUI event loop
    root.mainloop()
