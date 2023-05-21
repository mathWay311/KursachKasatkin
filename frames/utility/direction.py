import customtkinter as tk
from frame import BaseFrame


class Direction(BaseFrame):
    def create_widgets(self, controller, parent_frame):
        self.configure(height=80)
        self.configure(width=1200)
        self.configure(fg_color="#00FF00")
        self.configure(master = parent_frame)
        self.label = tk.CTkLabel(parent_frame, text = "")
        self.label.pack(side=tk.LEFT)
