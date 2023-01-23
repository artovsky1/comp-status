from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sql_commands import *
from customtkinter import *
from styles import *
import connection
from suggestions import *

class DeletePage(CTkFrame):

    def __init__(self, master):
        from StartPage import StartPage
        CTkFrame.__init__(self, master)
        style_delete_comp_page(master)
        conn = connection.connection()
        session = connection.session()

        def list_partnumber():
            result = session.execute(SELECT_LIST)
            result_list = [row[0].strip() for row in result]
            session.close()
            return result_list

        def list_revision():
            result = session.execute(SELECT_LIST_REV, {"partnumber": self.partnumber_py.get().strip()})
            result_list = [row[0].strip() for row in result]
            session.close()
            return result_list

        def update_partnumber_list(*args):
            self.partnumber_py["values"] = list_partnumber()

        def update_revision_list(*args):
            self.revision_py["values"] = list_revision()

        def lookup_comp():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip())
            result = conn.execute(SELECT_COMPONENT, values).fetchone()
            if result is not None:
                if messagebox.askyesno("Informacja", "Czy chcesz usunąć ten komponent?"):
                    conn.execute(DELETE_COMPONENT, values)
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

        def search(event):
            value = event.widget.get()
            if value == '':
                self.partnumber_py['values'] = list_partnumber()

            else:
                data = []

                for item in list_partnumber():
                    if value.lower() in item.lower():
                        data.append(item)
                    self.partnumber_py['values'] = data

        self.partnumber_py = ttk.Combobox(self, width=30, values=list_partnumber())
        self.partnumber_py.grid(row=0, column=1)
        self.partnumber_py.bind('<KeyRelease>', search)
        # self.partnumber_py.bind('<KeyRelease>', update_revision_list)
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=30, values=list_revision())
        self.revision_py.grid(row=1, column=1)

        self.partnumber_py.focus_set()

        adient_py_label = CTkLabel(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0)
        revision_py_label = CTkLabel(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)

        edit_btn = CTkButton(self, text="Usuń komponent", command=lookup_comp)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)

        entry_widgets = [self.partnumber_py, self.revision_py]
