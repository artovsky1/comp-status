from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *
from functions.suggestions import *


class DeletePage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Usuń komponent")
        master.width, master.height = 800, 600

        create_conn = connection()

        def update_partnumber_list(*args):
            self.partnumber_py["values"] = list_partnumber()

        def update_revision_list(*args):
            self.revision_py["values"] = list_revision(self)

        def lookup_comp():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            result = create_conn.execute(SELECT_COMPONENT, values).fetchone()
            if result is not None:
                if messagebox.askyesno("Informacja", "Czy chcesz usunąć ten komponent?"):
                    create_conn.execute(DELETE_COMPONENT, values)
                    messagebox.showinfo("Powodzenie", "Komponent został usunięty")
                    clear_entries()
            else:
                messagebox.showerror("Błąd", "Nie ma komponentu z takim numerem i rewizją")

        def clear_entries():
            if messagebox.askyesno("Informacja", "Czy chcesz usunąć jeszcze jakiś komponent?"):
                for entry in entry_widgets:
                    entry.delete(0, END)
                    update_partnumber_list()
            else:
                master.switch_frame(StartPage)

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

        adient_py_label = ttk.Label(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0)
        revision_py_label = ttk.Label(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)

        edit_btn = ttk.Button(self, text="Usuń komponent", command=lookup_comp)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = ttk.Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)

        entry_widgets = [self.partnumber_py, self.revision_py]
