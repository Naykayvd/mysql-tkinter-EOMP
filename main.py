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

# creating buttons
log_btn = Button(window, text="Sign in")
log_btn.place(x=120, y=95)
register = Button(window, text="Register new user")
register.place(x=85, y=145)

window.mainloop()
