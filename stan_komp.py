from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sql_commands import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from customtkinter import *
import pyodbc
from styles import *
from StartPage import *




class Inventory(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.title_name = ""
        self.title(self.title_name)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class, *args, **kwargs):
        new_frame = frame_class(self, *args, **kwargs)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    app = Inventory()
    app.mainloop()

# pyinstaller --noconfirm --onedir --windowed --noconsole --add-data "C:/Users/akozyrs/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/" "C:\Users\akozyrs\Desktop\python\stan_komp.py"
