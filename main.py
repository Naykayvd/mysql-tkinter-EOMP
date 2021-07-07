import mysql.connector
import datetime
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
                    messagebox.showinfo("Welcome!!", "You have signed in" + user_name_entry.get() + "\n" +
                                        "at" + )
            except:
                messagebox.showerror("Try again", "There maybe a typo or you are not a user")
                user_name_entry.delete(0, END)
                user_id_entry.delete(0, END)

    def erase():
        user_name_entry.delete(0, END)
        user_id_entry.delete(0, END)

    # buttons
    sign_in_button = Button(root, text="Login", command=sign, bg="blue")
    sign_in_button.place(x=30, y=140)
    clear_button = Button(root, text="clear", command=erase, bg="blue")
    clear_button.place(x=180, y=140)
    exit_button = Button(root, text="Exit", command=exit, bg="blue")
    exit_button.place(x=320, y=140)


def reg_new_user():
    window.destroy()
    new_user = Tk()
    new_user.title("Fill in your details")
    new_user.geometry("400x400")

    new_user_name_label = Label(new_user, text="Enter your name:")
    new_user_name_label.place(x=50, y=30)
    new_user_name_entry = Entry(new_user)
    new_user_name_entry.place(x=220, y=30)
    new_user_surname_label = Label(new_user, text="Enter your surname:")
    new_user_surname_label.place(x=30, y=70)
    new_user_surname_entry = Entry(new_user)
    new_user_surname_entry.place(x=220, y=70)
    new_user_id_label = Label(new_user, text="Enter your ID:")
    new_user_id_label.place(x=73, y=110)
    new_user_id_entry = Entry(new_user)
    new_user_id_entry.place(x=220, y=110)
    new_user_phonenumber_label = Label(new_user, text="Enter your phone number:")
    new_user_phonenumber_label.place(x=10, y=150)
    new_user_phonenumber_entry = Entry(new_user)
    new_user_phonenumber_entry.place(x=220, y=150)
    nextofkin_name_label = Label(new_user, text="Enter a next of kin name:")
    nextofkin_name_label.place(x=10, y=190)
    nextofkin_name_entry = Entry(new_user)
    nextofkin_name_entry.place(x=220,y=190)

    def erase2():
        new_user_name_entry.delete(0, END)
        new_user_surname_entry.delete(0, END)
        new_user_id_entry.delete(0, END)
        new_user_phonenumber_entry.delete(0, END)

    submit_button = Button(new_user, text="Submit details", bg="blue")
    submit_button.place(x=25, y=350)
    clear2_button = Button(new_user, text="Clear", command=erase2, bg="blue")
    clear2_button.place(x=200, y=350)
    exit2_button = Button(new_user, text="Exit", command=exit, bg="blue")
    exit2_button.place(x=325, y=350)


# creating buttons
log_btn = Button(window, text="Sign in", command=log, bg="blue")
log_btn.place(x=120, y=95)
register = Button(window, text="Register new user", command=reg_new_user, bg="blue")
register.place(x=85, y=145)

window.mainloop()
