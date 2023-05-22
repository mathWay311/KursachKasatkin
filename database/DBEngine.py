import os


PATH = "database/tables/"

class Table:
    def __init__(self, name):
        self.name = name
        self.path = PATH + name + ".db"
        self.column_config = []
        self.id_counter = 0

    def id_counter_refresh(self):
        file = open(self.path, "r")
        lines = file.readlines()
        last_line = lines[-1]
        last_ID = last_line.split(";")[0]
        self.id_counter = int(last_ID)

    def search_list(self, column, search_string):
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return args
        file.close()
        return False

    def search_line(self, column, search_string):
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return line
        file.close()
        return False


    def get_all(self):
        file = open(self.path, "r")
        lines = file.readlines()
        file.close()
        return lines

    def delete_by_id(self, id):
        lines = self.get_all()
        del_line = self.search_line("ID", id).strip()
        file = open(self.path, "w")
        for line in lines:
            if line.strip("\n") != del_line:
                file.write(line)
        file.close()

    def add_record(self,record):
        print(record)
        self.id_counter_refresh()
        file = open(self.path, "a")
        write_string = str(self.id_counter + 1) + ";" + record + "\n"
        file.write(write_string)

    def alter_record(self, id, column, text):
        lines = self.get_all()
        file = open(self.path, "w")
        for line in lines:
            line = line.strip()
            args = line.split(";")
            if args[0] == id:
                args[self.column_config.index(column)] = text
            output = ""
            print(args)
            for arg in args:
                output+=str(arg) + ";"

            output += "\n"
            print(output)
            file.write(output)

        file.close()




#   <--------Tables Declaration--------->

users_table = Table("users")
users_table.column_config = ["Name", "Password", "Role"]

directions_table = Table("directions")
directions_table.column_config = ["ID", "From", "To"]

planes_table = Table("planes")
planes_table.column_config = ["ID", "Brand", "Model", "BoardNum", "IsOccupied", "IsRepaired", "Malfunction", "ImagePath"]

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
        self.tables = {"users": users_table,
                       "directions": directions_table,
                       "planes": planes_table
                       }

    def is_record_present(self, table_name, column_name, record):
        result = self.tables[table_name].search_list(column_name, record)
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
        line = self.tables["users"].search_list("Name", login)
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

    def delete_by_id(self, table_name, id):
        self.tables[table_name].delete_by_id(id)

    def add_record(self, table_name, record):
        self.tables[table_name].add_record(record)

    def alter(self, table_name, id, column, text):
        self.tables[table_name].alter_record(id,column,text)