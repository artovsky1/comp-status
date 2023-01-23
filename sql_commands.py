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

# Change temp page commands
SELECT_COMPONENT_LOC = "SELECT partnumber, revision, localization FROM stan_komponentow WHERE partnumber = " \
                       "? AND revision = ?"

# Change page commands
CHANGE_COMP_LOC = "UPDATE stan_komponentow SET localization = ? WHERE partnumber = ? " \
                  " AND revision = ?"

# Lookup commands
SELECT_ALL = "SELECT * FROM stan_komponentow"

# Changelog commands
SELECT_ALL_CHANGELOG = "SELECT id, datetime, hostname, old_value, new_value, action FROM komponentyLOG"

# Auto Complete commands
SELECT_LIST = "SELECT DISTINCT(partnumber) FROM stan_komponentow"
SELECT_LIST_REV = "SELECT DISTINCT(revision) FROM stan_komponentow WHERE partnumber LIKE '%' + :partnumber + '%'"
