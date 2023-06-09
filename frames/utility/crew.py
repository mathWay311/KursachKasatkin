import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from database.models.models import CrewModel
from main import WINDOW_WIDTH

class Crew():
    def __init__(self, crew_model : CrewModel, controller, parent_frame):
        self.model = crew_model

        dir_rect = tk.CTkFrame(parent_frame, height=100, width=WINDOW_WIDTH,
                               fg_color="#6FB1DE")


        label_name = tk.CTkLabel(dir_rect, text=self.model.name, font=("Roboto", 26))


        label_additional_info = tk.CTkLabel(dir_rect,
                                  text= self.model.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_crew_details(self.model))

        edit_button = tk.CTkButton(dir_rect, text="Редактировать", font=("Roboto", 16), text_color="#FFFFFF",
                                   fg_color="#FFD37C",
                                   command=lambda: controller.edit_crew_window(self.model))

        edit_button.place(relheight = 1, relx = 0.8)
        button.place(relheight=1, relx=0.9)
        label_name.place(relheight=1, x=30)
        label_additional_info.place(relx = 0.5, relheight=1)
        dir_rect.pack(fill=tk.X, pady=1)