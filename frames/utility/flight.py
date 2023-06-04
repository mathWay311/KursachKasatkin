import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from database.models.models import *
from main import WINDOW_WIDTH
class Flight():
    def __init__(self, flight_model: FlightModel ,controller, parent_frame):
        self.model = flight_model


        dir_rect = tk.CTkFrame(parent_frame, height=80, width=WINDOW_WIDTH,
                               fg_color="#6FB1DE")

        label_info = tk.CTkLabel(dir_rect, text=self.model.print(), font=("Roboto", 14))

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF", command=lambda :controller.open_flight_details(self.model))

        edit_button = tk.CTkButton(dir_rect, text="Редактировать", font=("Roboto", 16), text_color="#FFFFFF",fg_color="#FFD37C",
                              command=lambda: controller.edit_flight_window(self.model))

        edit_button.place(relheight = 1, relx = 0.8)
        button.place(relheight=1, relx=0.9)
        label_info.place(relheight=1, x=30)
        dir_rect.pack(fill=tk.X, pady=1)