from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=200, height=400)
window.config(padx=20, pady=20)

image_path = "logo.png"
logo = PhotoImage(file=image_path)

canvas = Canvas()
canvas.create_image(200, 170, image=logo)
canvas.grid(column=1, row=1)

mainloop()
