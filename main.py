import os.path
from tkinter import *
from tkinter import messagebox

from passwordgenerator import PWD

pass_art = r"""
 
.______      ___           _______.     _______.____    __    ____  ______   .______       _______       _______.
|   _  \    /   \         /       |    /       |\   \  /  \  /   / /  __  \  |   _  \     |       \     /       |
|  |_)  |  /  ^  \       |   (----`   |   (----` \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  |   |   (----`
|   ___/  /  /_\  \       \   \        \   \      \            /  |  |  |  | |      /     |  |  |  |    \   \    
|  |     /  _____  \  .----)   |   .----)   |      \    /\    /   |  `--'  | |  |\  \----.|  '--'  |.----)   |   
| _|    /__/     \__\ |_______/    |_______/        \__/  \__/     \______/  | _| `._____||_______/ |_______/    
                                                                                                                 

************************************************************************************************************************                                                   
"""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    password = PWD.generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = password_input.get()
    email = email_input.get()
    website = web_input.get()

    if len(password) > 0 and len(email) > 0 and len(website) > 0:
        message = f"""
                    Website  : {website}
                    E-mail   : {email}
                    Password : {password}
                    """

        response = messagebox.askokcancel(title="Are you sure?", message=message)
        if response:
            web_input.delete(0, END)
            password_input.delete(0, END)
            if not os.path.isfile("passwords.txt"):
                with open("passwords.txt", 'a') as file:
                    file.write(pass_art)

            with open("passwords.txt", 'a') as file:
                file.write(message)
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

web_label = Label(window, text="Website:", font=font)
web_label.grid(row=1, column=0)
web_input = Entry(window, width=50)
web_input.grid(row=1, column=1)
web_input.grid_configure(padx=5, pady=10)
web_input.focus()
email_label = Label(window, text="Email/Username:", font=font)
email_label.grid(row=2, column=0)
email_input = Entry(window, width=50)
email_input.insert(END, "krishnameghwal635@gmail.com")
email_input.grid_configure(padx=5, pady=10)
email_input.grid(row=2, column=1)
password_label = Label(window, text="Password:", font=font)
password_label.grid(row=3, column=0)
f = Frame(window)
f.grid(row=3, column=1)
f.grid_configure(padx=5)
password_input = Entry(f, width=23)
password_input.grid(row=0, column=0)
generate_button = Button(f, bg="#C0C0C0", width=18, highlightthickness=0, text="Generate Password", font=font,
                         command=get_password)
generate_button.grid(row=0, column=1)
generate_button.grid_configure(padx=11, pady=10)
add_button = Button(window, bg="#C0C0C0", highlightthickness=0, text="ADD", width=40, font=font, command=save_password)
add_button.grid(row=4, column=1)
add_button.grid_configure(padx=10, pady=10)
window.mainloop()
