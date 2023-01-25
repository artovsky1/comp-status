from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *
from frames.StartPage import *


class LoginPage(CTkFrame):

    def __init__(self, master):
        CTkFrame.__init__(self, master)
        style_login_page(master)
        create_conn = connection()

        def button_login(*args):
            if all(val != "" for val in (self.username_py.get().strip(), self.password_py.get().strip())):
                login_check()
            else:
                messagebox.showerror("Błąd", "Wprowadź login i hasło")

        def login_check():
            if select_login() is not None:
                logging()
            else:
                messagebox.showerror("Błąd", "Wprowadzony login jest nieprawidłowy")

        def select_login():
            return create_conn.execute(SELECT_LOGIN, (self.username_py.get().strip())).fetchone()

        def logging():
            if select_password() is not None:
                messagebox.showinfo("Powodzenie", "Logowanie pomyślne")
                master.switch_frame(StartPage)
            else:
                messagebox.showerror("Błąd", "Wprowadzone hasło jest nieprawidłowe")

        def select_password():
            values = (self.username_py.get().strip(), self.password_py.get().strip())
            return create_conn.execute(SELECT_PASSWORD, values).fetchone()

        def close():
            quit()

        self.username_py = CTkEntry(self, width=200)
        self.username_py.grid(row=1, column=1)
        self.password_py = CTkEntry(self, width=200, show='*')
        self.password_py.grid(row=2, column=1)
        self.username_py.bind("<Return>", button_login)
        self.password_py.bind("<Return>", button_login)

        self.username_py.focus_set()

        username_py_label = CTkLabel(self, text="Login: ")
        username_py_label.grid(row=1, column=0)
        password_py_label = CTkLabel(self, text="Hasło: ")
        password_py_label.grid(row=2, column=0)

        # Create a update button
        login_btn = CTkButton(self, text="Zaloguj", command=button_login)
        login_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        # Create a back button
        exit_btn = CTkButton(self, text="Zamknij", command=close)
        exit_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)
