from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *
from functions.suggestions import *
from frames.ChangeCompPage import *


class ChangeTempCompPage(CTkFrame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        CTkFrame.__init__(self, master)
        style_change_comp_page(master)
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

        self.partnumber_py = ttk.Combobox(self, width=30, values=list_partnumber())
        self.partnumber_py.grid(row=0, column=1)
        self.partnumber_py.bind('<KeyRelease>', lambda event: search(self, event))
        # self.partnumber_py.bind('<KeyRelease>', update_revision_list)
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=30, values=list_revision(self))
        self.revision_py.grid(row=1, column=1)

        self.partnumber_py.focus_set()

        adient_py_label = CTkLabel(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0)
        revision_py_label = CTkLabel(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)

        edit_btn = CTkButton(self, text="Zmień lokalizację komponentu", command=empty_fields)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)