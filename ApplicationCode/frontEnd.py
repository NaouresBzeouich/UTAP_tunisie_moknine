import tkinter as tk
from tkinter import ttk


def print_alert(msg, root, frame, row, colmn):
    label = ttk.Label(frame, text=msg,
                      font=("Helvetica", 30), anchor="center", foreground="red", background="white")
    label.grid(row=row, column=colmn, columnspan=4, padx=10, pady=10)

    def forget():
        label.grid_forget()

    root.after(4000, forget)


def addLabel(frame, text, row, colmn=1, size=40):
    ttk.Label(frame, text=text, font=("Helvetica", size)).grid(row=row, column=colmn)


def addBttn(frame, action, text, row, colmn=1, size=40, columnspan = 1):
    btn = ttk.Button(frame, text=text, command=action)  # create the btn
    style = ttk.Style()  # create its style var
    style.configure('customised.TButton', font=('Helvetica', size), padding=5, anchor="e")  # customize the style
    btn.configure(style='customised.TButton')  # Apply the custom style to btn
    btn.grid(row=row, column=colmn, columnspan= columnspan)  # appear the btn


def addEntry(frame, row, colmn=1, size=40):
    entry = ttk.Entry(frame, font=("Helvetica", size))
    entry.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return entry


def addPswdEntry(frame, row, colmn=1, size=40, show='*'):
    psw = ttk.Entry(frame, font=("Helvetica", size), show=show)
    psw.grid(row=row, column=colmn, padx=20, pady=30, sticky="e")
    return psw


def LogOut(root, frame, initFrame):
    def initialFrame():
        frame.pack_forget()
        initFrame.pack()

    btn = ttk.Button(frame, text="خروج ", command=initialFrame)  # create the btn
    style = ttk.Style()  # create its style var
    style.configure('btn.TButton', font=('Helvetica', 16), padding=5)  # customize the style
    btn.configure(style='btn.TButton')  # Apply the custom style to btn
    btn.grid(row=0, column=0, padx=0, pady=5)
    btn.grid(sticky="sw")  # appear the btn


# function to handle the return the home page
def return_to_home(home, frame):
    frame.pack_forget()
    home.pack()


def form(frame):
    # function for selecting the type of cattle
    def cattle_select(event):
        option = selected_option.get()
        # Check if the selected option is "الماشية"
        if option == "الماشية":
            cattle_combobox.grid(row=5, column=2, columnspan=2, padx=20, pady=10, sticky="e")
        else:
            cattle_combobox.grid_forget()

    # create a place to do searching
    tk.Label(frame, text="\t\t").grid(row=0, column=1, padx=10, pady=10)
    labels = [": اسم ", ": اللقب ", " : رقم بطاقة الهوية الوطنية ", ": رقم الهاتف ", " : المنطقة ",
              " :النقابات القطاعية"]
    entries_writed = [ttk.Entry(frame, font=("Helvetica", 30)) for _ in range(5)]

    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        row_cells = []
        ttk.Label(frame, text=label, font=("Helvetica", 25), anchor="e").grid(row=i, column=6, columnspan=2,
                                                                              padx=20, pady=5,
                                                                              sticky="e")
        if i < 5:
            entries_writed[i].grid(row=i, column=4, columnspan=2, padx=20, pady=10, sticky="e")
        else:
            # Create a Combobox
            selected_option = tk.StringVar()
            combobox = ttk.Combobox(frame, textvariable=selected_option, font=("Helvetica", 30))
            combobox["values"] = ("الزياتين", "النحل", "السقوي", "الماشية", "الصيد الساحلي", "الصيد بالأضواء")
            combobox.grid(row=i, column=4, columnspan=2, padx=20, pady=10, sticky="e")

    # Create a Combobox for specifying the type of cattle
    cattle_selected_option = tk.StringVar()
    cattle_combobox = ttk.Combobox(frame, textvariable=cattle_selected_option, font=("Helvetica", 30))
    cattle_combobox["values"] = ("الأغنام", "الأبقار")

    # Bind the event handler to the cattle selection
    combobox.bind("<<ComboboxSelected>>", cattle_select)

    return {1: entries_writed, 2: combobox, 3: cattle_combobox}
