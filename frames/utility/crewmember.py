import customtkinter as tk
from frame import BaseFrame

from database.models.models import CrewmemberModel
from main import WINDOW_WIDTH
from frames.utility.get_image import *

class Crewmember():
    def __init__(self, crewmember_model : CrewmemberModel ,controller, parent_frame):
        self.model= crewmember_model

        path_string = "database/images/" + self.model.imagePath
        crewmember_logo_img = get_image(path_string, (200, 200))

        dir_rect = tk.CTkFrame(parent_frame, height=200, width=WINDOW_WIDTH,
                               fg_color="#6FB1DE")

        if self.model.isOccupied:
            dir_rect.configure(fg_color="#4C738F")
        if not self.model.isRetired and not self.model.isOccupied and not self.model.isBindedToCrew and not self.model.isInFlight:
            dir_rect.configure(fg_color="#96D3FF")

        crewmember_logo = tk.CTkLabel(dir_rect, image=crewmember_logo_img, text="")
        label_brand = tk.CTkLabel(dir_rect, text=self.model.full_name, font=("Roboto", 26))

        type_text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.model.type == "pilot":
            type_text = "Пилот(-есса)"
        elif self.model.type == "stuard":
            type_text = "Стюард(-есса)"
        label_additional_info = tk.CTkLabel(dir_rect,
                                  text= type_text + "\n" + self.model.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_crewmember_details(self.model))

        button_edit = tk.CTkButton(dir_rect, text="Редактировать", font=("Roboto", 16), text_color="#FFFFFF", fg_color="#FFD37C",
                              command=lambda: controller.edit_crewmember_window(self.model))


        crewmember_logo.place(x=0, relheight=1)
        button_edit.place(relheight = 0.2, relx = 0.8)
        button.place(relheight=0.2, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)