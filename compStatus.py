from tkinter import *
from tkinter import messagebox, ttk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from commands.styles import *
from database.sql_commands import *
from frames.StartPage import StartPage
from frames.LoginPage import *


class Inventory(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title_name = ""
        self.title(self.title_name)
        self.frame = None
        self.switch_frame(StartPage)
        self.config(bg=BgColor)
        icon = PhotoImage(file=get_path("icon_small.png"))
        self.iconphoto(True, icon)

    def switch_frame(self, frame_class, *args, **kwargs):
        new_frame = frame_class(self, *args, **kwargs)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()
        x = (self.winfo_screenwidth() / 2) - (self.width / 2)
        y = (self.winfo_screenheight() / 2) - (self.height / 2)
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))


if __name__ == "__main__":
    app = Inventory()
    app.mainloop()

# pyinstaller --noconfirm --onefile --windowed --add-data "C:\Users\akozyrs\Desktop\stan_komp\background.png;." --add-data "C:\Users\akozyrs\Desktop\stan_komp\icon_small.png;." --add-data "C:\Users\akozyrs\Desktop\stan_komp\Button.png;." --icon=C:\Users\akozyrs\Desktop\stan_komp\icon_big.png "C:\Users\akozyrs\Desktop\stan_komp\compStatus.py"
