import datetime
import os
from tkinter import messagebox

from database.models.models import *

PATH = "database/tables/"

class Table:
    def __init__(self, name, model_name):
        self.name = name
        self.path = PATH + name + ".db"
        self.column_config = []
        self.id_counter = 0

        self.model_name = model_name
        self.model_class = globals()[model_name]

    def id_counter_refresh(self):
        file = open(self.path, "r")
        lines = file.readlines()
        if len(lines) > 0:
            last_line = lines[-1]
            last_ID = last_line.split(";")[0]
            self.id_counter = int(last_ID)

    def search_list(self, column, search_string) -> list[str] | bool:
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return args
        file.close()
        return False

    def search_line(self, column: str, search_string: str) -> str | bool:
        """
        Поиск строки в таблице БД по соответствию

        Args:
            column: Столбец для поиска
            search_string: Строка по которой производится поиск

        Returns:
            Строка таблицы БД или False в случае провала
        """
        file = open(self.path, "r")
        search_string = str(search_string)
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return line
        file.close()
        return False

    def search_model(self, column: str, search_string: str) -> Model | bool:
        """
        Поиск строки в таблице БД по соответствию с выводом модели

        Args:
            column: Столбец для поиска
            search_string: Строка по которой производится поиск

        Returns:
            Строка таблицы БД или False в случае провала
        """
        file = open(self.path, "r")
        search_string = str(search_string)
        for line in file.readlines():
            args = line.split(";")
            print(args)
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                item = self.model_class(args)
                return item
        file.close()
        return False

    def __get_all_lines(self) -> list[str]:
        """
        !Приватный метод!
        Возвращает список всех строк таблицы

        Returns:
            Список всех строк таблицы
        """
        file = open(self.path, "r")
        lines = file.readlines()
        return lines

    def get_all(self) -> list[Model]:
        """
        Получает список всех обьектов данной таблицы и переводит их список обьектов класса модели (Название класса модели инициализируются конструктором)

        Returns:
            Список обьектов модели таблицы
        """
        file = open(self.path, "r")
        lines = file.readlines()
        models = []
        for line in lines:
            args = line.split(";")
            models.append(self.model_class(args))
        return models

    def get_all_where(self, column: str, text: str) -> list[Model]:
        """
        Получает список всех обьектов данной таблицы и переводит их список обьектов класса модели (Название класса модели инициализируются конструктором)
        Обьекты фильтруются и передаются только те, где column == text

        Args:
            column: Название столбца
            text: Содержание для сравнения

        Returns:
            Список обьектов модели таблицы, где column == text

        """
        lines = self.__get_all_lines()
        models = []
        for line in lines:
            args = line.split(";")
            if args[self.column_config.index(column)] == text:
                models.append(self.model_class(line))
        return models

    def delete_by_id(self, id):
        lines = self.__get_all_lines()
        del_line = self.search_line("ID", id)
        if type(del_line) == bool:
            raise Exception("Обьект по ID не найден")
        del_line = del_line.strip()
        file = open(self.path, "w")
        for line in lines:
            if line.strip("\n") != del_line:
                file.write(line)
        file.close()

    def add_record(self,record):
        self.id_counter_refresh()
        file = open(self.path, "a")
        record = record.replace("\n", r"\\n")
        write_string = str(self.id_counter + 1) + ";" + record + "\n"
        file.write(write_string)

    def alter_record(self, id, column, text):
        lines = self.__get_all_lines()
        isAltered = False
        alter_line = self.search_line("ID", id)
        if not alter_line:
            print("SEARCH FAIL: NON-EXISTENT ID")

        else:
            file = open(self.path, "w")
            for line in lines:
                if line != alter_line:
                    file.write(line)

                else:
                    args = alter_line.split(";")
                    args.pop(-1)
                    print(self.column_config.index(column))
                    args[self.column_config.index(column)] = text
                    outline = ""
                    for arg in args:
                        outline += str(arg) + ";"
                    isAltered = True
                    outline = outline.replace("\n", r"\\n")
                    outline += "\n"
                    file.write(outline)
        if not isAltered:
            print("DEBUG: ALTER FAIL (ID:", id, ",COLUMN:", column, "TEXT:",text)






