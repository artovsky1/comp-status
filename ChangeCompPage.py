from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sql_commands import *
from customtkinter import *
from styles import *
import connection


class ChangeCompPage(CTkFrame):

    def __init__(self, master, partnumber, revision, localization):
        from ChangeTempCompPage import ChangeTempCompPage
        from StartPage import StartPage
        CTkFrame.__init__(self, master)
        style_change_comp_page(master)
        conn = connection.connection()

        def empty_fields():
            if self.new_localization_py.get().strip() != "":
                button_action()
            else:
                messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione")

        def button_action():
            if messagebox.askyesno("Informacja", "Czy chcesz zmienić lokalizację komponentu?"):
                values = (self.new_localization_py.get().strip(), self.partnumber_py.get().strip(),
                          self.revision_py.get().strip())
                conn.execute(CHANGE_COMP_LOC, values)
                messagebox.showinfo("Powodzenie", "Lokalizacja zmieniona pomyślnie")
                repeat()

        def repeat():
            if messagebox.askyesno("Informacja", "Czy chcesz zmienić lokalizację kolejnego komponentu?"):
                master.switch_frame(ChangeTempCompPage)
            else:
                master.switch_frame(StartPage)

        self.partnumber_py = CTkEntry(self, width=200)
        self.partnumber_py.insert(0, partnumber.strip())
        self.partnumber_py.configure(state='readonly')
        self.partnumber_py.grid(row=0, column=1)

        self.revision_py = CTkEntry(self, width=200)
        self.revision_py.insert(0, revision.strip())
        self.revision_py.configure(state='readonly')
        self.revision_py.grid(row=1, column=1)

        self.localization = CTkEntry(self, width=200)
        self.localization.insert(0, localization.strip())
        self.localization.configure(state='readonly')
        self.localization.grid(row=2, column=1)
        self.new_localization_py = CTkEntry(self, width=200)
        self.new_localization_py.grid(row=3, column=1)

        self.new_localization_py.focus_set()

        adient_py_label = CTkLabel(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0)
        revision_py_label = CTkLabel(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)
        actual_loc_py_label = CTkLabel(self, text="Aktualna Lokalizacja: ")
        actual_loc_py_label.grid(row=2, column=0)
        new_loc_py_label = CTkLabel(self, text="Nowa lokalizacja: ")
        new_loc_py_label.grid(row=3, column=0)

        edit_btn = CTkButton(self, text="Przyjmij komponent", command=empty_fields)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)
