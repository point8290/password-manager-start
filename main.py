import json
from tkinter import *
from tkinter import messagebox

import pyperclip

from passwordgenerator import PWD


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    password = PWD.generate_password()
    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)


def search_password():
    website = str(web_input.get()).strip()
    if not website:
        messagebox.showinfo(title="Insufficient Info", message="Please provide website to search for")
        web_input.delete(0, END)
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                email = data[website]["E-mail"]
                password = data[website]["Password"]
                messagebox.showinfo(title=website, message=f"E-mail : {email}\nPassword : {password}")
                pyperclip.copy(password)
                web_input.delete(0, END)

        except FileNotFoundError:
            messagebox.showinfo(title="unable to search", message=f"{website} Not found")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = str(password_input.get()).strip()
    email = str(email_input.get()).strip()
    website = str(web_input.get()).strip()

    if len(password) > 0 and len(email) > 0 and len(website) > 0:

        info_dict = {
            website: {
                "E-mail": email,
                "Password": password
            },
        }

        message = f"""
                    {website}
                    E-mail: {email}
                    Password: {password}"""

        response = messagebox.askokcancel(title="Are you sure?", message=message)
        if response:
            web_input.delete(0, END)
            password_input.delete(0, END)
            try:
                with open("passwords.json", 'r') as file:
                    data = json.load(file)
                    data.update(info_dict)
            except FileNotFoundError:
                with open("passwords.json", 'w') as file:
                    json.dump(info_dict, file, indent=4)
            else:
                with open("passwords.json", 'w') as file:
                    json.dump(data, file, indent=4)

        else:
            web_input.focus()

    else:
        messagebox.showinfo(title="Insufficient Info", message="Please provide full information")


# ---------------------------- UI SETUP ------------------------------- #

font = ('calibre', 10, 'normal')
window = Tk()

window.title("Password manager")
window.config(padx=50, pady=20)
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
search = Frame(window)
search_button = Button(search, bg="#C0C0C0", highlightthickness=0, text="Search Passwords", font=font,
                       command=search_password)
search_button.grid(row=0, column=1)
search_button.grid_configure(padx=11, pady=10)
search.grid(row=1, column=1)
web_label = Label(window, text="Website:", font=font)
web_label.grid(row=1, column=0)
web_input = Entry(search, width=23)
web_input.grid(row=0, column=0)
web_input.grid_configure(padx=5, pady=10)
web_input.focus()
email_label = Label(window, text="Email/Username:", font=font)
email_label.grid(row=2, column=0)
email_input = Entry(window, width=47)
email_input.insert(END, "krishnameghwal635@gmail.com")
email_input.grid_configure(padx=5, pady=10)
email_input.grid(row=2, column=1)
password_label = Label(window, text="Password:", font=font)
password_label.grid(row=3, column=0)
generate = Frame(window)
generate.grid(row=3, column=1)
generate.grid_configure(padx=5)
password_input = Entry(generate, width=23)
password_input.grid(row=0, column=0)
generate_button = Button(generate, bg="#C0C0C0", highlightthickness=0, text="Generate Password", font=font,
                         command=get_password)
generate_button.grid(row=0, column=1)
generate_button.grid_configure(padx=11, pady=10)
add_button = Button(window, bg="#C0C0C0", highlightthickness=0, text="ADD", width=40, font=font, command=save_password)
add_button.grid(row=4, column=1)
add_button.grid_configure(padx=10, pady=10)
window.mainloop()
