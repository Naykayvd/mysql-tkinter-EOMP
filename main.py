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

date = datetime.datetime.now()


def admin_access():
    window.destroy()
    admin_tab = Tk()
    admin_tab.title("Admin Window")
    admin_tab.geometry("400x400")


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

    # functions
    def sign():
        mydb = mysql.connector.connect(user='lifechoices', password='@lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')
        sql = "SELECT * FROM user"
        mycursor = mydb.cursor()
        xy = mycursor.execute(sql)
        verified = False
        for i in mycursor:
            print(i)
            if user_name_entry.get() == i[0] and user_id_entry.get() == i[2]:
                verified = True
                print(i)
                # sign out page
            root.destroy()
            sign_out_page = Tk()
            sign_out_page.title("Sign out section")
            sign_out_page.geometry("300x300")
            label1 = Label(sign_out_page, text="We hope your enjoyed your day/visit")
            label1.place(x=30, y=20)
            button1 = Button(sign_out_page, text="Sign-Out")
            button1.place(x=120, y=250)
        if not verified:
            messagebox.showerror("Try again", "There maybe a typo or you are not a user")
            user_name_entry.delete(0, END)
            user_id_entry.delete(0, END)
        elif verified:
            messagebox.showinfo("Welcome!!", "You have signed in " + str(user_name_entry.get()) + "\n" +
                                "at " + str(date))

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
    new_user.geometry("500x400")

    new_user_name_label = Label(new_user, text="Enter your name:")
    new_user_name_label.place(x=10, y=30)
    new_user_name_entry = Entry(new_user)
    new_user_name_entry.place(x=300, y=30)
    new_user_surname_label = Label(new_user, text="Enter your surname:")
    new_user_surname_label.place(x=10, y=70)
    new_user_surname_entry = Entry(new_user)
    new_user_surname_entry.place(x=300, y=70)
    new_user_id_label = Label(new_user, text="Enter your ID:")
    new_user_id_label.place(x=10, y=110)
    new_user_id_entry = Entry(new_user)
    new_user_id_entry.place(x=300, y=110)
    new_user_phonenumber_label = Label(new_user, text="Enter your phone number:")
    new_user_phonenumber_label.place(x=10, y=150)
    new_user_phonenumber_entry = Entry(new_user)
    new_user_phonenumber_entry.place(x=300, y=150)
    nextofkin_name_label = Label(new_user, text="Enter a next of kin name:")
    nextofkin_name_label.place(x=10, y=190)
    nextofkin_name_entry = Entry(new_user)
    nextofkin_name_entry.place(x=300, y=190)
    nextofkin_phonenumber_label = Label(new_user, text="Enter the next of kin's phone number:")
    nextofkin_phonenumber_label.place(x=10, y=230)
    nextofkin_phonenumber_entry = Entry(new_user)
    nextofkin_phonenumber_entry.place(x=300, y=230)

    def registering():
        # insert new user to user table
        val = (new_user_name_entry.get(), new_user_surname_entry.get(), new_user_id_entry.get(),
               new_user_phonenumber_entry.get())
        SQL = "INSERT INTO user(name, surname, idnumber, phonenumber) \n VALUES(%s, %s, %s, %s)"
        xy = mycursor.execute(SQL, val)

        # insert into nextofkin table
        val = (nextofkin_name_entry.get(), nextofkin_phonenumber_entry.get())
        SQL = "INSERT INTO nextofkin(nextofkin_name, nextofkin_phonenumber)"
        xy = mycursor.execute(SQL, val)

    def erase2():
        new_user_name_entry.delete(0, END)
        new_user_surname_entry.delete(0, END)
        new_user_id_entry.delete(0, END)
        new_user_phonenumber_entry.delete(0, END)

    submit_button = Button(new_user, text="Submit details", command=registering, bg="blue")
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
admin = Button(window, text="Admin", command=admin_access, bg="red")
admin.place(x=120, y=45)

window.mainloop()
