from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from functions.sql_commands import *
from functions.connection import *
from frames.StartPage import *
from functions.styles import Font


class LoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(bg='white')
        master.title_name = "Logowanie"
        master.title(master.title_name)
        width, height = 400, 300
        x = (master.winfo_screenwidth() / 2) - (width / 2)
        y = (master.winfo_screenheight() / 2) - (height / 2)
        master.geometry("%dx%d+%d+%d" % (width, height, x, y))

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

        self.username_py = ttk.Entry(self, width=20, font=Font)

        self.password_py = ttk.Entry(self, width=20, show='*', font=Font)

        self.username_py.bind("<Return>", button_login)
        self.password_py.bind("<Return>", button_login)

        self.username_py.focus_set()

        self.username_py_label = Label(self, text="Login: ", font=Font, bg='white')

        self.password_py_label = Label(self, text="Hasło: ", font=Font, bg='white')


        self.grid_rowconfigure(1, weight=1, minsize=0)
        self.grid_columnconfigure(1, weight=1, minsize=0)

        # Create a update button
        self.button_img = PhotoImage(file="images/Button.png")

        self.login_btn = Button(self, text="Zaloguj", compound=CENTER, image=self.button_img, command=button_login,
                                font=Font, bg='white', border='0', fg='white', pady=10)


        # Create a back button
        self.exit_btn = Button(self, text="Zamknij", compound=CENTER, image=self.button_img, command=close,
                               font=Font, bg='white', border='0', fg='white')
        self.username_py.pack(side='right')
        self.password_py.pack(side='right')
        self.username_py_label.pack(side='left', padx=7)
        self.password_py_label.pack(side='left', padx=5)
        self.login_btn.pack(pady=10)
        self.exit_btn.pack(pady=10)

