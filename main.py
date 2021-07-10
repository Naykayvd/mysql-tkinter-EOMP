import mysql.connector
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# creating window
window = tk.Tk()
window.title("Login screen")
window.geometry("300x200")
welcome_label = Label(window, text="Please sign in or register")
welcome_label.place(x=70, y=10)

date = datetime.datetime.now()
window.bind("<Control-a>", lambda z: admin_access())


def admin_access():
    window.destroy()
    admin_tab = Tk()
    admin_tab.title("Admin Window")
    admin_tab.geometry("900x820")
    # Tree view columns
    connect = mysql.connector.connect(user="lifechoices", password="@lifechoices1234", host="127.0.0.1",
                                      database="lifechoices_online", auth_plugin="mysql_native_password")
    conn = connect.cursor()
    conn.execute("SELECT * FROM user")
    tree = ttk.Treeview(admin_tab)
    tree["columns"] = ("name", "surname", "idnumber", "phonenumber", "time_in", "time_out")
    tree.column("name", width=115, minwidth=115, anchor=tk.CENTER)
    tree.column("surname", width=115, minwidth=115, anchor=tk.CENTER)
    tree.column("idnumber", width=115, minwidth=115, anchor=tk.CENTER)
    tree.column("phonenumber", width=115, minwidth=115, anchor=tk.CENTER)
    tree.column("time_in", width=115, minwidth=115, anchor=tk.CENTER)
    tree.column("time_out", width=115, minwidth=115, anchor=tk.CENTER)

    tree.heading("name", text="Name", anchor=tk.CENTER)
    tree.heading("surname", text="Surname", anchor=tk.CENTER)
    tree.heading("idnumber", text="ID Number", anchor=tk.CENTER)
    tree.heading("phonenumber", text="Phone Number", anchor=tk.CENTER)
    tree.heading("time_in", text="Time in", anchor=tk.CENTER)
    tree.heading("time_out", text="Time out", anchor=tk.CENTER)

    i = 0
    for row in conn:
        tree.insert('', i, text="USER", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        i = i + 1
    tree.place(x=5, y=10)

    connect = mysql.connector.connect(user="lifechoices", password="@lifechoices1234", host="127.0.0.1",
                                      database="lifechoices_online", auth_plugin="mysql_native_password")
    conn = connect.cursor()
    conn.execute("SELECT * FROM nextofkin")
    nextofkin_tree = Listbox(admin_tab, height=10, width=110)
    nextofkin_tree.place(x=8, y=240)
    for i in conn:
        nextofkin_tree.insert('end', str(i))

    def delete_user():
        user_nm = entry_delete.get()
        mydb = mysql.connector.connect(user='lifechoices', password='@lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "Delete from user Where idnumber = %s"
        mycursor.execute(sql, [(user_nm)])
        mydb.commit()
        messagebox.showinfo("USER DELETED", "User deleted")

    # buttons
    delete_text = Label(admin_tab, text="Select from where to delete")
    delete_text.place(x=460, y=665)
    entry_delete = Entry(admin_tab)
    entry_delete.place(x=650, y=665)
    remove_button = Button(admin_tab, text="Delete", command=delete_user,bg="red")
    remove_button.place(x=820, y=662)


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
        if not verified:
            messagebox.showerror("Try again", "There maybe a typo or you are not a user")
            user_name_entry.delete(0, END)
            user_id_entry.delete(0, END)
        elif verified:
            messagebox.showinfo("Welcome!!", "Welcome " + str(user_name_entry.get()) + "\n" +
                                "You have signed in at " + str(date))
            # sign out page
            root.destroy()
            sign_out_page = Tk()
            sign_out_page.title("Sign out section")
            sign_out_page.geometry("300x300")
            label1 = Label(sign_out_page, text="We hope your enjoyed your day/visit")
            label1.place(x=30, y=20)
            button1 = Button(sign_out_page, text="Sign-Out", bg="blue")
            button1.place(x=120, y=250)

    def erase():
        user_name_entry.delete(0, END)
        user_id_entry.delete(0, END)

    # buttons
    sign_in_button = Button(root, text="Login", command=sign, bg="blue")
    sign_in_button.place(x=30, y=140)
    clear_button = Button(root, text="clear", command=erase, bg="magenta")
    clear_button.place(x=180, y=140)
    exit_button = Button(root, text="Exit", command=exit, bg="orange")
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
        mydb = mysql.connector.connect(user='lifechoices', password='@lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')
        sql = "SELECT * FROM user"
        mycursor = mydb.cursor()
        # insert new user to user table
        val = (new_user_name_entry.get(), new_user_surname_entry.get(), new_user_id_entry.get(),
               new_user_phonenumber_entry.get())
        SQL = "INSERT INTO user(name, surname, idnumber, phonenumber) \n VALUES(%s, %s, %s, %s)"
        xy = mycursor.execute(SQL, val)
        # insert into nextofkin table
        val = (nextofkin_name_entry.get(), nextofkin_phonenumber_entry.get(), new_user_name_entry.get())
        SQL = "INSERT INTO nextofkin(nextofkin_name, nextofkin_phonenumber, name) \n VALUES(%s, %s, %s)"
        xy = mycursor.execute(SQL, val)
        mydb.commit()
        messagebox.showinfo("REGISTERED", "Your details have been saved")

    def erase2():
        new_user_name_entry.delete(0, END)
        new_user_surname_entry.delete(0, END)
        new_user_id_entry.delete(0, END)
        new_user_phonenumber_entry.delete(0, END)
        nextofkin_name_entry.delete(0, END)
        nextofkin_phonenumber_entry.delete(0, END)

    submit_button = Button(new_user, text="Submit details", command=registering, bg="blue")
    submit_button.place(x=25, y=350)
    clear2_button = Button(new_user, text="Clear", command=erase2, bg="magenta")
    clear2_button.place(x=260, y=350)
    exit2_button = Button(new_user, text="Exit", command=exit, bg="orange")
    exit2_button.place(x=420, y=350)


# creating buttons
log_btn = Button(window, text="Sign in", command=log, bg="blue")
log_btn.place(x=120, y=95)
register = Button(window, text="Register new user", command=reg_new_user, bg="blue")
register.place(x=85, y=145)

window.mainloop()
