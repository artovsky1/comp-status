from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from functions.styles import *


class ChangeCompPage(Frame):

    def __init__(self, master, partnumber, revision, localization):
        from frames.ChangeTempCompPage import ChangeTempCompPage
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Zmiana lokalizacji komponentu")
        master.width, master.height = 800, 600

        create_conn = connection()

        def empty_fields():
            if self.new_localization_py.get().strip() != "":
                button_action()
            else:
                messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione")

        def button_action():
            if messagebox.askyesno("Informacja", "Czy chcesz zmienić lokalizację komponentu?"):
                values = (self.new_localization_py.get().strip(), self.partnumber_py.get().strip(),
                          self.revision_py.get().strip())
                create_conn.execute(CHANGE_COMP_LOC, values)
                messagebox.showinfo("Powodzenie", "Lokalizacja zmieniona pomyślnie")
                repeat()

        def repeat():
            if messagebox.askyesno("Informacja", "Czy chcesz zmienić lokalizację kolejnego komponentu?"):
                master.switch_frame(ChangeTempCompPage)
            else:
                master.switch_frame(StartPage)

        self.partnumber_py = ttk.Entry(self, width=200)
        self.partnumber_py.insert(0, partnumber.strip())
        self.partnumber_py.configure(state='readonly')
        self.partnumber_py.grid(row=0, column=1)

        self.revision_py = ttk.Entry(self, width=200)
        self.revision_py.insert(0, revision.strip())
        self.revision_py.configure(state='readonly')
        self.revision_py.grid(row=1, column=1)

        self.localization = ttk.Entry(self, width=200)
        self.localization.insert(0, localization.strip())
        self.localization.configure(state='readonly')
        self.localization.grid(row=2, column=1)
        self.new_localization_py = ttk.Entry(self, width=200)
        self.new_localization_py.grid(row=3, column=1)

        self.new_localization_py.focus_set()

        adient_py_label = ttk.Label(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0)
        revision_py_label = ttk.Label(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)
        actual_loc_py_label = ttk.Label(self, text="Aktualna Lokalizacja: ")
        actual_loc_py_label.grid(row=2, column=0)
        new_loc_py_label = ttk.Label(self, text="Nowa lokalizacja: ")
        new_loc_py_label.grid(row=3, column=0)

        edit_btn = ttk.Button(self, text="Przyjmij komponent", command=empty_fields)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = ttk.Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)
