from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functions.sql_commands import *
from functions.styles import *
from functions.connection import *


class ChangeLog(Frame):

    def __init__(self, master):
        from frames.StartPage import StartPage
        Frame.__init__(self, master)
        style_changelog_comp_page(master)
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
        self.my_tree['columns'] = ("id", "tstamp", "who", "old_val", "new_val", "operation")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id", anchor=W, width=140)
        self.my_tree.column("tstamp", anchor=W, width=140)
        self.my_tree.column("who", anchor=CENTER, width=140)
        self.my_tree.column("old_val", anchor=CENTER, width=140)
        self.my_tree.column("new_val", anchor=CENTER, width=140)
        self.my_tree.column("operation", anchor=CENTER, width=140)
        self.my_tree.heading("id", text="id", anchor=W)
        self.my_tree.heading("tstamp", text="datetime", anchor=W)
        self.my_tree.heading("who", text="hostname", anchor=CENTER)
        self.my_tree.heading("old_val", text="old_value", anchor=CENTER)
        self.my_tree.heading("new_val", text="new_value", anchor=CENTER)
        self.my_tree.heading("operation", text="action", anchor=CENTER)

        back_btn = Button(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.pack()

        result = create_session.execute(SELECT_ALL_CHANGELOG)
        rows = result.fetchall()
        for row in rows:
            self.my_tree.insert("", "end", values=(*row,))
        create_session.close()
