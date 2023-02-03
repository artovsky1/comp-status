from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *
from frames.StartPage import *


class ChangeLog(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)
        create_session = session()
        self.config(bg=BgColor)
        master.title("Historia zmian")
        master.width, master.height = 850, 470
        self.button_img = PhotoImage(file=get_path("Button.png"))

        def a_search(*args):
            search_query = self.search_entry.get()
            result = create_session.execute(get_search_changelog(search_query))
            rows = result.fetchall()
            self.my_tree.delete(*self.my_tree.get_children())
            for row in rows:
                self.my_tree.insert("", "end", values=(*row,))
            create_session.close()

        '''self.previous_column = None
        self.previous_order = "ASC"'''

        '''def sort_treeview(column, order):
            search_query = self.search_entry.get()
            result = create_session.execute(get_sort_changelog(order, search_query))
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
                self.my_tree.insert("", "end", values=(*row,))'''

        style = ttk.Style()

        style.configure("Treeview", rowheight=25)

        self.pack(pady=30)

        sort_frame = ttk.Frame(self, relief="solid")
        sort_frame.pack()

        '''sort_var = StringVar()
        sort_var.set("Numer referencji")

        sort_options = {"": "", "id": "ID", "tstamp": "Data zmiany", "who": "Użytkownik", "old_val":
            "Stara wartość", "new_val": "Nowa wartość", "operation": "Operacja"}
        sort_dropdown = ttk.OptionMenu(sort_frame, sort_var, *sort_options.values())
        sort_dropdown.pack(side=LEFT, padx=25, pady=10)
        sort_dropdown.configure(width=15)'''

        self.partnumber_label = Label(sort_frame, text="Szukana wartość: ")
        self.partnumber_label.pack(side=LEFT, padx=15, pady=10)

        self.search_entry = ttk.Entry(sort_frame)
        self.search_entry.pack(side=LEFT, padx=15, pady=10)

        self.search_entry.bind('<KeyRelease>', a_search)

        tree_frame = ttk.Frame(self)
        tree_frame.pack()

        self.my_tree = ttk.Treeview(tree_frame, selectmode='extended')
        self.my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.my_tree.yview)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.my_tree.configure(yscrollcommand=self.tree_scroll.set)
        self.my_tree['columns'] = ("id", "tstamp", "who", "old_val", "new_val", "operation")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id", anchor=CENTER, width=30)
        self.my_tree.column("tstamp", anchor=CENTER, width=130)
        self.my_tree.column("who", anchor=CENTER, width=80)
        self.my_tree.column("old_val", anchor=CENTER)
        self.my_tree.column("new_val", anchor=CENTER)
        self.my_tree.column("operation", anchor=CENTER, width=80)
        self.my_tree.heading("id", text="ID", anchor=CENTER)
        self.my_tree.heading("tstamp", text="Data zmiany", anchor=CENTER)
        self.my_tree.heading("who", text="Użytkownik", anchor=CENTER)
        self.my_tree.heading("old_val", text="Stara wartość", anchor=CENTER)
        self.my_tree.heading("new_val", text="Nowa wartość", anchor=CENTER)
        self.my_tree.heading("operation", text="Czynność", anchor=CENTER)

        '''for col in self.my_tree['columns']:
            self.my_tree.heading(col, text=col.capitalize(), command=lambda c=col: sort_treeview(c, "ASC"))
            self.my_tree.heading(col, text=col.capitalize(), command=lambda c=col: sort_treeview(c, "DESC"))
'''
        back_btn = Button(self, text="Wróć", image=self.button_img, **ButtonSettings,
                          command=lambda: master.switch_frame(StartPage))
        back_btn.pack(side=BOTTOM, pady=10)

        results = create_session.execute(SELECT_ALL_CHANGELOG)
        all_rows = results.fetchall()
        for a_row in all_rows:
            self.my_tree.insert("", "end", values=(*a_row,))
        create_session.close()
