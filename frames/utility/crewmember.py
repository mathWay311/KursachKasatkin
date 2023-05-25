import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from database.models.models import CrewmemberModel

class Crewmember():
    def __init__(self, crewmember_model : CrewmemberModel ,controller, parent_frame):
        self.model= crewmember_model

        crewmember_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.model.imagePath), size=(200, 200))

        dir_rect = tk.CTkFrame(parent_frame, height=200, width=1600,
                               fg_color="#6FB1DE")

        if self.model.isOccupied:
            dir_rect.configure(fg_color="#4C738F")

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



        crewmember_logo.place(x=0, relheight=1)
        button.place(relheight=0.2, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)