from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_box.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for char in range(randint(8, 10))]
    random_symbols = [choice(symbols) for char in range(randint(2, 4))]
    random_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = random_numbers + random_letters + random_symbols
    shuffle(password_list)

    generated_pass = "".join(password_list)

    password_box.insert(0, generated_pass)
    messagebox.showinfo(title="Copied", message="Generated password has been copied to clipboard!!!")
    pyperclip.copy(generated_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(link_box.get()) == 0 or len(password_box.get()) == 0:
        messagebox.showinfo(title="Invalid",message="Some fields are left empty!")

    else:
        if_yes = messagebox.askyesno(title=link_box.get(),message=f"Please confirm the details:\nEmail: {email_box.get()}\nPassword: {password_box.get()}\nAre the details correct?")
        if if_yes:
            with open("email.txt", mode="w") as email:
                email.write(f"{email_box.get()}")
                
            with open("data.txt","a") as file:
                file.write(f"Website: {link_box.get()} | Email: {email_box.get()} | Password: {password_box.get()}\n")
            link_box.delete(0,END)
            password_box.delete(0,END)
        else:
            pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0, column=2,columnspan=1)

#Label website
website = Label(text="Website:",font=("Courier",12,"normal"))
website.grid(row=3,column=1)

#Website entry
link_box = Entry(width=60)
link_box.focus()
link_box.grid(row=3,column=2,columnspan=2)

#Label email
email = Label(text="Email/Username:",font=("Courier",12,"normal"))
email.grid(row=4,column=1)

#Email entry
email_box = Entry(width=60)
email_box.grid(row=4,column=2,columnspan=2)

with open("email.txt") as new_email:
    current_email = new_email.read()

email_box.insert(END,current_email)

#Label password
password = Label(text="Password:",font=("Courier",12,"normal"))
password.grid(row=5,column=1)

#Passwrod entry
password_box = Entry(width=40)
password_box.grid(row=5,column=2)

#Button generate password
generate_password = Button(text="Generate Password",width=15,command=generate)
generate_password.grid(row=5,column=3)

#Button add
add_password = Button(text="Add",width=50,command=save)
add_password.grid(row=6,column=2,columnspan=3)





window.mainloop()