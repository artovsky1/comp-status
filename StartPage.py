from customtkinter import *
from styles import *

class StartPage(CTkFrame):

    def __init__(self, master):
        CTkFrame.__init__(self, master)
        style_start_page(master)

        CTkLabel(self, text="Stan komponentów Launch").grid(row=0, column=0)

        button0 = CTkButton(self, text="Dodaj komponent",
                            command=lambda: master.switch_frame(NewCompPage))
        button0.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button1 = CTkButton(self, text="Modyfikuj komponent",
                            command=lambda: master.switch_frame(ModifyTempCompPage))
        button1.grid(row=1, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

        button2 = CTkButton(self, text="Usuń komponent", command=lambda: master.switch_frame(DeletePage))
        button2.grid(row=1, column=2, columnspan=1, pady=10, padx=10, ipadx=50)

        button3 = CTkButton(self, text="Przyjmij komponent",
                            command=lambda: master.switch_frame(BringBackCompPage))
        button3.grid(row=2, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button4 = CTkButton(self, text="Wydaj komponent",
                            command=lambda: master.switch_frame(BringCompPage))
        button4.grid(row=2, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

        button5 = CTkButton(self, text="Zmień lokalizację",
                            command=lambda: master.switch_frame(ChangeTempCompPage))
        button5.grid(row=2, column=2, columnspan=1, pady=10, padx=10, ipadx=50)

        button6 = CTkButton(self, text="Podgląd stanu", command=lambda: master.switch_frame(LookUpPage))
        button6.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

        button7 = CTkButton(self, text="Historia zmian", command=lambda: master.switch_frame(ChangeLog))
        button7.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx=50)