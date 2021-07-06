import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# creating window
window = tk.Tk()
window.title("Login screen")
window.geometry("300x200")
welcome_label = Label(window, text="Please sign in or register")
welcome_label.place(x=70, y=10)

mydb = mysql.connector.connect(user='lifechoices', password='@lifechoices1234', host='127.0.0.1',
                               database='lifechoices_online', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


# Creating the sign in screen for existing users
def log():
    window.destroy()
    root = Tk()
    root.title("Sign-in Screen")
    root.geometry("400x250")
    # entries and labels
    user_name_label = Label(root, text="Enter your name:")
    user_name_label.place(x=30, y=30)
    user_name_entry = Entry(root)
    user_name_entry.place(x=210, y=30)
    user_id_label = Label(root, text="Enter your id:")
    user_id_label.place(x=30, y=60)
    user_id_entry = Entry(root)
    user_id_entry.place(x=210, y=60)

    def sign():
        xy = mycursor.execute('select name, idnumber from user')
        for i in mycursor:
            try:
                if user_name_entry.get() == i[0] and user_id_entry.get() == i[2]:
                    messagebox.showinfo("Welcome!!", "You have signed in" + user_name_entry.get())
            except:
                messagebox.showerror("Try again", "There maybe a typo or you are not a user")
                user_name_entry.delete(0, END)
                user_id_entry.delete(0, END)

    def erase():
        user_name_entry.delete(0, END)
        user_id_entry.delete(0, END)

    # buttons
    sign_in_button = Button(root, text="Login", command=sign)
    sign_in_button.place(x=30, y=140)
    clear_button = Button(root, text="clear", command=erase)
    clear_button.place(x=180, y=140)
    exit_button = Button(root, text="Exit", command=exit)
    exit_button.place(x=320, y=140)


def reg_new_user():
    window.destroy()
    new_user = Tk()
    new_user.title("Fill in your details")
    new_user.geometry("400x400")

    new_user_name_label = Label(new_user, text="Enter your name:")
    new_user_name_label.place(x=50, y=30)
    new_user_name_entry = Entry(new_user)
    new_user_name_entry.place(x=180, y=30)


# creating buttons
log_btn = Button(window, text="Sign in", command=log)
log_btn.place(x=120, y=95)
register = Button(window, text="Register new user", command=reg_new_user)
register.place(x=85, y=145)

window.mainloop()
