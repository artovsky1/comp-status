from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.functions import *
from commands.styles import *


class NewCompPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Nowy komponent")
        master.width, master.height = 400, 450

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

        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.partnumber_py = ttk.Entry(self, width=23)
        self.revision_py = ttk.Entry(self, width=23)
        self.description_py = ttk.Combobox(self, width=20, values=list_desc())
        self.description_py.bind('<KeyRelease>', lambda event: search_desc(self, event))
        self.project_py = ttk.Combobox(self, width=20, values=list_projects())
        self.project_py.bind('<KeyRelease>', lambda event: search_project(self, event))
        self.quantity_py = ttk.Entry(self, width=23)
        self.localization_py = ttk.Entry(self, width=23)

        self.partnumber_py.focus_set()

        self.partnumber_py_label = Label(self, text="Numer referencji: ", font=LabelFont, bg=BgColor)
        self.revision_py_label = Label(self, text="Rewizja: ", font=LabelFont, bg=BgColor)
        self.description_py_label = Label(self, text="Opis: ", font=LabelFont, bg=BgColor)
        self.project_py_label = Label(self, text="Projekt: ", font=LabelFont, bg=BgColor)
        self.quantity_py_label = Label(self, text="Ilość: ", font=LabelFont, bg=BgColor)
        self.localization_py_label = Label(self, text="Lokalizacja: ", font=LabelFont, bg=BgColor)

        self.edit_btn = Button(self, text="Dodaj Komponent", image=self.button_img, **ButtonSettings,
                               command=button_action)
        self.back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                               command=lambda: master.switch_frame(StartPage))

        Label(self, text="", bg=BgColor).grid(row=0, column=0, columnspan=2)

        self.partnumber_py_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')
        self.revision_py_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.description_py_label.grid(row=3, column=0, padx=10, pady=10, sticky='E')
        self.project_py_label.grid(row=4, column=0, padx=10, pady=10, sticky='E')
        self.quantity_py_label.grid(row=5, column=0, padx=10, pady=10, sticky='E')
        self.localization_py_label.grid(row=6, column=0, padx=10, pady=10, sticky='E')
        self.partnumber_py.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        self.revision_py.grid(row=2, column=1, padx=10, pady=10, sticky='W')
        self.description_py.grid(row=3, column=1, padx=10, pady=10, sticky='W')
        self.project_py.grid(row=4, column=1, padx=10, pady=10, sticky='W')
        self.quantity_py.grid(row=5, column=1, padx=10, pady=10, sticky='W')
        self.localization_py.grid(row=6, column=1, padx=10, pady=10, sticky='W')

        Label(self, text="", bg=BgColor).grid(row=3, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=9, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=10, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=11, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=12, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=13, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=14, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=15, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=16, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=17, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=18, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=19, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=20, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=21, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=22, column=0, columnspan=2)

        self.edit_btn.place(relx=0.8, rely=0.82, anchor='center')
        self.back_btn.place(relx=0.2, rely=0.82, anchor='center')

        entry_widgets = [self.partnumber_py, self.revision_py, self.description_py, self.project_py, self.quantity_py,
                         self.localization_py]
