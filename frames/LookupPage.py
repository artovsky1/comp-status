from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database.sql_commands import *
from database.connection import *
from commands.styles import *


class LookUpPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)

        def search():
            create_session = session()
            what_to_search = sort_var.get()
            search_query = self.search_entry.get()
            result = create_session.execute(f"SELECT * FROM component_status WHERE cast({what_to_search} as text) LIKE '%{search_query}%'")
            rows = result.fetchall()
            self.my_tree.delete(*self.my_tree.get_children())
            for row in rows:
                self.my_tree.insert("", "end", values=(*row,))
            create_session.close()

        def sort(order):
            create_session = session()
            search_query = sort_var.get()
            result = create_session.execute(f"SELECT * FROM component_status ORDER BY {search_query} {order}")
            rows = result.fetchall()
            self.my_tree.delete(*self.my_tree.get_children())
            for row in rows:
                self.my_tree.insert("", "end", values=(*row,))
            create_session.close()

        self.config(bg=BgColor)
        master.title("Podgląd stanu komponentów")
        master.width, master.height = 800, 600

        create_session = session()
        style = ttk.Style()

        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map(self, 'Treeview',
                  background=[('selected', '#347083')])

        self.pack(pady=10)

        tree_frame = ttk.Frame(self)
        tree_frame.pack()

        self.my_tree = ttk.Treeview(tree_frame, selectmode='extended')
        self.my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.my_tree.yview)
        tree_scroll.pack(side=RIGHT, fill=Y)
        self.my_tree.configure(yscrollcommand=tree_scroll.set)
        self.my_tree['columns'] = ("id", "partnumber", "revision", "description", "project", "quantity", "localization")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id", anchor=CENTER, width=30)
        self.my_tree.column("partnumber", anchor=CENTER, width=80)
        self.my_tree.column("revision", anchor=CENTER, width=80)
        self.my_tree.column("description", anchor=CENTER, width=160)
        self.my_tree.column("project", anchor=CENTER, width=100)
        self.my_tree.column("quantity", anchor=CENTER, width=80)
        self.my_tree.column("localization", anchor=CENTER, width=80)
        self.my_tree.heading("id", text="id", anchor=CENTER)
        self.my_tree.heading("partnumber", text="partnumber", anchor=CENTER)
        self.my_tree.heading("revision", text="revision", anchor=CENTER)
        self.my_tree.heading("description", text="description", anchor=CENTER)
        self.my_tree.heading("project", text="project", anchor=CENTER)
        self.my_tree.heading("quantity", text="quantity", anchor=CENTER)
        self.my_tree.heading("localization", text="localization", anchor=CENTER)

        back_btn = Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.pack(side=BOTTOM, pady=20)

        result = create_session.execute(SELECT_ALL)
        rows = result.fetchall()
        for row in rows:
            self.my_tree.insert("", "end", values=(*row,))
        create_session.close()

        search_frame = ttk.Frame(self)
        search_frame.pack()

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side=LEFT, padx=5)

        search_btn = ttk.Button(search_frame, text="Szukaj", command=search)
        search_btn.pack(side=LEFT, padx=5)

        sort_frame = ttk.Frame(self)
        sort_frame.pack()

        sort_var = StringVar()
        sort_var.set("id")

        sort_options = ["", "id", "partnumber", "revision", "description", "project", "quantity", "localization"]
        sort_dropdown = ttk.OptionMenu(sort_frame, sort_var, *sort_options)
        sort_dropdown.pack(side=LEFT)

        asc_sort_btn = ttk.Button(sort_frame, text="Sortuj Rosnąco", command=lambda: sort("ASC"))
        asc_sort_btn.pack(side=LEFT, padx=5)

        desc_sort_btn = ttk.Button(sort_frame, text="Sortuj Malejąco", command=lambda: sort("DESC"))
        desc_sort_btn.pack(side=LEFT, padx=5)
