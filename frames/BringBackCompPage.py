from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from commands.functions import *


class BringBackCompPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Przyjmij komponent")
        master.width, master.height = 360, 300

        create_conn = connection()

        def update_revision_list(*args):
            self.revision_py["values"] = list_revision(self)

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
                if messagebox.askyesno("Informacja", "Czy chcesz przyjąć ten komponent?"):
                    sql_update()
                    messagebox.showinfo("Powodzenie", "Komponent został przyjęty")
                    repeat()
            else:
                messagebox.showerror("Błąd", "Ilość nie może być ujemna")

        def sql_update():
            values = (self.quantity_py.get().strip(), self.partnumber_py.get().strip(), self.revision_py.get().strip())
            create_conn.execute(BRING_BACK_COMPONENT, values)

        def repeat():
            if messagebox.askyesno("Informacja", "Czy chcesz przyjąć kolejny komponent?"):
                for entry in entry_widgets:
                    entry.delete(0, END)
            else:
                master.switch_frame(StartPage)

        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.partnumber_py = ttk.Combobox(self, width=20, values=list_partnumber())
        self.partnumber_py.bind('<KeyRelease>', lambda event: search(self, event))
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=20, values=list_revision(self))
        self.quantity_py = ttk.Entry(self, width=23)

        self.partnumber_py.focus_set()

        self.partnumber_py_label = Label(self, text="Part number: ", font=LabelFont, bg=BgColor)
        self.revision_py_label = Label(self, text="Rewizja: ", font=LabelFont, bg=BgColor)
        self.quantity_py_label = Label(self, text="Ilość: ", font=LabelFont, bg=BgColor)

        self.edit_btn = Button(self, text="Przyjmij komponent", image=self.button_img, **ButtonSettings,
                               command=button_action)
        self.back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                               command=lambda: master.switch_frame(StartPage))

        Label(self, text="", bg=BgColor).grid(row=0, column=0, columnspan=2)

        self.partnumber_py_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')
        self.revision_py_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.quantity_py_label.grid(row=3, column=0, padx=10, pady=10, sticky='E')
        self.partnumber_py.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        self.revision_py.grid(row=2, column=1, padx=10, pady=10, sticky='W')
        self.quantity_py.grid(row=3, column=1, padx=10, pady=10, sticky='W')

        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=2)

        self.edit_btn.place(relx=0.77, rely=0.82, anchor='center')
        self.back_btn.place(relx=0.23, rely=0.82, anchor='center')

        entry_widgets = [self.partnumber_py, self.revision_py, self.quantity_py]
