from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame
from frames.test_frame import TestFrame
from frames.admin_frame import AdminFrame
from frames.utility.direction import Direction
import database.DBEngine as db
import content_gen

from tkinter import messagebox
import customtkinter as tk


class ScrollableFrame(tk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.CTkCanvas(self)
        scrollbar = tk.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        self.scrollable_frame = tk.CTkFrame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



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

    def populate_panel_with_content(self, content_name):
        if content_name == "Directions":
            lines = self.db.get_all_from("directions")
            self.content_range.max = len(lines)


            self.showed_frame.content_panel.destroy()
            self.showed_frame.content_panel = tk.CTkFrame(self.showed_frame.content_container)
            scrollbar = tk.CTkScrollbar
            self.showed_frame.content_panel.pack(side=tk.RIGHT, anchor=tk.SE, fill=tk.BOTH, expand = 1)

            for i in range(12):
                line = lines[i].split(";")
                dir_rect = tk.CTkFrame(self.showed_frame.content_panel, height=80, width=1200, fg_color="#6FB1DE")
                label = tk.CTkLabel(dir_rect, text = line[1] + " - " + line[2], font = ("Roboto", 26))
                label.place(relx = 0.1, relheight = 1)
                dir_rect.pack()






