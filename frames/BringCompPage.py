from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
<<<<<<< HEAD:frames/BringCompPage.py
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *
from functions.suggestions import *
=======
from styles import *
import connection
import suggestions
>>>>>>> 0d7faac51f4648ea3a88ec37507c14b08e8fa3a9:BringCompPage.py


class BringCompPage(CTkFrame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        CTkFrame.__init__(self, master)
        style_bring_comp_page(master)
<<<<<<< HEAD:frames/BringCompPage.py
        create_conn = connection()

        def update_revision_list(*args):
            self.revision_py["values"] = list_revision(self)
=======
        conn = connection.connection()
        session = connection.session()

        def update_revision_list(*args):
            self.revision_py["values"] = suggestions.list_revision(self)
>>>>>>> 0d7faac51f4648ea3a88ec37507c14b08e8fa3a9:BringCompPage.py

        def button_action():
            if select_sql() is not None:
                empty_fields()
            else:
                messagebox.showerror("Błąd", "Nie ma komponentu z takim numerem i rewizją")

        def select_sql():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            return create_conn.execute(SELECT_COMPONENT, values).fetchone()

        def empty_fields():
            if all(val != "" for val in (self.partnumber_py.get().strip(), self.revision_py.get().strip(),
                                         self.quantity_py.get().strip())):
                quantity_number()
            else:
                messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione")

        def quantity_number():
            if self.quantity_py.get().strip().isdigit():
                positive_quantity()
            else:
                messagebox.showerror("Błąd", "Ilość musi być liczbą")

        def positive_quantity():
            if self.quantity_py.get().strip() >= '0':
                if messagebox.askyesno("Informacja", "Czy chcesz wydać ten komponent?"):
                    sql_update()
                    messagebox.showinfo("Powodzenie", "Komponent został wydany")
                    repeat()
            else:
                messagebox.showerror("Błąd", "Ilość nie może być ujemna")

        def sql_update():
            values = (self.quantity_py.get().strip(), self.partnumber_py.get().strip(), self.revision_py.get().strip())
            create_conn.execute(BRING_COMPONENT, values)

        def repeat():
            if messagebox.askyesno("Informacja", "Czy chcesz wydać kolejny komponent?"):
                for entry in entry_widgets:
                    entry.delete(0, END)
            else:
                master.switch_frame(StartPage)

<<<<<<< HEAD:frames/BringCompPage.py
        self.partnumber_py = ttk.Combobox(self, width=30, values=list_partnumber())
        self.partnumber_py.grid(row=0, column=1)
        self.partnumber_py.bind('<KeyRelease>', lambda event: search(self, event))
=======
        self.partnumber_py = ttk.Combobox(self, width=30, values=suggestions.list_partnumber())
        self.partnumber_py.grid(row=0, column=1)
        self.partnumber_py.bind('<KeyRelease>', lambda event: suggestions.search(self, event))
>>>>>>> 0d7faac51f4648ea3a88ec37507c14b08e8fa3a9:BringCompPage.py
        # self.partnumber_py.bind('<KeyRelease>', update_revision_list)
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
<<<<<<< HEAD:frames/BringCompPage.py
        self.revision_py = ttk.Combobox(self, width=30, values=list_revision(self))
=======
        self.revision_py = ttk.Combobox(self, width=30, values=suggestions.list_revision(self))
>>>>>>> 0d7faac51f4648ea3a88ec37507c14b08e8fa3a9:BringCompPage.py
        self.revision_py.grid(row=1, column=1)
        self.quantity_py = CTkEntry(self, width=200)
        self.quantity_py.grid(row=4, column=1)

        self.partnumber_py.focus_set()

        adient_py_label = CTkLabel(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0, pady=(10, 0))
        revision_py_label = CTkLabel(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)
        quantity_py_label = CTkLabel(self, text="Ilość: ")
        quantity_py_label.grid(row=4, column=0)

        edit_btn = CTkButton(self, text="Wydaj komponent", command=button_action)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)

        entry_widgets = [self.partnumber_py, self.revision_py, self.quantity_py]
