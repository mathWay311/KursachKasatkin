import customtkinter as tk
from frame import BaseFrame
from database.models.models import *
from main import WINDOW_WIDTH
class Direction():
    def __init__(self, dir_model : DirectionModel, controller, parent_frame):
        self.model = dir_model
        self.id = self.model.id
        dir_rect = tk.CTkFrame(parent_frame, height=80, width=WINDOW_WIDTH,
                               fg_color="#6FB1DE")
        label = tk.CTkLabel(dir_rect, text=self.model.from_ + " - " + self.model.to_, font=("Roboto", 26))
        button_edit = tk.CTkButton(dir_rect, text="Редактировать", fg_color="#FFD37C", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda: controller.edit_direction_window(self.model))

        button = tk.CTkButton(dir_rect, text="Удалить", fg_color="#FF7CA3", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.delete_by_id("directions", self.model.id))
        button_edit.place(relheight = 1, relx = 0.8)
        button.place(relheight=1, relx=0.9)
        label.place(relheight=1, x=50)
        dir_rect.pack(fill=tk.X, pady=1)
