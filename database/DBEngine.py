import os


PATH = "database/tables/"

class Table:
    def __init__(self, name):
        self.name = name
        self.path = PATH + name + ".db"
        self.column_config = []

    def search(self, column, search_string):
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                return args
        return False

    def get_all(self):
        file = open(self.path, "r")
        return file.readlines()


#   <--------Tables Declaration--------->

users_table = Table("users")
users_table.column_config = ["Name", "Password", "Role"]

directions_table = Table("directions")
directions_table.column_config = ["ID", "From", "To"]

#   <--------Tables Declaration--------->

class Response:
    frame_codes = {101: "AdminFrame", 400: ""}
    def __init__(self, code):
        self.code = code
        self.fail = False
        if code >= 200:
            self.fail = True

    def frame(self):
        return self.frame_codes[self.code]


class DB:
    def __init__(self):
        self.tables = {"users": users_table, "directions": directions_table}

    def is_record_present(self, table_name, column_name, record):
        result = self.tables[table_name].search(column_name, record)
        if result:
            return True
        else:
            return False

    def is_login_available(self, login):
        answer = self.is_record_present("users", "Name", login)
        if answer:
            return False
        else:
            return True

    def authenticate(self, login, password):
        line = self.tables["users"].search("Name", login)
        if line:
            if line[1] == password:
                if line[2] == "admin":
                    return Response(101)
            else:
                return Response(404)
        else:
            return Response(403)

    def get_all_from(self, table_name):
        return self.tables[table_name].get_all()