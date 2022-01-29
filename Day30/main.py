# Author: Deepak Kumar Singh
# Description: Password Manager to store random password in json file.
# Date Created: 23/01/2022
# Date Modified: 23/01/2022
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json  # json.load, json.dump, json.update

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_entry.delete(0, 'end')

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the generated password to clipboard.


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    is_ok = False
    if len(website) == 0  or len(password) == 0 or len(username) == 0:
        messagebox.showwarning(title="Oops", message="please dont leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \n {username}\n {password}")

    if is_ok:
        try:
            with open("data.json", "r") as file:  # things which can fail
                # reading the json file into a python dictionary
                data = json.load(file)
        except FileNotFoundError: # what happens if there is a failure, handle it.
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        except JSONDecodeError:  # This is to handle when the data.json file is empty, which is invalid json format.
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:  # this executes when there is no failure and everything runs as expected.
            data.update(new_data)  # updating the dictionary with new items
            with open("data.json", "w") as file:
                # save the updated python dictionary into json format into json file
                json.dump(data, file, indent=4)
        finally:  # this executes no matter what.
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    search_for = website_entry.get().lower()
    try:
        with open("data.json", "r") as file:
            val = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="No File Found", message=f"No data file found!")
    except JSONDecodeError:
        messagebox.showerror(title="File empty", message=f"File is empty!")
    else:
        if search_for in val.keys():
            result = val[search_for]['email']
            pwd = val[search_for]['password']
            messagebox.showwarning(title=search_for, message=f"Username: {result}\n Password: {pwd}")
        else:
            messagebox.showerror(title=search_for, message=f"Entry for {search_for} doesn't exist!")




# ---------------------------- DELETE PASSWORD ------------------------------- #
def delete_password():
    to_delete = False
    search_for = website_entry.get()

    with open("data.json", "r") as file:
        val = json.load(file)

    if search_for in val.keys():
        to_delete = messagebox.askokcancel(title=search_for, message=f"Press ok to delete entry for\n {search_for}")
        if to_delete:
            val.pop(search_for)
            with open("data.json", "w") as file:
                json.dump(val, file, indent=4)
                messagebox.showwarning(title=search_for, message=f"Deleted entry for {search_for}")
    else:
        messagebox.showerror(title="No such value found", message=f"Entry for {search_for} doesn't exist")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(height=400, width=600)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# creating widgets

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_label.focus()

username_entry = Entry(justify=LEFT, width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "deepak.singh.buzz@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

genpwd_button = Button(text="Generate Password", command=generate_password)
genpwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_password)
search_button.grid(column=3, row=1)

delete_button = Button(text="Delete", command=delete_password)
delete_button.grid(column=3, row=2)


window.mainloop()