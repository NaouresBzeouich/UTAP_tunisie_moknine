import tkinter as tk
from tkinter import ttk
import __init__ as init
def addingNewUser(add_user, home, root):
    # function to add a user to the userList
    def add_user_to_list(user_name, password):
        data = [user_name, password]
        from openpyxl import load_workbook
        wb = load_workbook('userList.xlsx')
        ws = wb.active
        ws.append(data)
        wb.save('userList.xlsx')
    # function to check correct password
    def check_correct_psw(psw1, psw2):
        if str(psw2) == str(psw1):
            return True
        else:
            init.print_alert(" الرمزين  السريين  المدرجين  غير  متطابقين ")
            return False

    # function to handle the return the home page
    def return_to_home():
        add_user.pack_forget()
        home.pack()
    # function to add new user
    def add_new_user():
        excel_data = init.read_excel_data_UserList ()
        if name.get() == '':
            init.print_alert(" لم  تقم  بتعمير  خانة  الإسم  ")
        else:
            correct_password = init.search_user_name(name.get(), excel_data)
            if correct_password:
                init.print_alert(" الإسم الذي تمّ إدخاله مسجل في القاعدة ")
            else:
                if check_correct_psw(psw_1, psw_2):
                    add_user_to_list(name.get(), psw_1)
                return_to_home()


    # creating user and password labels and entries
    for i in range(2):
        ttk.Label(add_user, text="\n", font=("Helvetica", 30)).grid(row=i, column=3)

    ttk.Label(add_user, text=": الإسم  ", font=("Helvetica", 30)).grid(row=5, column=3)
    name = ttk.Entry(add_user, font=("Helvetica", 30))
    name.grid(row=5, column=2, padx=20, pady=30, sticky="e")

    ttk.Label(add_user, text=": الرمز السرِّي   ", font=("Helvetica", 30)).grid(row=6, column=3)
    psw_1 = ttk.Entry(add_user, font=("Helvetica", 30), show='*')
    psw_1.grid(row=6, column=2, padx=20, pady=30, sticky="e")

    ttk.Label(add_user, text=": التأكد من الرمز السرِّي   ", font=("Helvetica", 30)).grid(row=6, column=3)
    psw_2 = ttk.Entry(add_user, font=("Helvetica", 30), show='*')
    psw_2.grid(row=6, column=2, padx=20, pady=30, sticky="e")

    ttk.Label(add_user, text="\n", font=("Helvetica", 30)).grid(row=7, column=3)

    # creating a btn to return to home page
    submit_button = ttk.Button(add_user, text="  الرجوع إلى الصفحة الرئيسية  ", command=return_to_home)
    submit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    # creating a btn to return to home page
    submit_button = ttk.Button(add_user, text="  إضافة الحساب   ", command=add_new_user)
    submit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)
    add_user.pack()