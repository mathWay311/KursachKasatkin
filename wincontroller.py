from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame
from frames.test_frame import TestFrame
from frames.admin_frame import AdminFrame

import customtkinter as tk



class WinController():
    def __init__(self, root):

        self.root = root
        self.showed_frame = ""

        self.title_dict = {
            "AuthFrame": "G7 Airlines - Авторизация",
            "PilotFrame": "Окно пилота",
            "AdminFrame": "Администратор",
            "TestFrame": "Debug"
        }

        self.showed_frame = AuthFrame(root, self)
        self.showed_frame.create_widgets(self)

    def switch_to_frame(self, frame_name_show):
        self.showed_frame.destroy()
        frame_class = globals()[frame_name_show]
        self.showed_frame = frame_class(self.root,self)
        self.showed_frame.create_widgets(self)
        self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title):
        self.root.title(title)