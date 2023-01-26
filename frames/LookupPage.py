from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *


class LookUpPage(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)
        style_lookup_comp_page(master)
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
        tree_scroll = Scrollbar(self)
        tree_scroll.pack(expand=True, fill='both')
        self.my_tree = ttk.Treeview(self, yscrollcommand=tree_scroll, selectmode='extended')
        self.my_tree.pack()
        'tree_scroll.config(command=self.my_tree.yview)'
        self.my_tree['columns'] = ("id", "partnumber", "revision", "description", "project", "quantity", "localization")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("partnumber", anchor=W, width=140)
        self.my_tree.column("revision", anchor=CENTER, width=140)
        self.my_tree.column("description", anchor=CENTER, width=140)
        self.my_tree.column("project", anchor=CENTER, width=140)
        self.my_tree.column("quantity", anchor=CENTER, width=140)
        self.my_tree.column("localization", anchor=CENTER, width=140)
        self.my_tree.heading("id", text="id", anchor=W)
        self.my_tree.heading("partnumber", text="partnumber", anchor=W)
        self.my_tree.heading("revision", text="revision", anchor=CENTER)
        self.my_tree.heading("description", text="description", anchor=CENTER)
        self.my_tree.heading("project", text="project", anchor=CENTER)
        self.my_tree.heading("quantity", text="quantity", anchor=CENTER)
        self.my_tree.heading("localization", text="localization", anchor=CENTER)

        back_btn = Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.pack()

        result = create_session.execute(SELECT_ALL)
        rows = result.fetchall()
        for row in rows:
            self.my_tree.insert("", "end", values=(*row,))
        create_session.close()
