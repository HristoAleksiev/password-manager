from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# --------------------- PASSWORD GENERATOR ------------------------ #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    final_password = "".join(password_list)
    password_entry.insert(0, string=final_password)
    pyperclip.copy(final_password)

# ------------------------ SAVE PASSWORD --------------------------- #


def ingest_form_data():
    if website_entry.get().strip() == "" or user_email_entry.get().strip() == "" or password_entry.get().strip() == "":
        messagebox.showwarning(title="Warning",
                               message="You are leaving an empty field. "
                                       "Please provide all the information in the form!")
    else:
        user_confirmation = messagebox.askokcancel(title="Details Confirmation",
                                                   message=f"Are you sure you want to save the credentials:"
                                                           f" email: {user_email_entry.get()} "
                                                           f"and password: {password_entry.get()}"
                                                           f" for the website: {website_entry.get()}")

        if user_confirmation:

            data_to_dump = {
                website_entry.get(): {
                        "email": user_email_entry.get(),
                        "password": password_entry.get()
                }
            }

            try:
                with open("passwords-database.json", "r") as pass_db:
                    loaded_data = json.load(pass_db)
            except FileNotFoundError:
                with open("passwords-database.json", "w") as pass_db:
                    json.dump(data_to_dump, pass_db, indent=4)
            else:
                loaded_data.update(data_to_dump)
                with open("passwords-database.json", "w") as pass_db:
                    json.dump(loaded_data, pass_db, indent=4)
            finally:
                website_entry.delete(0, END)
                user_email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ------------------------ SAVE PASSWORD --------------------------- #


def get_password():
    searching_site = website_entry.get()

    try:
        with open("passwords-database.json", "r") as data:
            loaded_data = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Missing file to read!",
                             message="There is no database file found from which to read, "
                                     "please save some passwords first.")
    else:
        if searching_site in loaded_data:
            found_data = loaded_data[searching_site]
            messagebox.showinfo(title=searching_site,
                                message=f"These are the saved credentials for the searched website:\n"
                                        f"    {found_data['email']}\n"
                                        f"    {found_data['password']}")
        else:
            messagebox.showerror(title="No credentials found!",
                                 message="There are no saved credentials for the website you are searching for!\n"
                                         "Please fill the form to save your new credentials.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Column 1

website = Label(text="Website: ")
website.grid(column=0, row=1)

user_email = Label(text="Email/Username: ")
user_email.grid(column=0, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

# Column 2

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew")

user_email_entry = Entry(width=35)
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", padx=1)

add_button = Button(text="Add", width=36, command=ingest_form_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# Column 3

search_button = Button(text="Search", command=get_password)
search_button.grid(column=2, row=1, sticky="ew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

mainloop()
