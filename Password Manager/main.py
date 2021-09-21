from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

user_entry = Entry()
user_entry.grid(row=2, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

# Buttons
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2, padx=5, pady=5)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

window.mainloop()
