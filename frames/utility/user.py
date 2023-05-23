import customtkinter as tk
from frame import BaseFrame
from PIL import Image

class UserInfo():
    def __init__(self, line):
        self.id = int(line[0])
        self.login = line[1]
        self.password = line[2]
        self.role = line[3]
        self.full_name = line[4]
        self.info = line[5]
        self.crewID = int(line[6])


class User():
    def __init__(self, user_info ,controller, parent_frame, id):
        self.id = id
        self.user_info = user_info


        dir_rect = tk.CTkFrame(parent_frame, height=80, width=1600,
                               fg_color="#6FB1DE")

        label_name = tk.CTkLabel(dir_rect, text=self.user_info.full_name, font=("Roboto", 26))

        text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.user_info.role == "admin":
            text = "Администратор"
        if self.user_info.role == "pilot":
            text = "Пилот/Стюард"
        if self.user_info.role == "crew_manager":
            text = "Менеджер ЛС"
        if self.user_info.role == "flight_manager":
            text = "Менеджер Рейсов"
        if self.user_info.role == "plane_manager":
            text = "Менеджер ВС"

        label_additional_info = tk.CTkLabel(dir_rect,
                                  text= text,
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF", command= lambda : controller.open_users_details(self.id, self.user_info))



        button.place(relheight=1, relx=0.9)
        label_name.place(relheight=1, x=30)
        label_additional_info.place(relheight = 1,relx = 0.5)
        dir_rect.pack(fill=tk.X, pady=1)