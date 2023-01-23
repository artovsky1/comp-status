# sql_commands for postgres

# Login page
SELECT_LOGIN = "SELECT username FROM user_data WHERE username = (%s)"
SELECT_PASSWORD = "SELECT username, password FROM user_data WHERE username = (%s) AND password = (%s)"

# New page commands
SELECT_COMPONENT = "SELECT partnumber, revision FROM component_status WHERE partnumber = (%s) AND revision = (%s)"
INSERT_COMPONENT = "INSERT INTO component_status (partnumber, revision, description, project, quantity, localization) " \
                   "VALUES ((%s), (%s), (%s), (%s), (%s), (%s))"

# Modify temp page commands
SELECT_COMPONENT_ALL = "SELECT partnumber, revision, description, project, quantity, localization FROM " \
                       "component_status WHERE partnumber = (%s) AND revision = (%s)"

# Modify page commands
SELECT_COMPONENT_EXCEPT = "SELECT partnumber, revision FROM component_status WHERE partnumber = (%s) AND revision = (%s) " \
                          "EXCEPT SELECT partnumber, revision FROM component_status WHERE partnumber = (%s) AND revision " \
                          "= (%s)"
UPDATE_COMPONENT = "UPDATE component_status SET partnumber =(%s), revision=(%s), description=(%s), project= (%s), " \
                   "quantity=(%s), localization=(%s) WHERE partnumber = (%s) " \
                   " AND revision = (%s)"

# Delete page commands
DELETE_COMPONENT = "DELETE FROM component_status WHERE partnumber = (%s) AND revision = (%s)"

# Bring back page commands
BRING_BACK_COMPONENT = "UPDATE component_status SET quantity = quantity + (%s) WHERE (%s) = " \
                       "partnumber AND (%s) = revision"

# Bring page commands
BRING_COMPONENT = "UPDATE component_status SET quantity = quantity - (%s) WHERE (%s) = " \
                  "partnumber AND (%s) = revision"

# Change temp page commands
SELECT_COMPONENT_LOC = "SELECT partnumber, revision, localization FROM component_status WHERE partnumber = " \
                       "(%s) AND revision = (%s)"

# Change page commands
CHANGE_COMP_LOC = "UPDATE component_status SET localization = (%s) WHERE partnumber = (%s) " \
                  " AND revision = (%s)"

# Lookup commands
SELECT_ALL = "SELECT * FROM component_status"

# Changelog commands
SELECT_ALL_CHANGELOG = "SELECT id, tstamp, who, old_val, new_val, operation FROM t_history"

# Auto Complete commands
SELECT_LIST = "SELECT DISTINCT(partnumber) FROM component_status"
SELECT_LIST_REV = "SELECT DISTINCT(revision) FROM component_status WHERE partnumber LIKE :partnumber"
