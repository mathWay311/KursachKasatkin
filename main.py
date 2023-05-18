import customtkinter as tk
from frames.auth_frame import AuthFrame
from frames.test_frame import FrameTest

class WinManager():
    def __init__(self, root):
        self.frames = {"AUTH": AuthFrame(root, self),
                       "WIN2": FrameTest(root, self)
                       }
        for frame in self.frames.values():
            frame.create_widgets(self)

    def switch_to_frame(self, frame_name_hide, frame_name_show):
        self.frames[frame_name_hide].pack_forget()
        self.frames[frame_name_show].pack()


if __name__ == '__main__':
    root = tk.CTk()
    winmg = WinManager(root)
    root.mainloop()
