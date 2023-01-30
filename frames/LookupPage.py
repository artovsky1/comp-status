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
