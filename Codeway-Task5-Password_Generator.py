


from tkinter import *
import random
import string
import pyperclip
from tkinter import messagebox

def generate_password():
    if choice.get() == 0:
        messagebox.showinfo("Error", "Please select an option")
        return

    password = passgen()
    if password:
        password_var.set(password)

def copy_to_clipboard():
    if password_var.get() == "":
        messagebox.showinfo("Error", "Please generate a password first")
        return

    pyperclip.copy(password_var.get())
    root.deiconify()  # Show the window if it was minimized

def passgen():
    poor = string.ascii_lowercase
    average = string.ascii_letters + string.digits
    advance = string.ascii_letters + string.digits + string.punctuation

    if choice.get() == 1:
        return "".join(random.sample(poor, val.get())) if val.get() > 0 else None
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get())) if val.get() > 0 else None
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get())) if val.get() > 0 else None

def update_option():
    selected_option = choice.get()
    option_labels = ["WEAK", "AVERAGE", "STRONG"]

    for i, option_label in enumerate(option_labels):
        if i + 1 == selected_option:
            option_buttons[i].config(bg="#f39c12", fg="#ffffff", activebackground="#d35400", text=f"{option_label} ✓")
        else:
            option_buttons[i].config(bg="#3498db", fg="#ffffff", activebackground="#2980b9", text=option_label)

root = Tk()
root.title("Password Generator APP")
root.geometry("800x500")  # Set the initial size of the window
root.config(bg="#3498db")  # Set background color

title = Label(root, text="CHOOSE AN OPTION", font=("Arial", 24, "bold"), bg="#3498db", fg="#ffffff")
title.pack(pady=(20, 10))

choice = IntVar()
option_labels = ["WEAK", "AVERAGE", "STRONG"]
option_buttons = []

for i, option_label in enumerate(option_labels):
    option_button = Radiobutton(root, text=option_label, variable=choice, value=i + 1, font=("Arial", 18), bg="#3498db", fg="#ffffff", selectcolor="#3498db", activebackground="#2980b9", command=update_option)
    option_button.pack(anchor=CENTER, pady=10)
    option_buttons.append(option_button)

len_label = Label(root, text="Password length:", font=("Arial", 18, "bold"), bg="#3498db", fg="#ffffff")
len_label.pack()

val = IntVar()
Spinbox(root, from_=4, to_=32, textvariable=val, width=13, font=("Arial", 18)).pack()

generate_button = Button(root, text="Generate Password", bd=5, command=generate_password, font=("Arial", 18), bg="#f39c12", fg="#ffffff", activebackground="#d35400")
generate_button.pack(pady=(20, 20))

password_frame = Frame(root, bg="#3498db")
password_frame.pack(pady=(20, 20), padx=20)

password_var = StringVar()
password_entry = Entry(password_frame, textvariable=password_var, font=("Arial", 18), bd=5, relief=SOLID, width=20, justify=CENTER,state="readonly")
password_entry.grid(row=0, column=0)

copy_button = Button(password_frame, text="📋", command=copy_to_clipboard, font=("Arial", 18), bg="#e74c3c", fg="#ffffff", activebackground="#c0392b", padx=10, pady=5)
copy_button.grid(row=0, column=1, padx=(10, 0))

root.mainloop()
