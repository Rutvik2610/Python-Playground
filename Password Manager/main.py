from tkinter import *
from tkinter import messagebox
import random
import json

GRAY = "#E1E5EA"
BLUE = "#012443"
LIGHT_BLUE = "#B5EAEA"
RED = "#FF2626"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_entry.delete(0, END)
    password = []

    password += [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password)
    final_password = "".join(password)

    password_entry.insert(0, final_password)
    window.clipboard_clear()
    window.clipboard_append(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    data = None
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it okay to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                data = new_data
            except json.JSONDecodeError:
                data = new_data
            else:
                if website in data:
                    update = messagebox.askyesno("Warning", f"There is already a password saved for {website}.\n"
                                                            f"Would you like to overwrite?")
                    if update:
                        data[website]["password"] = password
                        data[website]["email"] = email
                else:
                    # Updating old data with new data
                    data.update(new_data)

            finally:
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- Clear entered data ------------------------------- #
def clear_data():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    user_entry.delete(0, END)


# ---------------------------- Search data ------------------------------- #
def search():
    website = website_entry.get()
    search_result = None

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            search_result = f"No details for {website} exist."
        else:
            if website in data:
                password = data[website]["password"]
                email = data[website]["email"]
                search_result = f"Website: {website}\nEmail: {email}\nPassword: {password}"
            else:
                search_result = f"No details for {website} exist."
        finally:
            messagebox.showinfo(title="Search Result", message=search_result)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=GRAY)

canvas = Canvas(width=200, height=200, bg=GRAY, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=GRAY, fg=RED, highlightthickness=0)
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", bg=GRAY, fg=RED, highlightthickness=0)
user_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=GRAY, fg=RED, highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

user_entry = Entry()
user_entry.insert(0, "rutvik@gmail.com")
user_entry.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

# Buttons
search_button = Button(text="Search", command=search, bg=LIGHT_BLUE, fg=BLUE)
search_button.grid(row=1, column=2, sticky=EW, padx=5, pady=5)

clear_all_button = Button(text="Clear All", command=clear_data, bg=LIGHT_BLUE, fg=BLUE)
clear_all_button.grid(row=2, column=2, sticky=EW, padx=5, pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password, bg=LIGHT_BLUE, fg=BLUE)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)

add_button = Button(text="Add", width=36, command=save, bg=LIGHT_BLUE, fg=BLUE)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

window.mainloop()
