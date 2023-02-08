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
from PIL import Image


class StartPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Strona startowa")
        master.width, master.height = 560, 400

        self.background_img = PhotoImage(file=get_path("Background.png"))
        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.background_label = Label(self, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        page_title = Label(self, text="Stan komponentów", bg=BgStartColor, font=TitleFont, fg=FgButtonColor)

        button0 = Button(self, text="Dodaj komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(NewCompPage))

        button1 = Button(self, text="Modyfikuj komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ModifyTempCompPage))

        button2 = Button(self, text="Usuń komponent",
                         image=self.button_img, **ButtonSettings, command=lambda: master.switch_frame(DeletePage))

        button3 = Button(self, text="Przyjmij komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(BringBackCompPage))

        button4 = Button(self, text="Wydaj komponent", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(BringCompPage))

        button5 = Button(self, text="Zmień lokalizację", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ChangeTempCompPage))

        button6 = Button(self, text="Podgląd stanu", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(LookUpPage))

        button7 = Button(self, text="Historia zmian", image=self.button_img, **ButtonSettings,
                         command=lambda: master.switch_frame(ChangeLog))

        page_title.grid(row=0, column=0, pady=20, padx=10)

        Label(self, text="", bg=BgColor).grid(row=1, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=2, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=3, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=9, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=10, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=11, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=12, column=0, columnspan=18)
        Label(self, text="", bg=BgColor).grid(row=13, column=0, columnspan=18)
        Label(self, text="ddddddddddddddddddddddddddddd", bg=BgColor, fg=FgButtonColor).grid(row=14, column=14,
                                                                                             columnspan=18)

        button0.place(relx=0.2, rely=0.38, anchor='center')
        button1.place(relx=0.2, rely=0.63, anchor='center')
        button2.place(relx=0.2, rely=0.88, anchor='center')
        button3.place(relx=0.5, rely=0.38, anchor='center')
        button4.place(relx=0.5, rely=0.63, anchor='center')
        button5.place(relx=0.5, rely=0.88, anchor='center')
        button6.place(relx=0.8, rely=0.38, anchor='center')
        button7.place(relx=0.8, rely=0.63, anchor='center')
