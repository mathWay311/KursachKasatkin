from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame
from frames.test_frame import TestFrame
from frames.admin_frame import AdminFrame
from frames.flight_manager_frame import FlightManagerFrame
from frames.plane_manager_frame import PlaneManagerFrame
from frames.crew_manager_frame import CrewManagerFrame


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

from frames.utility.edit_frames import *

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
            "FlightManagerFrame": "Менеджер Рейсов",
            "CrewManagerFrame": "Менеджер ЛС",
            "PlaneManagerFrame": "Менеджер ВС",
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

        self.role = ""
        self.id_user = ""


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
        if table_name == "planes":
            if not self.auth_check(["admin", "plane_manager"]):
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ВС может удалить самолёт")
                return
        if table_name == "crews":
            if not self.auth_check(["admin", "crew_manager"]):
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ЛС может удалить экипаж")
                return
        if table_name == "crewmembers":
            if not self.auth_check(["admin", "crew_manager"]):
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ЛС может удалить члена ЛС")
                return
        if table_name == "users":
            if not self.auth_check(["admin"]):
                messagebox.showerror("Нет доступа", "Только администратор может удалить пользователя")
                return
        if table_name == "flights":
            if not self.auth_check(["admin", "flight_manager"]):
                messagebox.showerror("Нет доступа", "Только администратор или менеджер рейсов может удалить рейс")
                return


        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            if table_name == "flights":
                self.release_from_flight_by_id(id)
            if table_name == "crews":
                self.db.release_bind(id)
            self.db.delete_by_id(table_name, id)
            self.temporary_window.destroy()
            self.refresh()

    def delete_crewmember(self, model : CrewmemberModel):
        """
        Удаляет члена лётного состава из базы, удаляя аккаунт
        Args:
            model: Модель получаемая из представления

        Returns:

        """
        user = self.db.search_model("users", "CrewmemberID", model.id)
        if user:
            self.db.delete_by_id("users", user.id)
        self.delete_item_by_id("crewmembers", model.id)


    def delete_by_id(self, table, id):
        """
        Удалить предмет по ID без закрытия текущего окна (в случае если кнопка удалить не находится внутри временного окна)

        Args:
            table:
                Наименование таблицы в формате, например "users"
            id:
                Идентификатор предмета для удаления
        """
        if table == "directions":
            if self.auth_check(["admin"]):
                result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
                if result:
                    self.db.delete_by_id(table, id)
                    self.refresh()
            else:
                messagebox.showerror("Нет доступа", "Только администратор может удалять направления")


    def refresh(self):
        self.db.refresh_current_flight_state()
        if not self.role == "pilot":
            self.populate_panel_with_content(self.current_content)
        else:
            self.show_status_to_pilot()


    def show_status_to_pilot(self):
        crews = self.db.get_all_from("crews")
        for crew in crews:
            ids = crew.pilotstring + crew.stuardstring
            ids = ids.split("|")
            ids.pop(-1)
            found = False

            for id in ids:
                id = id.split(" ")[0]
                user = self.db.search_model("users", "CrewmemberID", str(id))
                if user:
                    print(str(self.id_user) + "|" + str(user.id)+ "|")
                    if str(self.id_user) == str(user.id):
                        print("debug: found")
                        found = True

            if found:
                print("debug: found 2")
                flight_model = self.db.search_model("flights", "CrewID", crew.id)
                if flight_model:
                    plane = self.db.search_model("planes", "ID", str(flight_model.planeID))
                    dir = self.db.search_model("directions", "ID", str(flight_model.directionID))
                    self.showed_frame.info_label.configure(text = "Вы назначены на рейс\n" + dir.from_ + "-" + dir.to_ + "\nСамолёт:" + plane.brand + " " + plane.model + "\nВылет:" + flight_model.date_start + "\nПрилёт: " + flight_model.date_end)
                    return
        self.showed_frame.info_label.configure(text = "Пока нет назначений")


    def open_add_record_window(self):
        """
        Открыть новое окно для добавления нового обьекта в базу
        """

        if self.current_content == "directions":
            if self.auth_check(["admin"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddDirectionFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор может добавлять направления")
        if self.current_content == "users":
            if self.auth_check(["admin"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddUserFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор может добавлять пользователей")
        if self.current_content == "crewmembers":
            if self.auth_check(["admin", "crew_manager"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddCrewMemberFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ЛС может добавлять членов ЛС")
        if self.current_content == "planes":
            if self.auth_check(["admin", "plane_manager"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddPlaneFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ВС может добавлять самолёты")
        if self.current_content == "crews":
            if self.auth_check(["admin", "crew_manager"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddCrewFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор или менеджер ЛС может добавлять экипажи")
        if self.current_content == "flights":
            if self.auth_check(["admin", "flight_manager"]):
                self.temporary_window = tk.CTkToplevel(self.root)
                self.temporary_window.geometry("500x500")
                self.temporary_window_frame = AddFlightFrame(self.temporary_window, self)
                self.temporary_window_frame.create_widgets(self)
            else:
                messagebox.showerror("Нет доступа", "Только администратор или менеджер рейсов может добавлять рейсы")


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

    def auth_check(self, availables : list[str]) -> bool:
        """
        Проверка аутентификации для того или иного прецедента. Вызывается перед прецедентом

        Args:
            availables: Список разрешённых ролей

        Returns:

        """
        if self.role in availables:
            return True
        else:
            return False

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
            self.id_user = response.id
            self.role = response.role
        else:
            messagebox.showerror("Ошибка","Такого пользователя не существует, или пароль неверный")

    def unauthorize(self):
        self.role = ""
        self.id_user = ""
        self.switch_to_frame("AuthFrame")

    #       <--------AUTH---------->

    #       <--------DIRECTIONS---------->

    def add_direction(self):
        """
        Добавить направление
        """
        _from = self.temporary_window_frame.entry_from.get()
        _to = self.temporary_window_frame.entry_to.get()
        self.db.add_record("directions", _from + ";" + _to + ";")
        self.refresh()

    def get_available_directions(self) -> list[DirectionModel]:
        models = self.db.get_all_from("directions")
        output = []
        for model in models:
            output.append(model)
        return output

    def edit_direction_window(self, direction_model):
        if self.auth_check(["admin"]):
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditDirectionFrame(self.temporary_window, self, direction_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")

    def edit_direction(self):
        model = self.temporary_window_frame.model
        _from =  self.temporary_window_frame.entry_from.get()
        _to = self.temporary_window_frame.entry_to.get()
        self.db.alter("directions", model.id, "From", _from)
        self.db.alter("directions", model.id, "To", _to)
        self.temporary_window.destroy()
        self.refresh()

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
                           _brand + ";" + _model + ";" + _boardnum + ";0;0;;" + _picpath + ";0;")
        self.refresh()

    def get_available_planes(self) -> list[PlaneModel]:
        models = self.db.get_all_from("planes")
        output = []
        for model in models:
            if not model.isBinded:
                output.append(model)
        return output

    def edit_plane_window(self, direction_model):
        if self.auth_check(["admin", "plane_manager"]):
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditPlaneFrame(self.temporary_window, self, direction_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")
    def edit_plane(self):
        model = self.temporary_window_frame.model
        _brand = self.temporary_window_frame.dropdown_brand.get()
        _model = self.temporary_window_frame.dropdown_type.get()
        _board_num = self.temporary_window_frame.entry_boardnum.get()
        _image_path = self.temporary_window_frame.entry_picpath.get()
        self.db.alter("planes", model.id, "Brand", _brand)
        self.db.alter("planes", model.id, "Model", _model)
        self.db.alter("planes", model.id, "BoardNum", _board_num)
        self.db.alter("planes", model.id, "ImagePath", _image_path)
        self.temporary_window.destroy()
        self.refresh()

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
        _login = self.temporary_window_frame.entry_login.get()
        _password = self.temporary_window_frame.entry_password.get()

        if self.db.is_login_available(_login):
            id = self.db.add_record("crewmembers",
                               _type + ";" + _full_name + ";" + _info + ";-1;0;0;-1;" + _picpath + ";" + _fly_type + ";0;0;")

            self.db.add_user(UserModel([-1, _login, _password, "pilot", _full_name, _info, id]))
        else:
            messagebox.showerror("Ошибка", "Такой логин уже существует")
        self.refresh()

    def edit_crewmember_window(self, crewmb_model : CrewmemberModel):
        if self.auth_check(["admin", "crew_manager"]):
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditCrewmemberFrame(self.temporary_window, self, crewmb_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")


    def edit_crewmember(self):
        model = self.temporary_window_frame.model
        _type = self.temporary_window_frame.dropdown_types.get()
        _type = self.types_dict[_type]
        _full_name = self.temporary_window_frame.entry_full_name.get()
        _info = self.temporary_window_frame.info_entry_field.get("1.0", tk.END)
        _imgPath = self.temporary_window_frame.entry_picpath.get()
        _fliesType = self.temporary_window_frame.entry_flytype.get()

        self.db.alter("crewmembers", model.id, "Type", _type)
        self.db.alter("crewmembers", model.id, "FullName", _full_name)
        self.db.alter("crewmembers", model.id, "Info", _info)
        self.db.alter("crewmembers", model.id, "ImagePath", _imgPath)
        self.db.alter("crewmembers", model.id, "FliesType", _fliesType)

        self.temporary_window.destroy()
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

    def edit_user_window(self, user_model : UserModel):
        if self.auth_check(["admin"]):
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditUserFrame(self.temporary_window, self, user_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")

    def edit_user(self):
        model = self.temporary_window_frame.model
        _login = self.temporary_window_frame.entry_login2.get()
        _password = self.temporary_window_frame.entry_password.get()
        role_text = self.temporary_window_frame.dropdown_roles.get()
        _role = self.roles_dict[role_text]
        _full_name = self.temporary_window_frame.entry_full_name.get()
        _info = self.temporary_window_frame.info_entry_field.get("1.0", tk.END)

        if self.db.is_login_available(_login) or _login == model.login:
            self.db.alter("users", model.id, "Login", _login)
            self.db.alter("users", model.id, "Password", _password)
            self.db.alter("users", model.id, "Role", _role)
            self.db.alter("users", model.id, "FullName", _full_name)
            self.db.alter("users", model.id, "Info", _info)
            self.temporary_window.destroy()
            self.refresh()
        else:
            messagebox.showerror("Ошибка", "Такой логин уже существует")

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
            if not model.isBindedToCrew:
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

    def edit_crew_window(self, crew_model : CrewModel):
        if self.auth_check(["admin", "plane_manager"]):
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditCrewFrame(self.temporary_window, self, crew_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")

    def edit_crew(self):
        model = self.temporary_window_frame.model
        _name = self.temporary_window_frame.name_entry.get()
        _pilots = self.temporary_window_frame.list_of_pilots.get("1.0", tk.END).strip().split("\n")
        _stuards = self.temporary_window_frame.list_of_stuards.get("1.0", tk.END).strip().split("\n")
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

        unbind_ids = (model.pilotstring + model.stuardstring).split("|")
        unbind_ids.pop(-1)
        print(unbind_ids)
        print(to_bind_ids)

        for id in unbind_ids:
            print(id)
            id = id.split(" ")[0]

            self.db.alter("crewmembers", str(id), "IsBindedToCrew", 0)
        for id in to_bind_ids:
            self.db.alter("crewmembers", str(id), "IsBindedToCrew", 1)

        self.db.alter("crews", str(model.id), "Name", _name)
        self.db.alter("crews", str(model.id), "PilotString", pilot_string)
        self.db.alter("crews", str(model.id), "StuardString", stuard_string)


        self.temporary_window.destroy()
        self.refresh()

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

        self.db.add_record("flights", to_bind_plane + ";" + _datestart + ";" + _dateend + ";" + to_bind_direction + ";" + to_bind_crew + ";0;" )

        self.occupy_for_flight(to_bind_plane, to_bind_crew)

        self.temporary_window.destroy()
        self.refresh()

    def open_flight_details(self, flight_model : FlightModel):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = FlightDetail(flight_model)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def release_from_flight_by_id(self, id):
        flight_model = self.db.search_model("flights", "ID", id)
        self.db.alter("planes", str(flight_model.planeID), "IsBinded", 0)
        self.db.alter("planes", str(flight_model.planeID), "IsFlying", 0)
        self.db.alter("crews", str(flight_model.crewID), "IsOccupied", 0)
        self.db.release_crew(flight_model.crewID)

    def occupy_for_flight(self, to_bind_plane : str, to_bind_crew : str):
        self.db.alter("planes", to_bind_plane, "IsBinded", 1)
        self.db.alter("crews", to_bind_crew, "IsOccupied", 1)
        self.db.occupy_crew(to_bind_crew)

    def edit_flight_window(self, flight_model : FlightModel):
        if self.auth_check(["admin", "flight_manager"]) and not flight_model.isStarted:
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("1000x800")
            self.temporary_window_frame = EditFlightFrame(self.temporary_window, self, flight_model)
            self.temporary_window_frame.create_widgets(self)
        else:
            messagebox.showerror("Ошибка", "Нет доступа")

    def edit_flight(self):
        model = self.temporary_window_frame.model
        self.release_from_flight_by_id(model.id)
        _plane = self.temporary_window_frame.dropdown_planes.get()
        _datestart = self.temporary_window_frame.date_start_entry.get()
        _dateend = self.temporary_window_frame.date_end_entry.get()
        _direction = self.temporary_window_frame.dropdown_directions.get()
        _crew = self.temporary_window_frame.dropdown_crews.get()
        to_bind_plane = _plane.split(" ")[0]
        to_bind_crew = _crew.split(" ")[0]
        to_bind_direction = _direction.split(" ")[0]
        # flights_table.column_config = ["ID", "PlaneID" ,"DateStart", "DateEnd", "DirectionID", "CrewID"]
        self.db.alter("flights", model.id, "PlaneID", to_bind_plane)
        self.db.alter("flights", model.id, "DateStart", _datestart)
        self.db.alter("flights", model.id, "DateEnd", _dateend)
        self.db.alter("flights", model.id, "DirectionID", to_bind_direction)
        self.db.alter("flights", model.id, "CrewID", to_bind_crew)

        self.occupy_for_flight(to_bind_plane, to_bind_crew)

        self.temporary_window.destroy()
        self.refresh()


    #       <--------FLIGHTS---------->


    #   <--------FRAME SPECIFIC METHODS---------->




