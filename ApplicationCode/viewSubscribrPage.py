import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import frontEnd as fe
import outputInputXlFile as xl


def SubscriberPage(view, home):
    def delete_rows_after():
        for i in range( len(grid_cells)):
            for col_index in range(len(grid_cells[i])):
                grid_cells[i][col_index].grid_forget()
        grid_cells[ 1:] = []

    def search():
        if not os.path.exists('subscriberlist.xlsx'):
            messagebox.showerror("خطأ", "لا يوجد أي إشتراك في القائمة . قم بإضافة المشترك أولا ! ")
            fe.return_to_home(home,view)
        else:
            entries = [entriesDectionary[1][i].get() for i in range(5)]
            entries.append(entriesDectionary[2].get())
            if entriesDectionary[2].get() == "الماشية":
                entries.append(entriesDectionary[3].get())
            else:
                entries.append("")
            delete_rows_after()
            excel_data = xl.read_excel_data("subscriberlist.xlsx")
            data = []

            for i, row_data in enumerate(excel_data):
                test = True
                for j, cell_value in enumerate(row_data):
                    if entries[j] == '':
                        continue
                    else:
                        if entries[j] != str(cell_value):
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
                    label.grid(row=i + 10, column=j + 2, padx=10, pady=10)
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

    entriesDectionary = fe.form(excel_frame)
    # creating buttons
    submit_button = fe.addBttn(excel_frame,search,"بحث عن المشتركين ",8,5)
    def go_home():
        fe.return_to_home(home, view)
    return_to_home_btn = fe.addBttn(excel_frame,go_home," الرجوع إلى الصفحة الرئيسية ",8,2,40,2)

    # to show data first row
    for i, label in enumerate([": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ",
              " :النقابات القطاعية"]):
        fe.addLabel(excel_frame,label,9,i+2,20)
    excel_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
