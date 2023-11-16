import json
from tkinter import *
import secrets
import string
from tkinter import messagebox #not a class therefore does not get imported by *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

def password_gen():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]


    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)


    print(f"Your password is: {password}")
    input_password.delete(0,END)
    input_password.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    # messagebox.showinfo(title="Title", message="Message")
    if len(website) * len(email) * len(password) == 0:
        messagebox.showinfo(title="Check", message="Dont leave any fields empty")
    else:
        try:
            with open("file.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("file.json", mode="w") as file:
                json.dump(data, file, indent=4)

        except json.decoder.JSONDecodeError:
            with open("file.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        finally:        # file.write(f'{website}|{email}|{password}\n')
            input_website.delete(0, END)
            input_password.delete(0, END)

def search():
    website = input_website.get()
    try:
        with open("file.json", mode="r") as file:
            data = json.load(file)
            data = data[website]
            messagebox.showinfo(title=website, message=f"email:{data['email']}\n Password:{data['password']}")
    except:
        messagebox.showinfo(title=website, message=f"website not available")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website")
website.grid(row=1, column=0)

input_website = Entry(width=20)
input_website.grid(row=1, column=1, columnspan=1)
input_website.focus()


input_search = Button(width=14, text="Search", bg="#f7f5dd", command=search)
input_search.grid(row=1, column=2, columnspan=1)


email_Username = Label(text="Email/Username")
email_Username.grid(row=2, column=0)

input_email = Entry(width=38)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0,"arnavmarik@gmail.com" )

password = Label(text="Password")
password.grid(row=3, column=0)

input_password = Entry(width=20)
input_password.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command =password_gen)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command= save_file)
add.grid(row=4, column=1, columnspan=2)













window.mainloop()