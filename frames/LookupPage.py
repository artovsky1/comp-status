from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from frames.StartPage import *


class LookUpPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)
        session = create_session()
        self.config(bg=BgColor)
        master.title("Podgląd stanu komponentów")
        master.width, master.height = 730, 470
        self.button_img = PhotoImage(file=get_path("Button.png"))

        def a_search(*args):
            what_to_search = [k for k, v in sort_options.items() if v == sort_var.get()][0]
            search_query = self.search_entry.get()
            result = session.execute(get_search_query(what_to_search, search_query))
            rows = result.fetchall()
            self.my_tree.delete(*self.my_tree.get_children())
            for row in rows:
                self.my_tree.insert("", "end", values=(*row,))
            session.close()

        self.previous_column = None
        self.previous_order = "ASC"

        def sort_treeview(column, order):
            what_to_search = [k for k, v in sort_options.items() if v == sort_var.get()][0]
            search_query = self.search_entry.get()
            result = session.execute(get_sort_query(what_to_search, order, search_query))
            rows = result.fetchall()
            self.my_tree.delete(*self.my_tree.get_children())

            # Keep track of the order of the previous sort
            if self.previous_column == column:
                if self.previous_order == "ASC":
                    order = "DESC"
                else:
                    order = "ASC"
            self.previous_column = column
            self.previous_order = order

            if order == "DESC":
                reverse_order = True
            else:
                reverse_order = False
            sorted_rows = sorted(rows, key=lambda row_a: row_a[self.my_tree['columns'].index(column)],
                                 reverse=reverse_order)
            for row in sorted_rows:
                self.my_tree.insert("", "end", values=(*row,))
            session.close()

        style = ttk.Style()

        style.configure("Treeview", rowheight=25)

        self.pack(pady=30)

        sort_frame = ttk.Frame(self, relief="solid")
        sort_frame.pack()

        sort_var = StringVar()
        sort_var.set("Numer referencji")

        sort_options = {"": "", "id": "ID", "partnumber": "Numer referencji", "revision": "Rewizja", "description":
                        "Opis", "project": "Projekt", "quantity": "Ilość", "localization": "Lokalizacja"}
        sort_dropdown = ttk.OptionMenu(sort_frame, sort_var, *sort_options.values())
        sort_dropdown.pack(side=LEFT, padx=25, pady=10)
        sort_dropdown.configure(width=15)

        self.search_entry = ttk.Entry(sort_frame)
        self.search_entry.pack(side=LEFT, padx=25, pady=10)

        self.search_entry.bind('<KeyRelease>', a_search)

        tree_frame = ttk.Frame(self)
        tree_frame.pack()

        self.my_tree = ttk.Treeview(tree_frame, selectmode='extended')
        self.my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.my_tree.yview)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.my_tree.configure(yscrollcommand=self.tree_scroll.set)
        self.my_tree['columns'] = ("id", "partnumber", "revision", "description", "project", "quantity", "localization")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id", anchor=CENTER, width=30)
        self.my_tree.column("partnumber", anchor=CENTER, width=110)
        self.my_tree.column("revision", anchor=CENTER, width=60)
        self.my_tree.column("description", anchor=CENTER, width=160)
        self.my_tree.column("project", anchor=CENTER, width=100)
        self.my_tree.column("quantity", anchor=CENTER, width=70)
        self.my_tree.column("localization", anchor=CENTER, width=80)
        self.my_tree.heading("id", text="ID", anchor=CENTER)
        self.my_tree.heading("partnumber", text="Numer referencji", anchor=CENTER)
        self.my_tree.heading("revision", text="Rewizja", anchor=CENTER)
        self.my_tree.heading("description", text="Opis", anchor=CENTER)
        self.my_tree.heading("project", text="Projekt", anchor=CENTER)
        self.my_tree.heading("quantity", text="Ilość", anchor=CENTER)
        self.my_tree.heading("localization", text="Lokalizacja", anchor=CENTER)

        for col in self.my_tree['columns']:
            self.my_tree.heading(col, text=col.capitalize(), command=lambda c=col: sort_treeview(c, "ASC"))
            self.my_tree.heading(col, text=col.capitalize(), command=lambda c=col: sort_treeview(c, "DESC"))

        back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                          command=lambda: master.switch_frame(StartPage))
        back_btn.pack(side=BOTTOM, pady=10)

        results = session.execute(SELECT_ALL)
        all_rows = results.fetchall()
        for a_row in all_rows:
            self.my_tree.insert("", "end", values=(*a_row,))
        session.close()
