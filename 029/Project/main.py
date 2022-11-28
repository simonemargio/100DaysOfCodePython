from tkinter import *
from tkinter import messagebox
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    return password


def alert_data_saved():
    messagebox.showinfo("Correct", "Entry saved")


def warning_entry(field):
    messagebox.showwarning("Warning", f"The field {field} can't be empty!")


def add_generate_password():
    if len(entry_password.get()) != 0:
        entry_password.delete(0, END)
    new_password = generate_password()
    entry_password.insert(0, new_password)


def check_field(field_data, field_name):
    if len(field_data) == 0:
        warning_entry(field_name)
        return False
    else:
        return True


def write_new_entry(website, username, password):
    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {username} | {password}\n")
        alert_data_saved()
        entry_website.delete(0, END)
        entry_password.delete(0, END)


def add_new_entry():
    website = str(entry_website.get())
    username = str(entry_username.get())
    password = str(entry_password.get())
    if check_field(website, "website") and check_field(username, "username") and check_field(password, "password"):
        write_new_entry(website, username, password)


w = Tk()
w.title("Password Manager")
w.config(padx=20, pady=20)
c = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
c.create_image(100, 100, image=logo)
c.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_username = Label(text="Username:")
label_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "hello@simonemargio.im")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_generate_password = Button(text="Generate  🔑 ", command=add_generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=33, command=add_new_entry)
button_add.grid(column=1, row=4, columnspan=2)

w.mainloop()
