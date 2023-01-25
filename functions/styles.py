def style_login_page(master):
    master.title_name = "Logowanie"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_start_page(master):
    master.title_name = "Strona startowa"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_new_comp_page(master):
    master.title_name = "Nowy komponent"
    master.title(master.title_name)
    width, height = 500, 300
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_modify_comp_page(master):
    master.title_name = "Modyfikuj komponent"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_delete_comp_page(master):
    master.title_name = "Usuń komponent"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_bb_comp_page(master):
    master.title_name = "Przyjmij komponent"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_bring_comp_page(master):
    master.title_name = "Wydaj komponent"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_change_comp_page(master):
    master.title_name = "Zmiana lokalizacji komponentu"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_lookup_comp_page(master):
    master.title_name = "Podgląd stanu komponentów"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))


def style_changelog_comp_page(master):
    master.title_name = "Historia zmian"
    master.title(master.title_name)
    width, height = 800, 600
    x = (master.winfo_screenwidth() / 2) - (width / 2)
    y = (master.winfo_screenheight() / 2) - (height / 2)
    master.geometry("%dx%d+%d+%d" % (width, height, x, y))
