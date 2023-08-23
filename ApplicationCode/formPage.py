import tkinter as tk
from tkinter import ttk
def Form_Page(form, root, home):
    #function to handle the return the home page
    def return_to_home():
        form.pack_forget()
        home.pack()
    # Function to handle the form submission
    def submit_form():
        validation_results = validate_entries(form, entries, selected_option)
        if all(validation_results.values()):
            data = [entry.get() for entry in entries]
            data.append(combobox.get())
            save_to_excel(data)
            print("Form submitted!")
            return_to_home()
        else:
            print("Form validation failed. Please check your inputs.")

    # function for selecting the type of cattle
    def cattle_select(event):
        option = selected_option.get()
        print("combobox selected")
        # Check if the selected option is "op1"
        if option == "الماشية":
            print("option cattle selected")
            cattle_combobox.grid(row=5, column=1, padx=20, pady=30, sticky="e")
        else:
            cattle_combobox.grid_forget()

    # showing the form page
    form.pack(pady=10)
    # Create labels and entry fields for the form
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ", " :النقابات القطاعية"]
    entries = [ttk.Entry(form, font=("Helvetica", 30)) for _ in range(5)]
    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        ttk.Label(form, text="\t\t", font=("Helvetica", 20)).grid(row=i+2, column=1)
        if label == " :النقابات القطاعية":
            # Create a Combobox
            selected_option = tk.StringVar()
            combobox = ttk.Combobox(form, textvariable=selected_option, font=("Helvetica", 30))
            combobox["values"] = ( "الزياتين", "النحل", "السقوي" , "الماشية" , "الصيد الساحلي" , "الصيد بالأضواء")
            combobox.grid(row=i, column=2, padx=20, pady=30, sticky="e")
        else:
            entries[i].grid(row=i, column=2, padx=20, pady=30, sticky="e")
        ttk.Label(form, text=label, font=("Helvetica", 25), anchor="e").grid(row=i, column=3, padx=20, pady=5,
                                                                                    sticky="e")
    # Create a Combobox for specifying the type of cattle
    cattle_selected_option = tk.StringVar()
    cattle_combobox = ttk.Combobox(form, textvariable=cattle_selected_option, font=("Helvetica", 30))
    cattle_combobox["values"] = ("الماشية", "الأبقار")

    # Bind the event handler to the cattle selection
    combobox.bind("<<ComboboxSelected>>", cattle_select)

    # creating submit button
    submit_button = ttk.Button(form, text=" تسجيل المشترك ", command=submit_form)
    submit_button.grid(row=8, column=2, padx=10, pady=10)
    # creating return to home button
    submit_button = ttk.Button(form, text=" الرجوع إلى الصفحة الرئيسية ", command=return_to_home)
    submit_button.grid(row=8, columns=1, padx=10, pady=10)
# Validation function input (8-digit number)
def validate_number(input_value):
    if input_value.isdigit() and len(input_value) == 8:
        return True
    return False


# Validation function input (choices)
def validate_choice_speciality(input_value):
    # List of allowed choices
    choices = [ "الزياتين", "النحل", "السقوي" , "الماشية" , "الصيد الساحلي" , "الصيد بالأضواء" ]
    if input_value in choices:
        return True
    return False


# Function to validate all entries
def validate_entries(form, entries, selected_option):
    validation_results = {}

    for i in range(6):
        validation_results[i] = True

    validation_results[2] = validate_number(entries[2].get())
    validation_results[3] = validate_number(entries[3].get())
    validation_results[5] = validate_choice_speciality(selected_option.get())

    if validation_results[3]:
        tk.Label(form, anchor="e", text="                                                                 ").grid(row=3, column=1, sticky="e")
    else:
        tk.Label(form, anchor="e", text="رقم هاتف خاطئ يرجى إعادة التحقق منه ").grid(row=3, column=1, sticky="e")
    if validation_results[2]:
        tk.Label(form, anchor="e", text="                                                                     ").grid(row=2, column=1, sticky="e")
    else:
        tk.Label(form, anchor="e", text="رقم البطاقة الوطنية خاطئ يرجى إعادة التحقق منه ").grid(row=2,  column=1, sticky="e")
    if validation_results[5]:
        tk.Label(form, anchor="e", text="                                                     ").grid(row=5, column=1, sticky="e")
    else:
        tk.Label(form, anchor="e", text="التخصص غير مبرمج بالشبكة").grid(row=5, column=1, sticky="e")
    if entries[0].get() == "":
        tk.Label(form, anchor="e", text="خانة الاسم إلزامية").grid(row=0, column=1, sticky="e")
    else:
        tk.Label(form, anchor="e", text="                               ").grid(row=0, column=1, sticky="e")
    if entries[1].get() == "":
        tk.Label(form, anchor="e", text="خانة اللقب إلزامية").grid(row=1, column=1, sticky="e")
    else:
        tk.Label(form, anchor="e", text="                                ").grid(row=1, column=1, sticky="e")

    return validation_results

# Function to save data to Excel
def save_to_excel(data):
    from openpyxl import Workbook
    from openpyxl import load_workbook
    import os
    if os.path.exists('subscriberlist.xlsx'):
        wb = load_workbook('subscriberlist.xlsx')
        ws = wb.active
    else:
        print("erreur the document excel not found :( ")
        exit(1)

    ws.append(data)
    wb.save('subscriberlist.xlsx')
