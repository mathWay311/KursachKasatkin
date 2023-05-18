import copy

import customtkinter as tk
from frames.auth_frame import AuthFrame
from frames.pilot_frame import PilotFrame

class WinManager():
    def __init__(self, root):
        self.frame_names = {"AUTH": "AuthFrame",
                       "PILOT": "PilotFrame"
                       }

        self.showed_frame = ""

        self.title_dict = {
            "AUTH": "G7 Airlines - Авторизация",
            "PILOT": "Окно пилота"
        }

        self.showed_frame = AuthFrame(root, self)
        self.showed_frame.create_widgets(self)

        self.root = root

    def switch_to_frame(self, frame_name_hide, frame_name_show):
        self.showed_frame.destroy()
        frame_class = globals()[self.frame_names[frame_name_show]]
        self.showed_frame = frame_class(root,self)
        self.showed_frame.create_widgets(self)
        self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title):
        self.root.title(title)


if __name__ == '__main__':
    root = tk.CTk()
    root.title("G7 Airlines - Авторизация")
    root.geometry("600x600")
    root.resizable(1,1)

    winmg = WinManager(root)
    root.mainloop()
