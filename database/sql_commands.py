# Login page
SELECT_LOGIN = "SELECT username FROM user_data WHERE username = ?"
SELECT_PASSWORD = "SELECT username, password FROM user_data WHERE username = ? AND password = ?"

# New page commands
SELECT_COMPONENT = "SELECT partnumber, revision FROM stan_komponentow WHERE partnumber = ? AND revision = ?"
INSERT_COMPONENT = "INSERT INTO stan_komponentow (partnumber, revision, description, project, quantity, localization) " \
                   "VALUES (?, ?, ?, ?, ?, ?)"

# Modify temp page commands
SELECT_COMPONENT_ALL = "SELECT partnumber, revision, description, project, quantity, localization FROM " \
                       "stan_komponentow WHERE partnumber = ? AND revision = ?"

# Modify page commands
SELECT_COMPONENT_EXCEPT = "SELECT partnumber, revision FROM stan_komponentow WHERE partnumber = ? AND revision = ? " \
                          "EXCEPT SELECT partnumber, revision FROM stan_komponentow WHERE partnumber = ? AND revision " \
                          "= ?"
UPDATE_COMPONENT = "UPDATE stan_komponentow SET partnumber =?, revision=?, description=?, project= ?, " \
                   "quantity=?, localization=? WHERE partnumber = ? " \
                   " AND revision = ?"

# Delete page commands
DELETE_COMPONENT = "DELETE FROM stan_komponentow WHERE partnumber = ? AND revision = ?"

# Bring back page commands
BRING_BACK_COMPONENT = "UPDATE stan_komponentow SET quantity = quantity + ? WHERE ? = " \
                       "partnumber AND ? = revision"

# Bring page commands
BRING_COMPONENT = "UPDATE stan_komponentow SET quantity = quantity - ? WHERE ? = " \
                  "partnumber AND ? = revision"
ACTUAL_QTY = "SELECT quantity FROM stan_komponentow WHERE partnumber = ? AND revision = ?" \
             ""
# Change temp page commands
SELECT_COMPONENT_LOC = "SELECT partnumber, revision, localization FROM stan_komponentow WHERE partnumber = " \
                       "? AND revision = ?"

# Change page commands
CHANGE_COMP_LOC = "UPDATE stan_komponentow SET localization = ? WHERE partnumber = ? " \
                  " AND revision = ?"

# Lookup commands
SELECT_ALL = "SELECT * FROM stan_komponentow ORDER BY id ASC"


def get_search_query(what_to_search, search_query):
    return f"SELECT * FROM stan_komponentow WHERE {what_to_search} LIKE '%{search_query}%'"


def get_sort_query(what_to_search, order, search_query):
    return f"SELECT * FROM stan_komponentow WHERE {what_to_search} LIKE '%{search_query}%' ORDER BY {what_to_search} {order}"


# Changelog commands
SELECT_ALL_CHANGELOG = 'SELECT id, CONVERT(VARCHAR, datetime, 20), hostname, old_value, new_value, action FROM komponentyLOG ORDER BY id DESC'



def get_search_changelog(search_query):
    return f"SELECT id, CONVERT(VARCHAR, datetime, 20), hostname, old_value, new_value, action FROM komponentyLOG WHERE old_value LIKE '%{search_query}%' OR new_value LIKE '%{search_query}%' ORDER BY id DESC"


# Auto Complete commands
SELECT_LIST = "SELECT DISTINCT(partnumber) FROM stan_komponentow ORDER BY partnumber ASC"
SELECT_LIST_REV = "SELECT DISTINCT(revision) FROM stan_komponentow WHERE partnumber LIKE '%' + :partnumber + '%' ORDER BY revision ASC"

# Project and desc list
DESC_LIST = "SELECT DISTINCT(description) FROM stan_komponentow ORDER BY description ASC"
PROJECT_LIST = "SELECT DISTINCT(project) FROM stan_komponentow ORDER BY project ASC"
