from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame
from frames.test_frame import TestFrame
from frames.admin_frame import AdminFrame
from frames.utility.direction import Direction
import database.DBEngine as db
import content_gen
from frames.scrollable_Frame import ScrollableFrame
from frames.utility.add_frames import AddDirectionFrame

from frames.utility.plane import *

from frames.utility.detail_frames import *

from tkinter import messagebox
import customtkinter as tk





class ContentDisplayRangeController():
    def __init__(self, max):
        self.low = 0
        if max > 5:
            self.high = 5
        else:
            self.high = max
        self.max = max
    def next_range(self):
        if self.low + 5 < self.max and self.high + 5 <= self.max:
            self.low += 5
            self.high += 5
        elif self.low + 5 < self.max and self.high + 5 > self.max:
            self.low += 5
            self.high = self.max
    def prev_range(self):
        if self.low - 5 >= 0:
            self.low -= 5
            self.high = self.low + 5
        elif self.low - 5 < 0:
            self.low = 0
            self.high = 5
    def print(self):
        print(self.low, " - ", self.high)
    def reset(self):
        self.low = 0
        if self.max > 5:
            self.high = 5
        else:
            self.high = self.max


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

        self.showed_frame = AdminFrame(root, self)
        self.showed_frame.create_widgets(self)

        self.current_content = ""

        self.content_range = ContentDisplayRangeController(0)
        self.content_range.low = 0
        self.content_range.high = 5

    def switch_to_frame(self, frame_name_show):
        self.showed_frame.destroy()
        frame_class = globals()[frame_name_show]
        self.showed_frame = frame_class(self.root,self)
        self.showed_frame.create_widgets(self)
        self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title):
        self.root.title(title)

    #   <--------FRAME SPECIFIC METHODS---------->
    #       <--------AUTH---------->
    def authframe_login_submit(self):
        login = self.showed_frame.field_login.get()
        password = self.showed_frame.field_password.get()
        response = self.db.authenticate(login, password)
        if not response.fail:
            self.switch_to_frame(response.frame())
        else:
            messagebox.showerror("Ошибка","Такого пользователя не существует, или пароль неверный")

    #       <--------AUTH---------->
    def refresh(self):
        self.populate_panel_with_content(self.current_content)


    def delete_by_id(self, table, id):
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.db.delete_by_id(table, id)
            self.refresh()

    def add_direction(self, dir):
        _from = self.temporary_window_frame.entry_from.get()
        _to = self.temporary_window_frame.entry_to.get()
        self.db.add_record("directions", _from + ";" + _to)
        self.refresh()



    def open_add_record_window(self):
        if self.current_content == "directions":
            self.temporary_window = tk.CTkToplevel(self.root)
            self.temporary_window.geometry("500x500")
            self.temporary_window_frame = AddDirectionFrame(self.temporary_window, self)
            self.temporary_window_frame.create_widgets(self)

    def open_plane_details(self, id, plane_info):
        self.temporary_window = tk.CTkToplevel(self.root)
        self.temporary_window.geometry("1000x800")
        self.temporary_window_frame = PlaneDetail(id,plane_info)
        self.temporary_window_frame.create_widgets(self.temporary_window, self)

    def place_plane_on_repair(self, id):

        malfunction_text = self.temporary_window_frame.malfunction_entry_field.get("1.0", tk.END)
        self.db.alter("planes", id, "Malfunction", malfunction_text)
        self.db.alter("planes", id, "IsRepaired", 1)

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
        self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)





