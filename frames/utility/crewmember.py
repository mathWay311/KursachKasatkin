import customtkinter as tk
from frame import BaseFrame
from PIL import Image


class CrewmemberInfo():
    def __init__(self, line):
        self.id = int(line[0])
        self.type = line[1]
        self.full_name = line[2]
        self.info = line[3]
        self.crewID = int(line[4])
        self.isOccupied = bool(int(line[5]))
        self.isRetired = bool(int(line[6]))
        self.FlightID = int(line[7])
        self.imagePath = line[8]
        self.fliesType = line[9]

    def print_status(self):
        text = ""
        if self.isOccupied and self.isRetired:
            text+= "Статус: В отпуске или недоступен\n"
        elif self.isOccupied:
            text += "Статус: В полёте\n"
        else:
            text+= "Статус: Свободен\n"

        return text


class Crewmember():
    def __init__(self, crewmember_info ,controller, parent_frame, id):
        self.id = id
        self.crewmember_info = crewmember_info

        crewmember_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.crewmember_info.imagePath), size=(200, 200))

        dir_rect = tk.CTkFrame(parent_frame, height=200, width=1600,
                               fg_color="#6FB1DE")

        crewmember_logo = tk.CTkLabel(dir_rect, image=crewmember_logo_img, text="")
        label_brand = tk.CTkLabel(dir_rect, text=self.crewmember_info.full_name, font=("Roboto", 26))

        type_text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.crewmember_info.type == "pilot":
            type_text = "Пилот(-есса)"
        elif self.crewmember_info.type == "stuard":
            type_text = "Стюард(-есса)"
        label_additional_info = tk.CTkLabel(dir_rect,
                                  text= type_text + "\n" + self.crewmember_info.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_crewmember_details(self.id, self.crewmember_info))



        crewmember_logo.place(x=0, relheight=1)
        button.place(relheight=0.2, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)