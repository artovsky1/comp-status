from tkinter import *
from tkinter import messagebox, ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from frames.StartPage import *
from PIL import Image


class LoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Logowanie")
        master.width, master.height = 350, 250

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

        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.username_py_label = Label(self, text="Login: ", font=LabelFont, bg=BgColor)
        self.username_py = ttk.Entry(self, font=EntryFont)

        self.password_py_label = Label(self, text="Hasło: ", font=LabelFont, bg=BgColor)
        self.password_py = ttk.Entry(self, show='*', font=EntryFont)

        self.login_btn = Button(self, text="Zaloguj", image=self.button_img, **ButtonSettings, command=button_login)
        self.exit_btn = Button(self, text="Zamknij", image=self.button_img, **ButtonSettings, command=close)

        Label(self, text="", bg=BgColor).grid(row=0, column=0, columnspan=2)

        self.username_py_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')
        self.username_py.grid(row=1, column=1, padx=10, pady=10, sticky='W')

        self.password_py_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.password_py.grid(row=2, column=1, padx=10, pady=10, sticky='W')

        Label(self, text="", bg=BgColor).grid(row=3, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=2)

        self.login_btn.place(relx=0.75, rely=0.75, anchor='center')
        self.exit_btn.place(relx=0.25, rely=0.75, anchor='center')

        self.username_py.bind("<Return>", button_login)
        self.password_py.bind("<Return>", button_login)

        self.username_py.focus_set()
