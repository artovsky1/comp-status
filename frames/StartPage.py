from tkinter import *
from tkinter import ttk
from commands.styles import *
from frames.BringBackCompPage import *
from frames.NewCompPage import *
from frames.ModifyTempCompPage import *
from frames.DeletePage import *
from frames.BringCompPage import *
from frames.ChangeTempCompPage import *
from frames.LookupPage import *
from frames.ChangelogPage import *


class StartPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Strona startowa")
        master.width, master.height = 800, 600

        self.button_img = PhotoImage(file="images/Button.png")

        Label(self, text="Stan komponentów", bg=BgColor).grid(row=0, column=0)

        button0 = Button(self, text="Dodaj komponent", image=self.button_img, **ButtonSettings, command=lambda: master.switch_frame(NewCompPage))
        button0.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button1 = Button(self, text="Modyfikuj komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ModifyTempCompPage))
        button1.grid(row=1, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

        button2 = Button(self, text="Usuń komponent",
                         image=self.button_img, **ButtonSettings, command=lambda: master.switch_frame(DeletePage))
        button2.grid(row=1, column=2, columnspan=1, pady=10, padx=10, ipadx=50)

        button3 = Button(self, text="Przyjmij komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(BringBackCompPage))
        button3.grid(row=2, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button4 = Button(self, text="Wydaj komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(BringCompPage))
        button4.grid(row=2, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

        button5 = Button(self, text="Zmień lokalizację", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ChangeTempCompPage))
        button5.grid(row=2, column=2, columnspan=1, pady=10, padx=10, ipadx=50)

        button6 = Button(self, text="Podgląd stanu", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(LookUpPage))
        button6.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button7 = Button(self, text="Historia zmian", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ChangeLog))
        button7.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx=50)
