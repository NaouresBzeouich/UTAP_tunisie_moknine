import tkinter as tk
from tkinter import ttk
import outputInputXlFile as xl
import frontEnd as fe
import PageDAccueil as pa
import os

# Create the main window
root = tk.Tk()

# Adding a title to the main window
root.title("الاتحاد التونسي للفلاحة والصيد البحري Union tunisienne de l'agriculture et de la pêche  ")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to match the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Set the path to your custom icon file (use a .ico format)
icon_path = 'utap (2).ico'
# Check if the icon file exists and then set it
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print("Icon file not found:", icon_path)

# create the initial frame
frame = ttk.Frame(root)

xl.testExistingXlFile('userList.xlsx')


def check_password(correct_password):
    entered_password = str(psw.get())
    if not entered_password == str(correct_password):
        fe.print_alert(" ! الرجاء التثبت من كلمة العبور  ", root, frame, 9, 1)
        return False
    return True


def search_user_name(user_name, data):
    for i, row in enumerate(data):
        if str(user_name) == str(row[0]):
            return row[1]
    return False


def go_to_home():
    excel_data = xl.read_excel_data_UserList('userList.xlsx')
    if name.get() == '':
        fe.print_alert(" لم  تقم  بتعمير  خانة  الإسم  ", root, frame, 9, 1)
    else:
        correct_password = search_user_name(name.get(), excel_data)
        if not correct_password:
            fe.print_alert(" الإسم الذي تمّ إدخاله غير مسجل في القاعدة ", root, frame, 9, 1)
        else:
            if check_password(correct_password):
                frame.pack_forget()
                pa.HomePage(root, str(name.get()), "admin")


# creating user and password labels and entries
for i in range(2):
    fe.addLabel(frame, "\n", i)

fe.addLabel(frame, ": الإسم  ", 5, 3, 40)
name = fe.addEntry(frame, 5, 2)

fe.addLabel(frame, ": الرمز السرِّي   ", 6, 3, 40)
psw = fe.addPswdEntry(frame, 6, 2)

# creating a btn to go to home page
fe.addLabel(frame, "\n", 7)
fe.addBttn(frame, go_to_home, 8, 2, 40)

frame.pack()

# Start the GUI event loop
root.mainloop()
