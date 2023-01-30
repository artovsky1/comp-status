from database.connection import *
from database.sql_commands import *
import os
import sys

conn = connection()
session = session()


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename


def list_partnumber():
    result = session.execute(SELECT_LIST)
    result_list = [row[0].strip() for row in result]
    session.close()
    return result_list


def list_revision(self):
    result = session.execute(SELECT_LIST_REV, {"partnumber": self.partnumber_py.get().strip()})
    result_list = [row[0].strip() for row in result]
    session.close()
    return result_list


def search(self, event):
    value = event.widget.get()
    if value == '':
        self.partnumber_py['values'] = list_partnumber()

    else:
        data = []

        for item in list_partnumber():
            if value.lower() in item.lower():
                data.append(item)
            self.partnumber_py['values'] = data