#   <--------Tables Declaration--------->

users_table = Table("users", "UserModel")
users_table.column_config = ["ID", "Login", "Password", "Role", "FullName", "Info", "CrewmemberID"]

directions_table = Table("directions", "DirectionModel")
directions_table.column_config = ["ID", "From", "To"]

planes_table = Table("planes", "PlaneModel")
planes_table.column_config = ["ID", "Brand", "Model", "BoardNum", "IsFlying", "IsRepaired", "Malfunction", "ImagePath", "IsBinded"]

crewmembers_table = Table("crewmembers", "CrewmemberModel")
crewmembers_table.column_config = ["ID", "Type" ,"FullName", "Info", "CrewID", "IsOccupied", "isRetired", "FlightID" , "ImagePath", "FliesType", "IsBindedToCrew", "IsInFlight"]

flights_table = Table("flights", "FlightModel")
flights_table.column_config = ["ID", "PlaneID" ,"DateStart", "DateEnd", "DirectionID", "CrewID"]

crews_table = Table("crews", "CrewModel")
crews_table.column_config = ["ID", "Name", "PilotString" ,"StuardString", "IsOccupied"]

#   <--------Tables Declaration--------->

class Response:
    frame_codes = {101: "AdminFrame", 400: ""}

    def __init__(self, code, full_name = ""):
        self.code = code
        self.fail = False
        self.full_name = full_name
        if code >= 200:
            self.fail = True

    def frame(self):
        return self.frame_codes[self.code]


