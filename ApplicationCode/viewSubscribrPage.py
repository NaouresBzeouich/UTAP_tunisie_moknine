import tkinter as tk
from tkinter import ttk

def SubscriberPage(view,home):
    # function to handle the return the home page
    def return_to_home():
        view.pack_forget()
        home.pack()
    def delete_rows_after(row_index):
        for i in range(row_index + 1, len(grid_cells)):
            for col_index in range(len(grid_cells[i])):
                grid_cells[i][col_index].grid_forget()
        grid_cells[row_index + 1:] = []
    def search():
        delete_rows_after(6)
        excel_data = read_excel_data("subscriberlist.xlsx")
        data =[]

        for i, row_data in enumerate(excel_data):
            test = True
            for j in range(6):
                cell_value = row_data[j]
                if entries[j].get() == '':
                    continue
                else:
                    if entries[j].get() != str(cell_value) :
                        test = False
                        break
            if test:
                data.append(row_data)

        # to show data
        for i, row_data in enumerate(data):
            row_cells = []
            for j, cell_value in enumerate(row_data):
                if j == 6:
                    if cell_value is None:
                        continue
                label = tk.Label(excel_frame, text=str(cell_value))
                label.grid(row=i + 10, column=j+1, padx=10, pady=10)
                row_cells.append(label)
            grid_cells.append(row_cells)
    view.pack(fill="both", expand=True)
    global grid_cells
    grid_cells = []
    canvas = tk.Canvas(view)
    canvas.pack(side="left", fill="both", expand=True)

    # to create the scrollbar in the left
    scrollbar = ttk.Scrollbar(view, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    excel_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=excel_frame, anchor="nw")

    # create a place to do searching
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ", " :النقابات القطاعية"]
    entries = [ttk.Entry(excel_frame, font=("Helvetica", 30)) for _ in range(6)]

    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        row_cells = []
        ttk.Label(excel_frame, text="\t\t", font=("Helvetica", 20)).grid(row=i, column=1)
        ttk.Label(excel_frame, text="\t\t", font=("Helvetica", 20)).grid(row=i, column=2)
        entries[i].grid(row=i, column=3, padx=20, pady=10, sticky="e")
        ttk.Label(excel_frame, text=label, font=("Helvetica", 25), anchor="e").grid(row=i , column=4, padx=20, pady=5, sticky="e")

        row_cells.append(label)
        row_cells.append(entries[i].get())
        grid_cells.append(row_cells)

    # creating buttons
    submit_button = ttk.Button(excel_frame, text="بحث عن المشتركين ", command=search, padding=8)
    submit_button.grid(row=8, column=3, sticky="e")
    ttk.Label(excel_frame, text="\t").grid(row=8, column=4)
    ttk.Label(excel_frame, text="\t").grid(row=8, column=0)
    return_to_home_btn = ttk.Button(excel_frame, text=" الرجوع إلى الصفحة الرئيسية ", command=return_to_home, padding=8)
    return_to_home_btn.grid(row=8, column=1,columnspan=2 ,  pady=20)



    # to show data first row
    row_cells = []
    for i, label in enumerate(labels):
        row_cells.append(label)
        ttk.Label(excel_frame, text=label, relief="solid", borderwidth=1, padding=8, anchor="e", font=("Helvetica", 20)).grid(row=9, column=i+1, pady=20,  sticky="nsew")
    grid_cells.append(row_cells)
    excel_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

def read_excel_data(file_path):
    import openpyxl
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data




