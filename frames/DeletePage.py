from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from commands.functions import *


class DeletePage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        self.config(bg=BgColor)
        master.title("Usuń komponent")
        master.width, master.height = 350, 250

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

        self.button_img = PhotoImage(file=get_path("Button.png"))

        self.partnumber_py = ttk.Combobox(self, width=20, values=list_partnumber())

        self.partnumber_py.bind('<KeyRelease>', lambda event: search(self, event))
        # self.partnumber_py.bind('<KeyRelease>', update_revision_list)
        self.partnumber_py.bind("<FocusOut>", update_revision_list)
        self.partnumber_py.bind("<<ComboboxSelected>>", update_revision_list)
        self.partnumber_py.bind("<Return>", update_revision_list)
        self.revision_py = ttk.Combobox(self, width=20, values=list_revision(self))

        self.partnumber_py.focus_set()

        Label(self, text="", bg=BgColor).grid(row=0, column=0, columnspan=2)

        self.partnumber_py_label = Label(self, text="Part number: ", font=LabelFont, bg=BgColor)
        self.revision_py_label = Label(self, text="Rewizja: ", font=LabelFont, bg=BgColor)
        self.edit_btn = Button(self, text="Usuń komponent", image=self.button_img, **ButtonSettings,
                                   command=lookup_comp)
        self.back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                                   command=lambda: master.switch_frame(StartPage))

        entry_widgets = [self.partnumber_py, self.revision_py]

        self.partnumber_py_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')
        self.revision_py_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.partnumber_py.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        self.revision_py.grid(row=2, column=1, padx=10, pady=10, sticky='W')

        Label(self, text="", bg=BgColor).grid(row=3, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=4, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=5, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=6, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=7, column=0, columnspan=2)
        Label(self, text="", bg=BgColor).grid(row=8, column=0, columnspan=2)

        self.edit_btn.place(relx=0.75, rely=0.75, anchor='center')
        self.back_btn.place(relx=0.25, rely=0.75, anchor='center')
