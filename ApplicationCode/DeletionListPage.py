import tkinter as tk
from tkinter import ttk
def DeletionList(deleteList, home, rows_to_delete):

    # showing the DeletionList page
    deleteList.pack(pady=10)
    # text for make sure the deletion
    ttk.Label(deleteList, text=" هل أنت متأكد من حذف هؤلاء المشتركين  ",
                                 font=("Helvetica", 50), anchor="center", foreground="red", background="white").grid(row=1, padx=10, pady=10)


