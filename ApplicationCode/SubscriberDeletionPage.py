import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
def SubscriberDeletion(delete, home, root):
    # function to the button delete subscriber
    def delete_subscriber():
        if not os.path.exists('subscriberlist.xlsx'):
            messagebox.showerror("خطأ", "لا يوجد أي إشتراك في القائمة . قم بإضافة المشترك أولا ! ")
            return_to_home()
        else:
            # saving the entries
            data = [entry.get() for entry in entries]
            data.append(combobox.get())
            if combobox.get() == "الماشية":
                data.append(cattle_combobox.get())
            else:
                data.append("")
                # test if there's subscriber with same details
                rows_to_delete = []
                excel_data = read_excel_data("subscriberlist.xlsx")
                row_number = 0
                for i, row_data in enumerate(excel_data):
                    test = True
                    for j in range(7):
                        cell_value = row_data[j]
                        if data[j] == '':
                            continue
                        else:
                            if data[j] != str(cell_value):
                                test = False
                                break
                    if test:
                        row_number += 1
                        rows_to_delete.append(row_data)
                # creating the new frame that contains subscriber list to delete
                deleteList = ttk.Frame(root)
                # hiding the delete page which is the current page
                delete.pack_forget()
                # calling the function deleteList from the file viewSubscriberPage
                import DeletionListPage as dl
                dl.DeletionList(root, deleteList, home, rows_to_delete, row_number)

    # function for selecting the type of cattle
    def cattle_select(event):
        option = selected_option.get()
        print("combobox selected")
        # Check if the selected option is "op1"
        if option == "الماشية":
            print("option cattle selected")
            cattle_combobox.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="e")
        else:
            cattle_combobox.grid_forget()

    # function to handle the return the home page
    def return_to_home():
        delete.pack_forget()
        home.pack()

    # showing the SubscriberDeletion page
    delete.pack(pady=10)
    # Create labels and entry fields
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ",
              " :النقابات القطاعية"]
    entries = [ttk.Entry(delete, font=("Helvetica", 30)) for _ in range(5)]
    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        ttk.Label(delete, text="\t\t", font=("Helvetica", 20)).grid(row=i + 2, column=1)
        if label == " :النقابات القطاعية":
            # Create a Combobox
            selected_option = tk.StringVar()
            combobox = ttk.Combobox(delete, textvariable=selected_option, font=("Helvetica", 30))
            combobox["values"] = ("الزياتين", "النحل", "السقوي", "الماشية", "الصيد الساحلي", "الصيد بالأضواء")
            combobox.grid(row=i, column=2, padx=20, pady=30, sticky="e")
        else:
            entries[i].grid(row=i, column=2, padx=20, pady=30, sticky="e")
        ttk.Label(delete, text=label, font=("Helvetica", 25), anchor="e").grid(row=i, column=3, padx=20, pady=5,
                                                                               sticky="e")
    # Create a Combobox for specifying the type of cattle
    cattle_selected_option = tk.StringVar()
    cattle_combobox = ttk.Combobox(delete, textvariable=cattle_selected_option, font=("Helvetica", 30))
    cattle_combobox["values"] = ("الأغنام", "الأبقار")

    # Bind the event handler to the cattle selection
    combobox.bind("<<ComboboxSelected>>", cattle_select)

    # creating submit button
    submit_button = ttk.Button(delete, text=" حذف المشترك ", command=delete_subscriber)
    submit_button.grid(row=8, column=2, padx=10, pady=10)
    # creating return to home button
    submit_button = ttk.Button(delete, text=" الرجوع إلى الصفحة الرئيسية ", command=return_to_home)
    submit_button.grid(row=8, columns=1, padx=10, pady=10)


def read_excel_data(file_path):
    import openpyxl
    data = []
    if os.path.exists('subscriberlist.xlsx'):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)
    return data
