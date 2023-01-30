from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *


class NewCompPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Nowy komponent")
        master.width = 800
        master.height = 600

        create_conn = connection()

        def button_action():
            if select_sql() is None:
                empty_fields()
            else:
                messagebox.showerror("Błąd", "Komponent z takim numerem i rewizją już istnieje")

        def select_sql():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            return create_conn.execute(SELECT_COMPONENT, values).fetchone()

        def empty_fields():
            if all(val != "" for val in (self.partnumber_py.get().strip(), self.revision_py.get().strip(),
                                         self.description_py.get().strip(), self.project_py.get().strip(),
                                         self.quantity_py.get().strip(), self.localization_py.get().strip())):
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
                if messagebox.askyesno("Informacja", "Czy chcesz dodać ten komponent?"):
                    sql_insert()
                    messagebox.showinfo("Powodzenie", "Komponent został dodany pomyślnie")
                    clear_entries()
            else:
                messagebox.showerror("Błąd", "Ilość nie może być ujemna")

        def sql_insert():
            values = (
                self.partnumber_py.get().strip(), self.revision_py.get().strip(), self.description_py.get().strip(),
                self.project_py.get().strip(), self.quantity_py.get().strip(), self.localization_py.get().strip())
            create_conn.execute(INSERT_COMPONENT, values)

        def clear_entries():
            if messagebox.askyesno("Informacja", "Czy chcesz dodać kolejny komponent?"):
                for entry in entry_widgets:
                    entry.delete(0, END)
            else:
                master.switch_frame(StartPage)

        self.partnumber_py = ttk.Entry(self)
        self.partnumber_py.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.revision_py = ttk.Entry(self)
        self.revision_py.grid(row=1, column=1)
        self.description_py = ttk.Combobox(self, values=['2D fleece', '3D fleece', 'PE insert', 'Wire',
                                                         'Frame', 'Clip',
                                                         'PUR insert', 'Hook tape', 'Cut foam',
                                                         'Sealing fleece',
                                                         'Spacer', 'Chip insert'], state='readonly')

        self.description_py.grid(row=2, column=1)
        self.project_py = ttk.Combobox(self, values=['Porsche G3', 'Opel OV', 'CDPO', 'Volvo GPA'],
                                       state='readonly')

        self.project_py.grid(row=3, column=1)
        self.quantity_py = ttk.Entry(self)
        self.quantity_py.grid(row=4, column=1)
        self.localization_py = ttk.Entry(self)
        self.localization_py.grid(row=5, column=1)

        self.partnumber_py.focus_set()

        adient_py_label = ttk.Label(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0, pady=(10, 0))
        revision_py_label = ttk.Label(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)
        description_py_label = ttk.Label(self, text="Opis: ")
        description_py_label.grid(row=2, column=0)
        project_py_label = ttk.Label(self, text="Projekt: ")
        project_py_label.grid(row=3, column=0)
        quantity_py_label = ttk.Label(self, text="Ilość: ")
        quantity_py_label.grid(row=4, column=0)
        localization_py_label = ttk.Label(self, text="Lokalizacja: ")
        localization_py_label.grid(row=5, column=0)

        edit_btn = ttk.Button(self, text="Dodaj Komponent", command=button_action)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = ttk.Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)

        entry_widgets = [self.partnumber_py, self.revision_py, self.description_py, self.project_py, self.quantity_py,
                         self.localization_py]
