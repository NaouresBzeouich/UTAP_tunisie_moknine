import tkinter as tk
from tkinter import ttk

def Form_Page(form, root, home):
    # Function to handle the form submission
    def submit_form():
        validation_results = validate_entries(form, entries)
        if all(validation_results.values()):
            data = [entry.get() for entry in entries]
            save_to_excel(data)
            print("Form submitted!")
            form.pack_forget()
            home.pack()
        else:
            print("Form validation failed. Please check your inputs.")

    # showing the form page
    form.pack(pady=10)
    # Create labels and entry fields for the form
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ", " : تخصص"]
    entries = [tk.Entry(form) for _ in range(6)]
    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        ttk.Label(form, text=label).grid(row=i, column=2, padx=20, pady=5)
        entries[i].grid(row=i, column=1, padx=10, pady=5)
    # creating submit button
    submit_button = ttk.Button(form, text=" تسجيل المشترك ", command=submit_form)
    submit_button.grid(row=8, columnspan=3, padx=10, pady=10)

# Validation function input (8-digit number)
def validate_number(input_value):
    if input_value.isdigit() and len(input_value) == 8:
        return True
    return False


# Validation function input (choices)
def validate_choice_speciality(input_value):
    # List of allowed choices
    choices = ["Option 1", "Option 2", "Option 3"]
    if input_value in choices:
        return True
    return False


# Function to validate all entries
def validate_entries(form, entries):
    validation_results = {}

    for i, entry in enumerate(entries):
        validation_results[i] = True

    validation_results[2] = validate_number(entries[2].get())
    validation_results[3] = validate_number(entries[3].get())
    validation_results[5] = validate_choice_speciality(entries[5].get())

    if validation_results[3]:
        tk.Label(form, text="                                                                 ").grid(row=3, column=0,
                                                                                                      padx=10, pady=5)
    else:
        tk.Label(form, text="رقم هاتف خاطئ يرجى إعادة التحقق منه ").grid(row=3, column=0, padx=10, pady=5)
    if validation_results[2]:
        tk.Label(form, text="                                                                     ").grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
    else:
        tk.Label(form, text="رقم البطاقة الوطنية خاطئ يرجى إعادة التحقق منه ").grid(row=2, column=0, padx=10, pady=5)
    if validation_results[5]:
        tk.Label(form, text="                                                     ").grid(row=5, column=0, padx=10,
                                                                                          pady=5)
    else:
        tk.Label(form, text="التخصص غير مبرمج بالشبكة").grid(row=5, column=0, padx=10, pady=5)
    if entries[0].get() == "":
        tk.Label(form, text="خانة الاسم إلزامية").grid(row=0, column=0, padx=10, pady=5)
    else:
        tk.Label(form, text="                               ").grid(row=0, column=0, padx=10, pady=5)
    if entries[1].get() == "":
        tk.Label(form, text="خانة اللقب إلزامية").grid(row=1, column=0, padx=10, pady=5)
    else:
        tk.Label(form, text="                                ").grid(row=1, column=0, padx=10, pady=5)

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
