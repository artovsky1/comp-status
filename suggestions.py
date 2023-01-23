def list_partnumber():
    result = session.execute(SELECT_LIST)
    result_list = [row[0].strip() for row in result]
    session.close()
    return result_list


def list_revision():
    result = session.execute(SELECT_LIST_REV, {"partnumber": self.partnumber_py.get().strip()})
    result_list = [row[0].strip() for row in result]
    session.close()
    return result_list


def update_partnumber_list(*args):
    self.partnumber_py["values"] = list_partnumber()


def update_revision_list(*args):
    self.revision_py["values"] = list_revision()
