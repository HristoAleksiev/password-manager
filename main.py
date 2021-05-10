from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.tile("Password Manager")
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
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

user_email_entry = Entry(width=35)
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", padx=1)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# Column 3

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="w")

mainloop()
