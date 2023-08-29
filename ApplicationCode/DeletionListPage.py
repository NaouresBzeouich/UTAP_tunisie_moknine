import tkinter as tk
from tkinter import ttk
def DeletionList(deleteList, home, rows_to_delete):
    # function to handle the return the home page
    def return_to_home():
        deleteList.pack_forget()
        home.pack()

    # showing the DeletionList page
    deleteList.pack(pady=10)
    if rows_to_delete:
        # text for make sure the deletion
        ttk.Label(deleteList, text=" هل أنت متأكد من حذف هؤلاء المشتركين  ", font=("Helvetica", 50), anchor="center", foreground="red", background="white").grid(row=1, padx=10, pady=10)
        # table contain selected subscriber
        labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ",
                  " :النقابات القطاعية"]
        # to show data first row
        for i, label in enumerate(labels):
            ttk.Label(deleteList, text=label, relief="solid", borderwidth=1, padding=8, anchor="e",
                      font=("Helvetica", 20)).grid(row=9, column=i + 2, pady=20, sticky="nsew")
        print(rows_to_delete)
        # to show deletion data
        grid_cell = []
        for i, row_data in enumerate(rows_to_delete):
            row_cell = []
            for j, cell_value in enumerate(row_data):
                if j == 6:
                    if cell_value is None:
                        continue
                label = tk.Label(deleteList, text=str(cell_value))
                label.grid(row=i + 10, column=j + 2, padx=10, pady=10)
                row_cell.append(label)
            grid_cell.append(row_cell)
    else:
        ttk.Label(deleteList, text=" لا يوجد مشتركين بهذه المعطيات  ", font=("Helvetica", 50), anchor="center", foreground="red", background="white").grid(row=1, padx=10, pady=10)

    # creating return to home button
    submit_button = ttk.Button(deleteList, text=" الرجوع إلى الصفحة الرئيسية ", command=return_to_home)
    submit_button.grid(row=8, columns=1, padx=10, pady=10)

