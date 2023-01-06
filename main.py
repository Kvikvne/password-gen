from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# --------------------------SEARCH BUTTON---------------------------------------#


def find_password():
    s = open("data.json")
    data_s = json.load(s)

    try:
        web = data_s[website_entry.get()]
    except KeyError:
        messagebox.showinfo(title="Password GEN", message=f"No password saved for {website_entry.get()}")
    else:
        passw = web["Password"]
        emailw = web["email"]
        messagebox.showinfo(title="Password GEN", message=f"{website_entry.get()}:\n----------------"
                                                          f"\nEmail: {emailw}\nPassword: {passw}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# file = open("Passwords.txt", "a")


def save():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "Password": password,

        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Password GEN", message="One or more entries are empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            messagebox.showinfo(title="Password GEN", message="Password copied to clipboard")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password GEN")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3)

# Entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=27)
email_entry.insert(0, "kaianderson9@gmail.com")
email_entry.grid(row=2, column=1, columnspan=1)
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

# Buttons
gen_password_button = Button(text="Generate Password", command=password_gen)
gen_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=22, command=save)
add_button.grid(row=4, column=1, columnspan=1)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
