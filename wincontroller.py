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

        self.showed_frame = AdminFrame(root, self)
        self.showed_frame.create_widgets(self)

        self.current_content = ""


    def switch_to_frame(self, frame_name_show):
        self.showed_frame.destroy()
        frame_class = globals()[frame_name_show]
        self.showed_frame = frame_class(self.root,self)
        self.showed_frame.create_widgets(self)
        self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title):
        self.root.title(title)

    #   <--------GENERIC---------->

    # Удаление предмета из базы с закрытием окна
    def delete_item_by_id(self,table_name,id):
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.db.delete_by_id(table_name, id)
            self.temporary_window.destroy()
            self.refresh()

    # Удаление предмета из базы без закрытия окна (нужно только для направлений)
    def delete_by_id(self, table, id):
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.db.delete_by_id(table, id)
            self.refresh()

    # Обновить страницу
    def refresh(self):
        self.populate_panel_with_content(self.current_content)

    # Открыть окно добавления предмета (универсальный метод)
    def open_add_record_window(self):
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

    # Вывести контент на панель
    def populate_panel_with_content(self, content_name):
        self.current_content = content_name
        lines = self.db.get_all_from(content_name)
        self.showed_frame.content_panel.destroy()
        self.showed_frame.content_panel = ScrollableFrame(self.showed_frame)
        scrollbar = tk.CTkScrollbar

        for i in range(len(lines)):
            line = lines[i].split(";")
            if content_name == "directions":
                dir = Direction(line, self, self.showed_frame.content_panel.scrollable_frame, line[0])
            if content_name == "planes":
                plane_info = PlaneInfo(line)
                plane = Plane(plane_info, self, self.showed_frame.content_panel.scrollable_frame, line[0])
            if content_name == "crewmembers":
                crewmember_info = CrewmemberInfo(line)
                crewmember = Crewmember(crewmember_info, self, self.showed_frame.content_panel.scrollable_frame, line[0])
            if content_name == "users":
                user_info = UserInfo(line)
                user = User(user_info, self, self.showed_frame.content_panel.scrollable_frame, line[0])
            if content_name == "crews":
                crew_info = CrewInfo(line)
                crew = Crew(crew_info, self, self.showed_frame.content_panel.scrollable_frame, line[0])
            if content_name == "flights":
                flight_info = FlightInfo(line)
                flight_text = self.db.search_list("crews", "ID", str(flight_info.crewID))
                flight_info.crewName = flight_text[1]

                plane_text = self.db.search_list("planes", "ID", str(flight_info.planeID))
                flight_info.planeName = plane_text[1] + plane_text[2]

                dir_text = self.db.search_list("directions", "ID", str(flight_info.directionID))
                flight_info.dirName = dir_text[1] + " - " + dir_text[2]

                fli = Flight(flight_info, self, self.showed_frame.content_panel.scrollable_frame, line[0])

        self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

    #   <--------GENERIC---------->

    #   <--------FRAME SPECIFIC METHODS---------->
    #       <--------AUTH---------->

    def authframe_login_submit(self):
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

    def add_direction(self, dir):
        _from = self.temporary_window_frame.entry_from.get()
        _to = self.temporary_window_frame.entry_to.get()
        self.db.add_record("directions", _from + ";" + _to)
        self.refresh()

    #       <--------DIRECTIONS---------->



    #       <--------PLANES---------->
    def open_plane_details(self, id, plane_info):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = PlaneDetail(id,plane_info)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def place_plane_on_repair(self, id):
        malfunction_text = self.temporary_window_frame.malfunction_entry_field.get("1.0", tk.END)
        self.db.alter("planes", str(id), "Malfunction", malfunction_text)
        self.db.alter("planes", str(id), "IsRepaired", 1)
        self.db.alter("planes", str(id), "IsOccupied", 1)
        self.temporary_window.destroy()
        self.refresh()

    def retrieve_plane_from_repair(self, id):
        self.db.alter("planes", str(id), "Malfunction", "")
        self.db.alter("planes", str(id), "IsRepaired", 0)
        self.db.alter("planes", str(id), "IsOccupied", 0)
        self.temporary_window.destroy()
        self.refresh()
        ["ID", "Brand", "Model", "BoardNum", "IsOccupied", "IsRepaired", "Malfunction", "ImagePath"]
    def add_plane(self):
        _brand = self.temporary_window_frame.dropdown_brand.get()
        _model = self.temporary_window_frame.dropdown_type.get()
        _boardnum = self.temporary_window_frame.entry_boardnum.get()
        _picpath = self.temporary_window_frame.entry_picpath.get()
        self.db.add_record("planes",
                           _brand + ";" + _model + ";" + _boardnum + ";0;0;;" + _picpath + ";")
        self.refresh()

    #       <--------PLANES---------->



    #       <--------CREWMEMBERS---------->

    def open_crewmember_details(self, id, crewmember_info):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x400")
        self.temporary_window_frame = CrewmemberDetail(id, crewmember_info)
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

    def open_users_details(self, id, user_info):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x200")
        self.temporary_window_frame = UserDetail(id, user_info)
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
    def open_crew_details(self, id, crew_info):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = CrewDetail(id,crew_info)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)
    #       <--------CREWS---------->

    #   <--------FRAME SPECIFIC METHODS---------->




