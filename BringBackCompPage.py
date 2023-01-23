from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sql_commands import *
from customtkinter import *
from styles import *
import connection
import suggestions


class BringBackCompPage(CTkFrame):

    def __init__(self, master):
        from StartPage import StartPage
        CTkFrame.__init__(self, master)
        style_bb_comp_page(master)
        conn = connection.connection()
        session = connection.session()


        def update_revision_list(*args):
            self.revision_py["values"] = suggestions.list_revision(self)

        def button_action():
            if select_sql() is not None:
                empty_fields()
            else:
                messagebox.showerror("Błąd", "Nie ma komponentu z takim numerem i rewizją")

        def select_sql():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            return conn.execute(SELECT_COMPONENT, values).fetchone()

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
                if messagebox.askyesno("Informacja", "Czy chcesz przyjąć ten komponent?"):
                    sql_update()
                    messagebox.showinfo("Powodzenie", "Komponent został przyjęty")
                    repeat()
            else:
                messagebox.showerror("Błąd", "Ilość nie może być ujemna")

        def sql_update():
            values = (self.quantity_py.get().strip(), self.partnumber_py.get().strip(), self.revision_py.get().strip())
            conn.execute(BRING_BACK_COMPONENT, values)

        def repeat():
            if messagebox.askyesno("Informacja", "Czy chcesz przyjąć kolejny komponent?"):
                for entry in entry_widgets:
                    entry.delete(0, END)
            else:
                master.switch_frame(StartPage)


        self.partnumber_py = ttk.Combobox(self, width=30, values=suggestions.list_partnumber())
        self.partnumber_py.grid(row=0, column=1)
        self.partnumber_py.bind('<KeyRelease>', lambda event: suggestions.search(self, event))
        # self.partnumber_py.bind('<KeyRelease>', update_revision_list)
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=30, values=suggestions.list_revision(self))
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

        edit_btn = CTkButton(self, text="Przyjmij komponent", command=button_action)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)

        entry_widgets = [self.partnumber_py, self.revision_py, self.quantity_py]
