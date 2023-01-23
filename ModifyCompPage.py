class ModifyCompPage(CTkFrame):

    def __init__(self, master, partnumber, revision, description, project, quantity, localization):
        CTkFrame.__init__(self, master)
        style_modify_comp_page(master)

        def button_action():
            if select_sql() is None:
                empty_fields()
            else:
                messagebox.showerror("Błąd", "Komponent z takim numerem i rewizją już istnieje")

        def select_sql():
            values = (self.partnumber_py.get().strip(), self.revision_py.get().strip(), partnumber, revision)
            return conn.execute(SELECT_COMPONENT_EXCEPT, values).fetchone()

        def empty_fields():
            if all(val != "" for val in
                   (self.partnumber_py.get().strip(), self.revision_py.get().strip(),
                    self.description_py.get().strip(), self.project_py.get().strip(),
                    self.quantity_py.get().strip(), self.localization_py.get().strip())):
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
                if messagebox.askyesno("Informacja", "Czy chcesz modyfikować komponent?"):
                    sql_update()
                    messagebox.showinfo("Powodzenie", "Komponent zmodyfikowany pomyślnie")
                    clear_entries()
            else:
                messagebox.showerror("Błąd", "Ilość nie może być ujemna")

        def sql_update():
            values = (
                self.partnumber_py.get().strip(), self.revision_py.get().strip(), self.description_py.get().strip(),
                self.project_py.get().strip(), self.quantity_py.get().strip(), self.localization_py.get().strip(),
                partnumber, revision)
            conn.execute(UPDATE_COMPONENT, values)

        def clear_entries():
            if messagebox.askyesno("Informacja", "Czy chcesz modyfikować kolejny komponent?"):
                master.switch_frame(ModifyTempCompPage)
            else:
                master.switch_frame(StartPage)

        self.partnumber_py = CTkEntry(self, width=200)
        self.partnumber_py.insert(0, partnumber.strip())
        self.partnumber_py.grid(row=0, column=1)
        self.revision_py = CTkEntry(self, width=200)
        self.revision_py.insert(0, revision.strip())
        self.revision_py.grid(row=1, column=1)
        self.description_py = ttk.Combobox(self, values=['2D fleece', '3D fleece', 'PE insert', 'Wire',
                                                         'CTkFrame', 'Clip',
                                                         'PUR insert', 'Hook tape', 'Cut foam', 'Sealing fleece',
                                                         'Spacer',
                                                         'Chip insert'])
        self.description_py.insert(0, description.strip())
        self.description_py.grid(row=2, column=1)
        self.project_py = ttk.Combobox(self, values=['Porsche G3', 'Opel OV', 'CDPO', 'Volvo GPA'])
        self.project_py.insert(0, project.strip())  # Set the selected item to the first item in the list
        self.project_py.grid(row=3, column=1)
        self.quantity_py = CTkEntry(self, width=200)
        self.quantity_py.insert(0, quantity)
        self.quantity_py.grid(row=4, column=1)
        self.localization_py = CTkEntry(self, width=200)
        self.localization_py.insert(0, localization.strip())
        self.localization_py.grid(row=5, column=1)

        # Create text box labels
        adient_py_label = CTkLabel(self, text="Part number: ")
        adient_py_label.grid(row=0, column=0, pady=(10, 0))
        revision_py_label = CTkLabel(self, text="Rewizja: ")
        revision_py_label.grid(row=1, column=0)
        description_py_label = CTkLabel(self, text="Opis: ")
        description_py_label.grid(row=2, column=0)
        project_py_label = CTkLabel(self, text="Projekt: ")
        project_py_label.grid(row=3, column=0)
        quantity_py_label = CTkLabel(self, text="Stan: ")
        quantity_py_label.grid(row=4, column=0)
        localization_py_label = CTkLabel(self, text="Lokalizacja: ")
        localization_py_label.grid(row=5, column=0)

        # Create a update button
        edit_btn = CTkButton(self, text="Modyfikuj Komponent", command=button_action)
        edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

        # Create a back button
        back_btn = CTkButton(self, text="Wróć", command=lambda: master.switch_frame(StartPage))
        back_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=65)
