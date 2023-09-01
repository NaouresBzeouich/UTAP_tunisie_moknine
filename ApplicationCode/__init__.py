from PageDAccueil import *
from openpyxl import Workbook
import os

# Create the main window
root = tk.Tk()

# Adding a title to the main window
root.title("الاتحاد التونسي للفلاحة والصيد البحري Union tunisienne de l'agriculture et de la pêche  ")

# Setting dimensions (width x height)
root.geometry("1900x1000")

# Set the path to your custom icon file (use a .ico format)
iconpath = 'C:/Users/R I B/Desktop/STAGE/UTAP_tunisie_moknine/utap (2).ico'
# Set the window's icon
root.iconbitmap(iconpath)

# create the initial frame
frame = ttk.Frame(root)

# test if user list exist or we wil create it
if not os.path.exists('userList.xlsx'):
    wb = Workbook()  # Create a new Workbook
    wb.save('userList.xlsx')
    wb.close()


def check_password(correct_password):
    entered_password = psw.get()
    if not entered_password == correct_password:
        wrong_psw = ttk.Label(frame, text=" ! الرجاء التثبت من كلمة العبور   ",
                              font=("Helvetica", 30), anchor="center", foreground="red", background="white")
        wrong_psw.grid(row=9, column=1, columnspan=4, padx=10, pady=10)

        def forget():
            wrong_psw.grid_forget()

        root.after(4000, forget)
        return False
    return True


def go_to_home():
    correct_password = 'your_password'
    if check_password(correct_password):
        frame.pack_forget()
        HomePage(root)


# creating user and password labels and entries
for i in range(2):
    ttk.Label(frame, text="\n", font=("Helvetica", 40)).grid(row=i, column=3)

ttk.Label(frame, text=": الإسم  ", font=("Helvetica", 40)).grid(row=5, column=3)
name = ttk.Entry(frame, font=("Helvetica", 40))
name.grid(row=5, column=2, padx=20, pady=30, sticky="e")

ttk.Label(frame, text=": رمز السرِّي   ", font=("Helvetica", 40)).grid(row=6, column=3)
psw = ttk.Entry(frame, font=("Helvetica", 40), show='*')
psw.grid(row=6, column=2, padx=20, pady=30, sticky="e")

ttk.Label(frame, text="\n", font=("Helvetica", 40)).grid(row=7, column=3)

# creating a btn to go to home page
submit_button = ttk.Button(frame, text=" دخول  ", command=go_to_home)
submit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

frame.pack()

# Increase the button size0
ttk.Style().configure("TButton", font=("Helvetica", 40), padding=5, anchor="e")

# Start the GUI event loop
root.mainloop()
