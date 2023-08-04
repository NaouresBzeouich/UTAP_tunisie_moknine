import tkinter as tk
def FormPage(form,root):
    # showing the form page
    form.pack(pady=10)
    # Function to handle the form submission
    def submit_form():
        #for testing everthing is okkey
        for i, entry in enumerate(entries):
            print(f"Input {i + 1}: {entry.get()}")
        print("Form submitted!")
    # Create labels and entry fields for the form
    labels = ["Input 1:", "Input 2:", "Input 3:", "Input 4:", "Input 5:", "Input 6:"]
    entries = [tk.Entry(form) for _ in range(6)]
    # Place labels and entry fields in the frame
    for i, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
        entries[i].grid(row=i, column=1, padx=10, pady=5)
    # creating submit button
    submitButton=tk.Button(root,text=" تسجيل المشترك ",command=submit_form)
    submitButton.pack(pady=20)



