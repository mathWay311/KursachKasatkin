from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame
from frames.test_frame import TestFrame
from frames.admin_frame import AdminFrame
from frames.utility.direction import Direction
import database.DBEngine as db
import content_gen
from frames.scrollable_Frame import ScrollableFrame
from frames.utility.add_frames import *

from frames.utility.plane import *
from frames.utility.crewmember import *
from frames.utility.user import *
from frames.utility.crew import *
from frames.utility.flight import *

from frames.utility.detail_frames import *


from database.models.models import *

from tkinter import messagebox
import customtkinter as tk


class WinController():
    def __init__(self, root):
        self.db = db.DB()
        self.root = root
        self.showed_frame = ""

        self.title_dict = {
            "AuthFrame": "G7 Airlines - Авторизация",
            "PilotFrame": "Окно пилота",
            "AdminFrame": "Администратор",
            "TestFrame": "Debug"
        }

        self.roles_dict = {
            "Администратор" : "admin", "Менеджер Рейсов": "flight_manager", "Менеджер ЛС": "crew_manager", "Менеджер ВС": "plane_manager", "Пилот/Стюардесса": "pilot"
        }
        self.types_dict = {
            "Пилот": "pilot", "Стюардесса": "stuard"
        }

        self.showed_frame = AuthFrame(root, self)
        self.showed_frame.create_widgets(self)

        self.current_content = ""


    def switch_to_frame(self, frame_name_show : str):
        """
        Переключает отображаемый фрейм по названию
        Args:
            frame_name_show :
                Наименование фрейма для переключения
        """
        self.showed_frame.destroy()
        if frame_name_show in self.title_dict.keys():
            frame_class = globals()[frame_name_show]
            self.showed_frame = frame_class(self.root,self)
            self.showed_frame.create_widgets(self)
            self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title : str):
        self.root.title(title)

    #   <--------GENERIC---------->

    def delete_item_by_id(self, table_name : str, id : str):
        """
        Удалить предмет по ID и закрыть окно

        Args:
            table_name:
                Наименование таблицы в формате "table"
            id:
                Идентификатор предмета для удаления
        """
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.db.delete_by_id(table_name, id)
            self.temporary_window.destroy()
            self.refresh()


    def delete_by_id(self, table, id):
        """
        Удалить предмет по ID без закрытия текущего окна (в случае если кнопка удалить не находится внутри временного окна)

        Args:
            table:
                Наименование таблицы в формате, например "users"
            id:
                Идентификатор предмета для удаления
        """
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.db.delete_by_id(table, id)
            self.refresh()


    def refresh(self):
        self.populate_panel_with_content(self.current_content)


    def open_add_record_window(self):
        """
        Открыть новое окно для добавления нового обьекта в базу
        """
        if self.current_content == "directions":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddDirectionFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)
        if self.current_content == "users":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddUserFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)
        if self.current_content == "crewmembers":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddCrewMemberFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)
        if self.current_content == "planes":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddPlaneFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)
        if self.current_content == "crews":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddCrewFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)
        if self.current_content == "flights":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddFlightFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)


    def populate_panel_with_content(self, content_name):
        """
        Заполнить поле для контента обьектами из базы

        Args:
            content_name:
                Название контента для заполнения в формате "table", то есть то же имя, что и у файла таблицы БД
        """
        self.current_content = content_name
        models = self.db.get_all_from(content_name)
        self.showed_frame.content_panel.destroy()
        self.showed_frame.content_panel = ScrollableFrame(self.showed_frame)
        scrollbar = tk.CTkScrollbar

        for model in models:
            if content_name == "directions":
                dir = Direction(model, self, self.showed_frame.content_panel.scrollable_frame)

            if content_name == "planes":
                plane = Plane(model, self, self.showed_frame.content_panel.scrollable_frame)

            if content_name == "crewmembers":
                crewmember = Crewmember(model, self, self.showed_frame.content_panel.scrollable_frame)
            if content_name == "users":
                user = User(model, self, self.showed_frame.content_panel.scrollable_frame)

            if content_name == "crews":
                crew = Crew(model, self, self.showed_frame.content_panel.scrollable_frame)

            if content_name == "flights":
                flight_text = self.db.search_list("crews", "ID", str(model.crewID))
                model.crewName = flight_text[1]

                plane_text = self.db.search_list("planes", "ID", str(model.planeID))
                model.planeName = plane_text[1] + plane_text[2]

                dir_text = self.db.search_list("directions", "ID", str(model.directionID))
                model.dirName = dir_text[1] + " - " + dir_text[2]

                fli = Flight(model, self, self.showed_frame.content_panel.scrollable_frame)

        self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

    #   <--------GENERIC---------->

    #   <--------FRAME SPECIFIC METHODS---------->
    #       <--------AUTH---------->

    def authframe_login_submit(self):
        """
        Подтверждение входа (по нажатию кнопки ВХОД)
        """
        login = self.showed_frame.field_login.get()
        password = self.showed_frame.field_password.get()
        response = self.db.authenticate(login, password)
        if not response.fail:
            self.switch_to_frame(response.frame())
            self.showed_frame.label_name.configure(text = response.full_name)
        else:
            messagebox.showerror("Ошибка","Такого пользователя не существует, или пароль неверный")

    #       <--------AUTH---------->

    #       <--------DIRECTIONS---------->

    def add_direction(self):
        """
        Добавить направление
        """
        _from = self.temporary_window_frame.entry_from.get()
        _to = self.temporary_window_frame.entry_to.get()
        self.db.add_record("directions", _from + ";" + _to)
        self.refresh()

    def get_available_directions(self) -> list[DirectionModel]:
        models = self.db.get_all_from("directions")
        output = []
        for model in models:
            output.append(model)
        return output

    #       <--------DIRECTIONS---------->



    #       <--------PLANES---------->
    def open_plane_details(self, plane_model : PlaneModel):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = PlaneDetail(plane_model)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def place_plane_on_repair(self, id):
        malfunction_text = self.temporary_window_frame.malfunction_entry_field.get("1.0", tk.END)
        self.db.alter("planes", str(id), "Malfunction", malfunction_text)
        self.db.alter("planes", str(id), "IsRepaired", 1)
        self.temporary_window.destroy()
        self.refresh()

    def retrieve_plane_from_repair(self, id):
        self.db.alter("planes", str(id), "Malfunction", "")
        self.db.alter("planes", str(id), "IsRepaired", 0)
        self.temporary_window.destroy()
        self.refresh()

    def add_plane(self):
        _brand = self.temporary_window_frame.dropdown_brand.get()
        _model = self.temporary_window_frame.dropdown_type.get()
        _boardnum = self.temporary_window_frame.entry_boardnum.get()
        _picpath = self.temporary_window_frame.entry_picpath.get()
        self.db.add_record("planes",
                           _brand + ";" + _model + ";" + _boardnum + ";0;0;;" + _picpath + ";")
        self.refresh()

    def get_available_planes(self) -> list[PlaneModel]:
        models = self.db.get_all_from("planes")
        output = []
        for model in models:
            if not model.isBinded:
                output.append(model)
        return output
    #       <--------PLANES---------->



    #       <--------CREWMEMBERS---------->

    def open_crewmember_details(self, crewmember_model : CrewmemberModel):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x400")
        self.temporary_window_frame = CrewmemberDetail(crewmember_model)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def add_crewmember(self):
        type_text = self.temporary_window_frame.dropdown_types.get()
        _type = self.types_dict[type_text]
        _full_name = self.temporary_window_frame.entry_full_name.get()
        _info = self.temporary_window_frame.info_entry_field.get("1.0", tk.END)
        _picpath = self.temporary_window_frame.entry_picpath.get()
        _fly_type = self.temporary_window_frame.entry_flytype.get()
        self.db.add_record("crewmembers",
                           _type + ";" + _full_name + ";" + _info + ";-1;0;0;-1;" + _picpath + ";" + _fly_type + ";")
        self.refresh()

    #       <--------CREWMEMBERS---------->

    #       <--------USERS---------->

    def open_users_details(self, user_model : UserModel):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x200")
        self.temporary_window_frame = UserDetail(user_model)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def add_user(self):
        _login = self.temporary_window_frame.entry_login.get()
        _password = self.temporary_window_frame.entry_password.get()
        role_text = self.temporary_window_frame.dropdown_roles.get()
        _role = self.roles_dict[role_text]
        _full_name = self.temporary_window_frame.entry_full_name.get()
        _info = self.temporary_window_frame.info_entry_field.get("1.0", tk.END)
        self.db.add_record("users", _login + ";" + _password + ";" + _role + ";" + _full_name + ";" + _info + ";" + "-1" + ";")
        self.refresh()
    #       <--------USERS---------->

    #       <--------CREWS---------->
    def open_crew_details(self, crew_model : CrewModel):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = CrewDetail(crew_model)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def get_available_crewmembers(self) -> list[CrewmemberModel]:
        models = self.db.get_all_from("crewmembers")
        output = []
        for model in models:
            if not model.idBindedToCrew:
                output.append(model)
        return output

    def add_crew(self):
        _name = self.temporary_window_frame.name_entry.get()
        _pilots = self.temporary_window_frame.list_of_pilots.get("1.0", tk.END).strip().split("\n")
        _stuards= self.temporary_window_frame.list_of_stuards.get("1.0", tk.END).strip().split("\n")
        to_bind_ids = []
        pilot_string = ""
        for pilot in _pilots:
            pilot_string += pilot + "|"
            to_bind_ids.append(pilot.split(" ")[0])
        stuard_string = ""

        for stuard in _stuards:
            if len(stuard.strip()) != 0:
                stuard_string += stuard + "|"
                to_bind_ids.append(stuard.split(" ")[0])
        self.db.add_record("crews", _name + ";" + pilot_string + ";" + stuard_string + ";0;")

        for id in to_bind_ids:
            self.db.alter("crewmembers", str(id), "IsBindedToCrew", 1)
        self.temporary_window.destroy()
        self.refresh()

    def get_available_crews(self) -> list[CrewModel]:
        models = self.db.get_all_from("crews")
        output = []
        for model in models:
            if not model.isOccupied:
                output.append(model)
        return output
    #       <--------CREWS---------->

    #       <--------FLIGHTS---------->
    def add_flight(self):
        _plane = self.temporary_window_frame.dropdown_planes.get()
        _datestart = self.temporary_window_frame.date_start_entry.get()
        _dateend = self.temporary_window_frame.date_end_entry.get()
        _direction = self.temporary_window_frame.dropdown_directions.get()
        _crew = self.temporary_window_frame.dropdown_crews.get()
        to_bind_plane = _plane.split(" ")[0]
        to_bind_crew = _crew.split(" ")[0]
        to_bind_direction = _direction.split(" ")[0]
        # flights_table.column_config = ["ID", "PlaneID" ,"DateStart", "DateEnd", "DirectionID", "CrewID"]
        self.db.add_record("flights", to_bind_plane + ";" + _datestart + ";" + _dateend + ";" + to_bind_direction + ";" + to_bind_crew + ";")

        self.db.alter("planes", to_bind_plane, "IsBinded", 1)
        self.db.alter("crews", to_bind_crew, "IsOccupied", 1)

        self.temporary_window.destroy()
        self.refresh()
    #       <--------FLIGHTS---------->


    #   <--------FRAME SPECIFIC METHODS---------->




