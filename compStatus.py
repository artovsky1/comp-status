from tkinter import *
from tkinter import messagebox, ttk
from database.sql_commands import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
import pyodbc
from commands.styles import *
from frames.StartPage import StartPage
from frames.LoginPage import *


class Inventory(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title_name = ""
        self.title(self.title_name)
        self._frame = None
        self.switch_frame(LoginPage)
        self.config(bg=BgColor)

    def switch_frame(self, frame_class, *args, **kwargs):
        new_frame = frame_class(self, *args, **kwargs)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        x = (self.winfo_screenwidth() / 2) - (self.width / 2)
        y = (self.winfo_screenheight() / 2) - (self.height / 2)
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))


if __name__ == "__main__":
    app = Inventory()
    app.mainloop()

# pyinstaller --noconfirm --windowed --noconsole "C:\Users\akozyrs\Desktop\python\stan_komp.py"
