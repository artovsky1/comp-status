from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from commands.functions import *
from frames.ChangeCompPage import *


class ChangeTempCompPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Zmiana lokalizacji komponentu")
        master.width, master.height = 350, 250

        create_conn = connection()

        def update_revision_list(*args):
            self.revision_py["values"] = list_revision(self)

        def empty_fields():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            if all(val != "" for val in values):
                result = create_conn.execute(SELECT_COMPONENT_LOC, values).fetchone()
                if result is not None:
                    master.switch_frame(ChangeCompPage, *result)
                else:
                    messagebox.showerror("Błąd", "Nie ma komponentu z takim numerem i rewizją")
            else:
                messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione")

        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.partnumber_py = ttk.Combobox(self, width=20, values=list_partnumber())
        self.partnumber_py.bind('<KeyRelease>', lambda event: search(self, event))
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=20, values=list_revision(self))

        self.partnumber_py.focus_set()

        self.partnumber_py_label = Label(self, text="Part number: ", font=LabelFont, bg=BgColor)
        self.partnumber_py_label.grid(row=0, column=0)
        self.revision_py_label = Label(self, text="Rewizja: ", font=LabelFont, bg=BgColor)
        self.revision_py_label.grid(row=1, column=0)

        self.edit_btn = Button(self, text="Zmień lokalizację", image=self.button_img, **ButtonSettings,
                               command=empty_fields)

        self.back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                               command=lambda: master.switch_frame(StartPage))

        Label(self, text="", bg=BgColor).grid(row=0, column=0, columnspan=2)

        self.partnumber_py_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')
        self.revision_py_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.partnumber_py.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        self.revision_py.grid(row=2, column=1, padx=10, pady=10, sticky='W')

        Label(self, text="", bg=BgColor).grid(row=3, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=2)

        self.edit_btn.place(relx=0.75, rely=0.75, anchor='center')
        self.back_btn.place(relx=0.25, rely=0.75, anchor='center')
