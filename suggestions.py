import connection
from sql_commands import *
import ChangeTempCompPage

conn = connection.connection()
session = connection.session()


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
