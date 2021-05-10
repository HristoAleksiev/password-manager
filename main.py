from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def ingest_form_data():
    if website_entry.get().strip() == "" or user_email_entry.get().strip() == "" or password_entry.get().strip() == "":
        messagebox.showwarning(title="Warning",
                               message="You are leaving an empty field. Please provide all the information in the form!")
    else:
        user_confirmation = messagebox.askokcancel(title="Details Confirmation",
                                                   message=f"Are you sure you want to save the credentials:"
                                                           f" email: {user_email_entry.get()} "
                                                           f"and password: {password_entry.get()}"
                                                           f" for the website: {website_entry.get()}")

        if user_confirmation:
            with open("passwords-database.txt", "a") as pass_db:
                pass_db.write(f"{website_entry.get()}  |  ")
                website_entry.delete(0, END)
                pass_db.write(f"{user_email_entry.get()}  |  ")
                user_email_entry.delete(0, END)
                pass_db.write(f"{password_entry.get()}\n")
                password_entry.delete(0, END)
                website_entry.focus()

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
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

user_email_entry = Entry(width=35)
# .insert() here ?
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", padx=1)

add_button = Button(text="Add", width=36, command=ingest_form_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# Column 3

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="w")

mainloop()
