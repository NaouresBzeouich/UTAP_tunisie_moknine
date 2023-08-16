import tkinter as tk
from tkinter import ttk

def SubscriberPage(view):
    def search():
        excel_data = read_excel_data("subscriberlist.xlsx")
        # to show data
        for i, row_data in enumerate(excel_data):
            for j, cell_value in enumerate(row_data):
                label = tk.Label(excel_frame, text=str(cell_value))
                label.grid(row=i + 10, column=j, padx=10, pady=10)

    view.pack(fill="both", expand=True)

    canvas = tk.Canvas(view)
    canvas.pack(side="left", fill="both", expand=True)
    # to create the scrollbar in the left
    scrollbar = ttk.Scrollbar(view, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    excel_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=excel_frame, anchor="nw")
    # create a place to do searching
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ", " : تخصص"]
    entries = [tk.Entry(excel_frame) for _ in range(6)]
    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        ttk.Label(excel_frame, text=label).grid(row=i , column=2, padx=20, pady=5)
        entries[i].grid(row=i, column=1, padx=10, pady=5)
    # creating search button
    submit_button = ttk.Button(excel_frame, text="بحث عن المشتركين ", command=search)
    submit_button.grid(row=8, columnspan=3, padx=10, pady=10)
    # to show data first row
    for i, label in enumerate(labels):
        ttk.Label(excel_frame, text=label).grid(row=9, column=i, padx=20, pady=5)
    excel_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

def read_excel_data(file_path):
    import openpyxl
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data