class DB:
    def __init__(self):
        self.tables = {"users": users_table,
                       "directions": directions_table,
                       "planes": planes_table,
                       "crewmembers": crewmembers_table,
                       "flights" : flights_table,
                       "crews" : crews_table
                       }

    def is_record_present(self, table_name, column_name, record) -> bool:
        """
        Проверяет существует ли запись с такими параметрами в таблице

        Args:
            table_name: Название таблицы для поиска
            column_name: Название столбца по которому будет произведён поиск
            record: Текст поиска

        Returns:
            True или False
        """
        result = self.tables[table_name].search_list(column_name, record)
        if result:
            return True
        else:
            return False

    def is_login_available(self, login):
        answer = self.is_record_present("users", "Login", login)
        self.is_record_present()
        if answer:
            return False
        else:
            return True

    def authenticate(self, login, password):
        line = self.tables["users"].search_list("Login", login)
        if line:
            if line[self.tables["users"].column_config.index("Password")] == password:
                if line[self.tables["users"].column_config.index("Role")] == "admin":
                    return Response(101, line[self.tables["users"].column_config.index("FullName")])
            else:
                return Response(404)
        else:
            return Response(403)

    def get_all_from(self, table_name):
        return self.tables[table_name].get_all()

    def get_all_where(self, table_name, column, text):
        self.tables[table_name].get_all_where(column, text)

    def delete_by_id(self, table_name, id):
        self.tables[table_name].delete_by_id(id)

    def add_record(self, table_name, record):
        self.tables[table_name].add_record(record)

    def alter(self, table_name, id, column, text):
        self.tables[table_name].alter_record(id,column,text)

    def search_line(self, table_name, column, search_string):
        return self.tables[table_name].search_line(column, search_string)

    def search_list(self, table_name, column, search_string):
        return self.tables[table_name].search_list(column, search_string)

    def search_model(self, table_name, column, search_string) -> Model:
        return self.tables[table_name].search_model(column, search_string)

    def occupy_crew(self, crew_id):
        crew_model = self.tables["crews"].search_model("ID", crew_id)
        occupy_string = crew_model.pilotstring + crew_model.stuardstring
        occupy_list = occupy_string.split("|")
        occupy_list.pop(-1)
        for to_occupy in occupy_list:
            to_occupy = to_occupy.split(" ")[0]
            self.tables["crewmembers"].alter_record(to_occupy, "IsOccupied" , 1)


    def release_crew(self, crew_id):
        crew_model = self.tables["crews"].search_model("ID", crew_id)
        occupy_string = crew_model.pilotstring + crew_model.stuardstring
        occupy_list = occupy_string.split("|")
        occupy_list.pop(-1)
        for to_occupy in occupy_list:
            to_occupy = to_occupy.split(" ")[0]
            self.tables["crewmembers"].alter_record(to_occupy, "IsOccupied" , 0)

    def start_crew_fly(self, crew_id):
        crew_model = self.tables["crews"].search_model("ID", crew_id)
        occupy_string = crew_model.pilotstring + crew_model.stuardstring
        occupy_list = occupy_string.split("|")
        occupy_list.pop(-1)
        for to_occupy in occupy_list:
            to_occupy = to_occupy.split(" ")[0]
            self.tables["crewmembers"].alter_record(to_occupy, "IsInFlight", 1)

    def end_crew_fly(self, crew_id):
        crew_model = self.tables["crews"].search_model("ID", crew_id)
        occupy_string = crew_model.pilotstring + crew_model.stuardstring
        occupy_list = occupy_string.split("|")
        occupy_list.pop(-1)
        for to_occupy in occupy_list:
            to_occupy = to_occupy.split(" ")[0]
            self.tables["crewmembers"].alter_record(to_occupy, "IsInFlight", 0)
        self.tables["crews"].alter_record(crew_id, "IsOccupied", 0)

    def start_plane_fly(self, plane_id):
        self.alter("planes", str(plane_id), "IsFlying", 1)

    def end_plane_fly(self, plane_id):
        self.alter("planes", str(plane_id), "IsFlying", 0)
        self.alter("planes", str(plane_id), "IsBinded", 0)

    def refresh_current_flight_state(self):
        """
        Обновляет текущее состояние базы данных.
        Проверяются все рейсы, если какой-то рейс завершен, он удаляется из базы и экипаж высвобождается.
        Если какой-то рейс запланирован и начинается время его выполнения, самолёт помечается в полёте, также как и люди причастные экипажу.

        """
        flights = self.tables["flights"].get_all()
        for flight in flights:
            time_start_str = flight.date_start
            time_end_str = flight.date_end

            start_args_date = time_start_str.split(" ")[0].split(".")
            start_args_time = time_start_str.split(" ")[1].split(":")

            end_args_date = time_end_str.split(" ")[0].split(".")
            end_args_time = time_end_str.split(" ")[1].split(":")

            for i in range(len(end_args_date)):
                end_args_date[i] = int(end_args_date[i])
            for i in range(len(end_args_time)):
                end_args_time[i] = int(end_args_time[i])

            for i in range(len(start_args_date)):
                start_args_date[i] = int(start_args_date[i])
            for i in range(len(start_args_time)):
                start_args_time[i] = int(start_args_time[i])

            date_start = datetime.datetime(year=start_args_date[2], month=start_args_date[1], day=start_args_date[0],
                                           hour=start_args_time[0], minute=start_args_time[1])
            date_end = datetime.datetime(year=end_args_date[2], month=end_args_date[1],
                                         day=end_args_date[0], hour=end_args_time[0],
                                         minute=end_args_time[1])

            if ((date_start - datetime.datetime.now()).total_seconds() <= 0) and not ((date_end - datetime.datetime.now()).total_seconds() <= 0):
                self.start_crew_fly(flight.crewID)
                self.start_plane_fly(flight.planeID)
                messagebox.showinfo("Рейс", "Рейс начался")

            if ((date_end - datetime.datetime.now()).total_seconds() <= 0):
                self.release_crew(flight.crewID)
                self.end_crew_fly(flight.crewID)
                self.end_plane_fly(flight.planeID)


                self.delete_by_id("flights", flight.id)
                messagebox.showinfo("Рейс", "Рейс закончился")

